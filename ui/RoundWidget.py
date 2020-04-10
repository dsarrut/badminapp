
from PySide2 import QtWidgets
from PySide2.QtCore import Slot, QCoreApplication
from .ui_RoundWidget import Ui_RoundWidget
from ui import MatchWidget
from ui.WaitingPlayersWidget import WaitingPlayersWidget

class RoundWidget(QtWidgets.QWidget, Ui_RoundWidget):

    def __init__(self, parent=None):
        super().__init__(parent)
        self.setupUi(self)

        self.fields = {}
        # signal button
        self.button_random.clicked.connect(self.slot_on_random)
        self.button_next_round.clicked.connect(parent.slot_on_next_round)
        self.button_random_scores.clicked.connect(self.slot_on_random_scores)

    def set_round(self, round):
        self.round = round
        print(round.tournament)
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
            wpw.set_waiting_players(self.round.waiting_players)
            self.main_layout.addWidget(wpw, r, c)

        # update status
        self.slot_on_match_status_changed()

        # update options
        self.spin_fields.setValue(self.round.fields_number)
        self.spin_max_point_value.setValue(self.round.max_point_value)
        self.spin_win_point_value.setValue(self.round.win_point_value)

        # set current tab
        self.toolBox.setCurrentIndex(0)

    @Slot()
    def slot_on_random(self):
        print('FIXME read and set round properties here')
        self.round.fields_number = self.spin_fields.value()
        self.round.set_max_point_value(self.spin_max_point_value.value())
        self.round.set_win_point_value(self.spin_win_point_value.value())
        self.round.create_matches()
        self.set_round(self.round)


    @Slot()
    def slot_on_random_scores(self):
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
        if nb_win == n:
            self.button_next_round.setEnabled(True)
        else:
            self.button_next_round.setEnabled(False)

        
