
from PySide2 import QtWidgets
from PySide2.QtCore import Slot, Qt, QMimeData
from PySide2.QtGui import QDrag, QPixmap
from .ui_TeamWidget import Ui_TeamWidget
from .PlayerWidget import PlayerWidget

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
        #self.label_player1.dragMoveEvent.connect(self.slot_on_drag_move)
        #self.p = QPixmap(u":/icons/128x128/emotes/face-wink-4.png")
        #self.p = self.p.scaled(32,32)

        self.setAcceptDrops(True)
        #self.label_player1.setAcceptDrops(True)
        #self.label_player2.setAcceptDrops(True)

        #self.setAcceptDrops(True)
        #self.setDragDropMode(QtWidgets.QAbstractItemView.DropOnly)
        #self.setDefaultDropAction(QtCore.Qt.CopyAction)

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
        #self.label_player1.setAcceptDrops(True)
        #self.label_player2.setAcceptDrops(True)
        #self.label_player2.setPixmap(self.p)
        #self.team.player1.player_name_changed.connect(self.slot_on_player_name_change)
        #self.team.player2.player_name_changed.connect(self.slot_on_player_name_change)

    #@Slot()
    #def slot_on_player_name_change(self):
        #self.label_player1.setText(str(self.team.player1))
        #self.label_player2.setText(str(self.team.player2)

