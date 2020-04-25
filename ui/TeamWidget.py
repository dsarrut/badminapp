
from PySide2 import QtWidgets
from .ui_TeamWidget import Ui_TeamWidget
from .PlayerWidget import PlayerWidget

class TeamWidget(QtWidgets.QWidget, Ui_TeamWidget):

    def __init__(self, parent=None, team=None):
        '''
        Constructor
        '''
        super().__init__(parent)
        self.setupUi(self)
        self.setAcceptDrops(True)

        self.set_team(team)

    def set_team(self, team):
        self.team = team
        if team == None:
            return
        self.label_player1.setText('')
        self.label_player2.setText('')
        self.p1 = PlayerWidget(self, self.team, 1)
        self.p2 = PlayerWidget(self, self.team, 2)
        self.layout().replaceWidget(self.label_player1, self.p1)
        self.layout().replaceWidget(self.label_player2, self.p2)
        self.label_player1 = self.p1
        self.label_player2 = self.p2