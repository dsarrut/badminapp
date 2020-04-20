
from PySide2 import QtWidgets
from .ui_MainWindow import Ui_MainWindow
from PySide2.QtCore import Slot, QCoreApplication
from PySide2.QtWidgets import QApplication, QGridLayout, QWidget
from ui import RoundWidget
from ui import PlayersListWidget
from core import Tournament

class MainWindow(QtWidgets.QMainWindow, Ui_MainWindow):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.setupUi(self)

        self.tournament = Tournament()
        self.action_exit.triggered.connect(self.exit_app)
        self.action_debug_mode.triggered.connect(self.debug_mode)
        self.action_save.triggered.connect(self.save_players)
        self.action_load.triggered.connect(self.load_players)

        # install the player list widget
        pl = self.tournament.players
        self.players_list_widget = PlayersListWidget.PlayersListWidget(self, pl)
        self.tab_player.layout().addWidget(self.players_list_widget)
        self.tab_player.setAutoFillBackground(True)

    def set_tournament(self, tournament):
        # FIXME: check if already exist ?
        self.tournament = tournament
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
        
    @Slot()
    def exit_app(self):
        QApplication.quit()

    @Slot()
    def debug_mode(self, checked):
        for r in self.tournament.rounds:
            r.set_debug_mode(checked)

    def save_players(self):
        print('save')

    def load_players(self):
        print('load')

