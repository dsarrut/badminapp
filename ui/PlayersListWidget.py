
from PySide2 import QtWidgets, QtGui
from PySide2.QtCore import Slot, Signal, QSize, Qt
from PySide2.QtGui import QPixmap, QPalette, QColor, QFont, QBrush
from PySide2.QtWidgets import QAction, QAbstractItemView
from .ui_PlayersListWidget import Ui_PlayersListWidget


class PlayersListWidget(QtWidgets.QWidget, Ui_PlayersListWidget):

    def __init__(self, parent=None, players=None):
        '''
        Constructor
        '''
        super().__init__(parent)
        self.setupUi(self)
        self.set_players(players)


    def set_players(self, players):
        self.players = players
        tw = self.table_widget
        tw.setRowCount(len(players))

        # install players
        i=0
        for p in players:
            self.add_player(i, p)
            i = i+1

        # set connection
        tw.itemChanged.connect(self.slot_on_item_changed)


    def add_player(self, row, player):
        tw = self.table_widget
        tw.setItem(row, 0, QtWidgets.QTableWidgetItem(player.get_name(0)))
        tw.setItem(row, 1, QtWidgets.QTableWidgetItem(player.get_name(1)))

        # set other columns not editable and with color black
        for c in range(2,tw.columnCount()):
            item = QtWidgets.QTableWidgetItem('') #FIXME real value
            tw.setItem(row, c, item)
            item.setFlags(Qt.ItemIsEditable)
            item.setForeground(QBrush(QColor('black')))


    @Slot()
    def slot_on_item_changed(self, item):
        col = item.column()
        if col > 1:
            return
        row = item.row()
        player = self.players[row]
        if player.get_name(col) != item.text():
            player.set_name(col, item.text())
