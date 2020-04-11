
from PySide2 import QtWidgets, QtGui
from PySide2.QtCore import Slot, Signal, QSize, Qt, QModelIndex
from PySide2.QtGui import QPixmap, QPalette, QColor, QFont, QBrush
from PySide2.QtWidgets import QAction, QAbstractItemView, QTableWidgetSelectionRange
from .ui_PlayersListWidget import Ui_PlayersListWidget


class PlayersListWidget(QtWidgets.QWidget, Ui_PlayersListWidget):

    def __init__(self, parent=None, players=None):
        '''
        Constructor
        '''
        super().__init__(parent)
        self.setupUi(self)
        self.set_players(players)

        # set connections
        tw = self.table_widget
        tw.itemChanged.connect(self.slot_on_item_changed)
        tw.itemSelectionChanged.connect(self.slot_on_cell_activated)
        self.button_del.clicked.connect(self.slot_on_player_del)


    def set_players(self, players):
        self.players = players
        tw = self.table_widget
        tw.setRowCount(len(players))

        # install players
        i=0
        for p in players:
            self.add_player(i, p)
            i = i+1

        # some ui
        self.button_del.setEnabled(False)


    def add_player(self, row, player):
        tw = self.table_widget
        tw.setItem(row, 0, QtWidgets.QTableWidgetItem(player.get_name(0)))
        tw.setItem(row, 1, QtWidgets.QTableWidgetItem(player.get_name(1)))

        # set other columns not editable but with color black
        n = tw.columnCount()
        self.index_column = n-1
        for c in range(2,n-1):
            item = QtWidgets.QTableWidgetItem('') #FIXME real value
            tw.setItem(row, c, item)
            item.setFlags(Qt.ItemIsEditable)
            item.setForeground(QBrush(QColor('black')))

        # last one is id but is hidden, this it the index
        item = QtWidgets.QTableWidgetItem(str(player.id))
        tw.setItem(row, n-1, item)
        #tw.setColumnHidden(n-1, True) #FIXME


    @Slot()
    def slot_on_item_changed(self, item):
        col = item.column()
        if col > 1:
            return
        row = item.row()
        player = self.players[row]
        if player.get_name(col) != item.text():
            player.set_name(col, item.text())


    def get_current_selected_player(self):
        items = self.table_widget.selectedItems()
        if len(items) == 0:
            return None
        row = items[0].row()
        id = int(self.table_widget.item(row, self.index_column).text())
        for p in self.players:
            if p.id == id:
                break
        return p


    def slot_on_cell_activated(self):
        player = self.get_current_selected_player()
        if player:
            self.button_del.setText("Supprimer "+str(player))
            self.button_del.setEnabled(True)
        else:
            self.button_del.setText("Supprimer")
            self.button_del.setEnabled(False)

    def slot_on_player_del(self):
        player = self.get_current_selected_player()
        row = self.table_widget.selectedItems()[0].row()
        tw = self.table_widget
        tw.blockSignals(True)
        p = self.players.index(player)
        self.players.remove(player)
        tw.rowsAboutToBeRemoved(QModelIndex(), row, row)
        tw.removeRow(row)
        tw.blockSignals(False)
        tw.clearSelection()
        #self.slot_on_cell_activated() # no because not seen selected
