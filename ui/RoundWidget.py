from PySide2 import QtWidgets
from PySide2.QtCore import Slot, QCoreApplication, QSortFilterProxyModel, Qt
from PySide2.QtWidgets import QMessageBox
from .ui_RoundWidget import Ui_RoundWidget
from ui import MatchWidget
from ui.WaitingPlayersWidget import WaitingPlayersWidget
from .RoundPlayersTableModel import RoundPlayersTableModel

class RoundWidget(QtWidgets.QWidget, Ui_RoundWidget):

    def __init__(self, parent=None):
        super().__init__(parent)
        self.setupUi(self)

        self.fields = {}
        self.parent = parent

        # signal button
        self.button_random.clicked.connect(self.slot_on_random)
        self.button_swiss.clicked.connect(self.slot_on_swiss_random)
        self.button_next_round.clicked.connect(self.slot_on_next_round)
        self.button_previous_round.clicked.connect(self.slot_on_previous_round)
        self.button_random_scores.clicked.connect(self.slot_on_random_scores)
        self.button_next_round.setEnabled(False)
        self.button_erase_score.clicked.connect(self.slot_on_erase_scores)

    def set_round(self, round):
        self.round = round
        n = round.number
        s = QCoreApplication.translate("RoundWidget", u"Tour n\u00b0"+str(n), None)
        self.toolBox.setItemText(self.toolBox.indexOf(self.page), s)
        s = QCoreApplication.translate("RoundWidget", u"Joueurs et options du tour n\u00b0" + str(n), None)
        self.toolBox.setItemText(1, s)

        # new match widgets
        self.match_widgets = []
        for m in round.matches:
            mw = MatchWidget.MatchWidget(parent=self)
            mw.set_match(m)
            mw.match_status_has_changed.connect(self.slot_on_match_status_changed)
            self.match_widgets.append(mw)

        # remove current widgets
        c = self.main_layout.takeAt(0)
        while c:
            c.widget().setParent(None)
            del c
            c = self.main_layout.takeAt(0)

        # add new ones
        r = 0
        c = 0
        for mw in self.match_widgets:
            self.main_layout.addWidget(mw, r, c)
            if c == 0:
                c = 1
            else:
                c = 0
                r = r+1
        if len(self.round.waiting_players) > 0:
            wpw = WaitingPlayersWidget(self)
            wpw.set_waiting_players(self.round)
            self.main_layout.addWidget(wpw, r, c)

        # update status
        self.slot_on_match_status_changed()
        self.slot_on_round_termination_changed()

        # update options
        self.spin_fields.setValue(self.round.fields_number)
        self.spin_max_point_value.setValue(self.round.max_point_value)
        self.spin_win_point_value.setValue(self.round.win_point_value)

        # set current tab
        self.toolBox.setCurrentIndex(0)

        # debug mode
        self.button_random_scores.setEnabled(self.round.debug_mode)
        self.button_random_scores.setVisible(self.round.debug_mode)
        self.round.debug_mode_changed.connect(self.slot_on_debug_mode_changed)

        # connection
        self.round.round_termination_changed.connect(self.slot_on_round_termination_changed)
        self.round.round_started_changed.connect(self.slot_on_round_start_changed)

        # set player list
        self.setup_players_list()

    @Slot()
    def slot_on_random(self):
        if self.round.terminated:
            return
        self.round.match_generation_mode = 'random'
        self.generate_matches()

    @Slot()
    def slot_on_swiss_random(self):
        self.round.match_generation_mode = 'swiss'
        self.generate_matches()

    def generate_matches(self):
        for m in self.round.matches:
            self.round.remove_match_for_players(m)
        self.round.matches.clear()
        self.round.fields_number = self.spin_fields.value()
        self.round.set_max_point_value(self.spin_max_point_value.value())
        self.round.set_win_point_value(self.spin_win_point_value.value())
        self.round.create_matches()
        self.set_round(self.round)

    @Slot()
    def slot_on_random_scores(self):
        if self.round.terminated:
            return
        self.round.random_scores()
        for mw in self.match_widgets:
            mw.set_match(mw.match)

    @Slot()
    def slot_on_match_status_changed(self):
        # update text status
        nb_win = self.round.nb_of_terminated_matches()
        n = len(self.round.matches)
        m = n-nb_win
        if nb_win > 1:
            t = f'{n} matches - {nb_win} terminés - {m} en cours'
        else:
            t = f'{n} matches - {nb_win} terminé - {m} en cours'
        self.label_center.setText(t)

        # update fields
        self.round.update_fields()
        for m in self.match_widgets:
            m.update_match_field()

        # update 'next round' button
        self.update_buttons_next_previous()
        
    @Slot()
    def slot_on_debug_mode_changed(self):
        self.button_random_scores.setEnabled(self.round.debug_mode)
        self.button_random_scores.setVisible(self.round.debug_mode)


    def setup_players_list(self):
        if self.round.terminated:
            players = self.round.selected_players
        else:
            players = self.round.tournament.players
        f = f'Options du tour n°{self.round.number}'
        self.label_options.setText(f)
        # setup model
        self.model = RoundPlayersTableModel(players)
        self.table_widget.setModel(self.model)
        self.table_widget.setAlternatingRowColors(True)
        if not self.round.terminated:
            self.model.dataChanged.connect(self.slot_on_players_change)
        else:
            self.table_widget.setEnabled(False)
            self.spin_win_point_value.setEnabled(False)
            self.spin_max_point_value.setEnabled(False)
            self.spin_fields.setEnabled(False)

        # filter
        self.filter_proxy_model = QSortFilterProxyModel()
        self.filter_proxy_model.setSourceModel(self.model)
        self.filter_proxy_model.setFilterKeyColumn(3)
        self.filter_proxy_model.setSortLocaleAware(True)
        self.filter_proxy_model.setSortCaseSensitivity(Qt.CaseInsensitive)
        self.table_widget.setModel(self.filter_proxy_model)
        self.table_widget.setSortingEnabled(True)
        self.edit_filter.textChanged.connect(self.filter_proxy_model.setFilterRegExp)
        self.edit_filter.setClearButtonEnabled(True)

        # UI
        self.table_widget.setColumnHidden(3, True)
        class AlignDelegate(QtWidgets.QStyledItemDelegate):
            def initStyleOption(self, option, index):
                super(AlignDelegate, self).initStyleOption(option, index)
                option.displayAlignment = Qt.AlignCenter
        delegate = AlignDelegate(self.table_widget)
        self.table_widget.setItemDelegateForColumn(2, delegate)
        self.table_widget.setSizeAdjustPolicy(QtWidgets.QAbstractScrollArea.AdjustToContents)
        header = self.table_widget.horizontalHeader()
        header.setSectionResizeMode(0, QtWidgets.QHeaderView.ResizeToContents)
        header.setSectionResizeMode(1, QtWidgets.QHeaderView.ResizeToContents)
        header.setSectionResizeMode(2, QtWidgets.QHeaderView.ResizeToContents)

        # init
        self.slot_on_players_change()

    def slot_on_players_change(self):
        n = len(self.round.players)
        m = 0
        for p in self.round.players:
            if p.selected:
                m = m+1
        f = f'Participants : {m}/{n}'
        self.label_players.setText(f)
        self.label_players_2.setText(f)

    @Slot()
    def slot_on_next_round(self):
        self.round.setTerminated(True)
        if self.round.is_last_round():
            self.parent.slot_on_next_round()
        else:
            self.parent.set_tab_round(self.round.number+1)
        self.setup_players_list()

    @Slot()
    def slot_on_previous_round(self):
        idx = self.round.tournament.rounds.index(self.round)
        if idx>0:
            self.parent.set_tab_round(idx)

    @Slot()
    def slot_on_round_termination_changed(self):
        f = True
        if self.round.terminated:
            f = False
        self.button_random_scores.setEnabled(f)
        self.button_random.setEnabled(f)
        self.button_swiss.setEnabled(f)
        t = self.round.tournament
        self.update_buttons_next_previous()
        self.button_erase_score.setEnabled(f)

    def update_buttons_next_previous(self):
        if self.round.number == 1:
            self.button_previous_round.setEnabled(False)
        else:
            self.button_previous_round.setEnabled(True)
        if self.round.terminated:
            self.button_next_round.setText('Tour suivant')
            self.button_next_round.setEnabled(True)
            return
        nb_win = self.round.nb_of_terminated_matches()
        n = len(self.round.matches)
        if nb_win == n and n != 0:
            self.button_next_round.setText('Nouveau tour')
            self.button_next_round.setEnabled(True)
        else:
            self.button_next_round.setEnabled(False)

    def slot_on_round_start_changed(self):
        v = not self.round.started
        self.button_random.setEnabled(v)
        self.button_swiss.setEnabled(v)

    def slot_on_erase_scores(self):
        if self.round.terminated:
            return
        if self.round.started == False:
            return
        box = QMessageBox()
        box.setStandardButtons(QMessageBox.Yes | QMessageBox.Discard)
        yes = box.button(QMessageBox.Yes)
        yes.setText('Oui, effacez tout.')
        discard = box.button(QMessageBox.Discard)
        discard.setText('Heu ... non, je me suis trompé !')
        box.setText('Attention ! Tous les résultats actuels seront supprimés. \n Voulez-vous continuer ?')
        box.setWindowTitle('Générer les matchs')
        ret = box.exec_()
        if ret == QMessageBox.Discard:
            return
        self.round.reset_all_scores()
        for w in self.match_widgets:
            w.set_match(w.match)