
from PySide2 import QtWidgets
from PySide2.QtCore import Slot, Qt, QMimeData, QPoint
from PySide2.QtGui import QDrag
from .ui_PlayerWidget import Ui_PlayerWidget

class WaitingPlayerWidget(QtWidgets.QWidget, Ui_PlayerWidget):

    def __init__(self, parent, player, round):
        '''
        Constructor
        '''
        super().__init__(parent)
        self.setupUi(self)
        self.player = player
        self.round = round

        # prepare drag & drop
        self.setAcceptDrops(True)
        self.setCursor(Qt.OpenHandCursor)

        # style
        self.css_normal = ""
        self.css_drag = "color: blue; font-weight: bold;"

        # player name
        self.slot_on_player_name_change()
        self.player.player_name_changed.connect(self.slot_on_player_name_change)

    def mousePressEvent(self, event):
        if event.button() != Qt.LeftButton:
            return
        self.setStyleSheet(self.css_drag)
        self.p = self.grab()
        self.drag = QDrag(self)
        mimeData = QMimeData()
        f = f'{self.player.id} ; waiting'
        mimeData.setText(f)
        self.drag.setMimeData(mimeData)
        self.drag.setPixmap(self.p)
        pos = QPoint()
        pos.setY(-15)
        pos.setX(-25)
        self.drag.setHotSpot(pos)

    def mouseMoveEvent(self, event):
        self.drag.exec_()
        self.setCursor(Qt.OpenHandCursor)
        self.setStyleSheet(self.css_normal)

    def mouseReleaseEvent(self, event):
        self.setCursor(Qt.OpenHandCursor)
        self.setStyleSheet(self.css_normal)

    def dragEnterEvent(self, event):
        id = event.mimeData().text()
        ids = id.split(' ; ')
        id = ids[0]
        if str(self.player.id) != id and ids[1] != 'waiting':
            self.setStyleSheet(self.css_drag)
            event.accept()

    def dragLeaveEvent(self, event):
        self.setStyleSheet(self.css_normal)

    def dropEvent(self, event):
        m = event.mimeData().text()
        ids = m.split(' ; ')
        if ids[1] == 'waiting':
            return
        r = self.round
        m = r.get_match_by_id(int(ids[1]))
        p = r.get_player_by_id(int(ids[0]))
        m.swap_player_waiting(p, self.player)
        self.setStyleSheet(self.css_normal)

    @Slot()
    def slot_on_player_name_change(self):
        try:
            self.player.player_name_changed.disconnect(self.slot_on_player_name_change)
        except:
            pass
        #self.player = self.team.player(self.player_nb)
        self.label.setText(str(self.player))
        self.player.player_name_changed.connect(self.slot_on_player_name_change)
        self.setStyleSheet(self.css_normal)

    @Slot()
    def slot_on_round_termination_changed(self):
        f = self.match.round.terminated
        self.setAcceptDrops(not f)

