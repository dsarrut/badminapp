
from PySide2 import QtWidgets
from .ui_MainWindow import Ui_MainWindow
from PySide2.QtCore import Slot, QCoreApplication
from PySide2.QtGui import QIcon
from PySide2.QtWidgets import QApplication, QGridLayout, QWidget, QFileDialog, QMessageBox
from ui import RoundWidget
from ui import PlayersListWidget
from ui import FinalWidget
from core import Tournament
from core import Player
import json

class MainWindow(QtWidgets.QMainWindow, Ui_MainWindow):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.setupUi(self)

        self.setWindowIcon(QIcon(u":/icons/bad.jpg"))  # Set the window icon and add it
        self.setWindowTitle("Badminapp - Tournoi de badminton de type 'ronde Suisse' - BCVT 2020")

        self.filename = None
        self.tournament = Tournament()
        self.action_exit.triggered.connect(self.exit_app)
        self.action_debug_mode.triggered.connect(self.debug_mode)
        self.action_save.triggered.connect(self.save_players)
        self.action_save_as.triggered.connect(self.save_players_as)
        self.action_load.triggered.connect(self.load_players)

        # install the player list widget
        pl = self.tournament.players
        self.players_list_widget = PlayersListWidget.PlayersListWidget(self, pl)
        self.tab_player.layout().addWidget(self.players_list_widget)
        self.tab_player.setAutoFillBackground(True)

    def set_tournament(self, tournament):
        # FIXME: check if already exist ?
        self.tournament = tournament
        while self.tab.count() != 1:
            self.tab.removeTab(1)
        self.players_list_widget.set_players(tournament.players)

    def set_round(self, round):
        #self.rounds.append(round)
        rw = RoundWidget.RoundWidget(parent=self)
        rw.set_round(round)
        self.layout.addWidget(rw)

    def set_tab_round(self, round_nb):
        self.tab.setCurrentIndex(round_nb)

    @Slot()
    def slot_on_next_round(self):
        # new round
        t = self.tournament
        r = t.new_round()
        # new round widget
        rw = RoundWidget.RoundWidget(parent=self)
        rw.set_round(r)
        # new tab
        n = r.number
        s = QCoreApplication.translate("MainWindow", u"Tour n\u00b0"+str(n), None)
        tw = QWidget()
        self.tab.addTab(tw, "")
        self.tab.setTabText(self.tab.indexOf(tw), s)
        self.tab.setAutoFillBackground(True)
        tw.setAutoFillBackground(True)
        l = QGridLayout(tw)
        l.addWidget(rw)
        idx = self.tab.indexOf(tw)
        self.tab.setCurrentIndex(idx)
        rw.button_end_tournament.clicked.connect(self.end_tournament)
        
    @Slot()
    def exit_app(self):
        QApplication.quit()


    @Slot()
    def debug_mode(self, checked):
        for r in self.tournament.rounds:
            r.set_debug_mode(checked)


    def save_players(self):
        if self.filename == None:
            self.filename, _ = \
                QFileDialog.getSaveFileName(self, 'Sauvegarder les joueurs','','Joueurs (*.json)')
        if not self.filename:
            return
        self.save_players_to_file()

    def save_players_to_file(self):
        fs = open(self.filename, 'w')
        d = {}
        for p in self.tournament.players:
            d[p.id] = p.to_dict()
        json.dump(d, fs, sort_keys=True, indent=2)
        self.action_save.setText(f'Sauvegarder {self.filename}')

    def save_players_as(self):
        self.filename, _ = \
                QFileDialog.getSaveFileName(self, 'Sauvegarder les joueurs','','Joueurs (*.json)')
        if not self.filename:
            return
        self.save_players_to_file()

    def load_players(self):
        self.open_filename, _ = \
                QFileDialog.getOpenFileName(self, 'Charger des joueurs','','Joueurs (*.json)')

        box = QMessageBox()
        box.setStandardButtons(QMessageBox.Yes | QMessageBox.Discard)
        yes = box.button(QMessageBox.Yes)
        yes.setText('Oui, effacez tout.')
        discard = box.button(QMessageBox.Discard)
        discard.setText('Heu ... non, je me suis trompé !')
        box.setText('Attention ! Tous les résultats actuels seront supprimés. \n Voulez-vous continuer ?')
        box.setWindowTitle('Remplacer les joueurs')
        ret = box.exec_()
        if ret == QMessageBox.Discard:
            return

        fs = open(self.open_filename, 'r')
        dic = json.load(fs)
        t = Tournament()
        players = []
        for p in dic:
            player = Player()
            player.from_dict(dic[p])
            if player.id == -1:
                print('error player',dic[p])
                continue
            players.append(player)
        t.set_players(players)
        self.set_tournament(t)
        self.slot_on_next_round()
        self.tab.setCurrentIndex(0)


    def end_tournament(self):
        tw = QWidget()
        tw.setAutoFillBackground(True)
        self.tab.addTab(tw, "")
        s = "C'est terminé !"
        idx = self.tab.indexOf(tw)
        self.tab.setTabText(idx, s)
        l = QGridLayout(tw)
        fw = FinalWidget.FinalWidget(self, self.tournament, tw)
        l.addWidget(fw)
        self.tab.setAutoFillBackground(True)
        self.tab.setCurrentIndex(idx)

    def remove_final(self, w):
        idx = self.tab.indexOf(w)
        self.tab.removeTab(idx)