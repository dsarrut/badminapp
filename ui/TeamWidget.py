
from PySide2 import QtWidgets
from PySide2.QtCore import Slot, Signal, QSize
from PySide2.QtGui import QPixmap, QPalette, QColor, QFont
from PySide2.QtWidgets import QAction
from .ui_TeamWidget import Ui_TeamWidget
import platform

class TeamWidget(QtWidgets.QWidget, Ui_TeamWidget):

    def __init__(self, parent=None, team=None):
        '''
        Constructor
        '''
        super().__init__(parent)
        self.setupUi(self)

        #pal = self.label_separator.palette()
        #pal.setColor(QPalette.Base, QColor("red"))
        #self.label_separator.setPalette(pal)
        self.set_team(team)

    def set_team(self, team):
        self.team = team
        if team == None:
            return
        self.label_player1.setText(str(self.team.player1))
        self.label_player2.setText(str(self.team.player2))
        self.team.player1.player_name_changed.connect(self.slot_on_player_name_change)
        self.team.player2.player_name_changed.connect(self.slot_on_player_name_change)

    @Slot()
    def slot_on_player_name_change(self):
        self.label_player1.setText(str(self.team.player1))
        self.label_player2.setText(str(self.team.player2))


