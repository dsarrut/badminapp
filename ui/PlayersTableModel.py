import sys
from PySide2 import QtCore, QtGui, QtWidgets
from PySide2.QtCore import Qt, Signal
from core import Player

class PlayersTableModel(QtCore.QAbstractTableModel):

    players_changed = Signal()

    def __init__(self, players):
        super(PlayersTableModel, self).__init__()
        self._players = players
        self.headers=[]
        self.headers.append('Nom')
        self.headers.append('Prénom')
        self.headers.append('Classement')
        self.headers.append('Matchs joués')
        self.headers.append('Matchs gagnés')
        self.headers.append('Set perdus')
        self.headers.append('Points')
        self.headers.append('name')
        self.headers.append('id')
        self.index_name = self.headers.index('name')
        self.index_id = self.headers.index('id')

    def data(self, index, role):
        if role == Qt.DisplayRole:
            # See below for the nested-list data structure.
            # .row() indexes into the outer list,
            # .column() indexes into the sub-list
            p = self._players[index.row()]
            #print(index.row(), p)
            c = index.column()
            if c == 0:
                return p.first_name
            if c == 1:
                return p.last_name
            if c == self.index_id:
                return p.id
            if c == self.index_name:
                return str(p).lower()
            return '12'


    def rowCount(self, index):
        # The length of the outer list.
        return len(self._players)


    def columnCount(self, index):
        # The following takes the first sub-list, and returns
        # the length (only works if all rows are an equal length)
        return len(self.headers)


    def flags(self, index):
        #print('flags', index)
        original_flags = super(PlayersTableModel, self).flags(index)
        if index.column()>1:
            return original_flags
        return original_flags | QtCore.Qt.ItemIsEditable | QtCore.Qt.ItemIsEnabled | QtCore.Qt.ItemIsSelectable


    def setData(self, index, value, role):
        if not index.isValid():
            return False
        if role != QtCore.Qt.EditRole:
            return False
        row = index.row()
        if row < 0 or row >= len(self._players):
            return False
        column = index.column()
        if column < 0 or column >= 2:
            return False
        if column == 0:
            self._players[row].set_name(0, value)
            self.dataChanged.emit(index, index)
            return True
        if column == 1:
            self._players[row].set_name(1, value)
            self.dataChanged.emit(index, index)
            return True
        return False

    def headerData(self, section, orientation, role):
        if orientation == QtCore.Qt.Horizontal and role == QtCore.Qt.DisplayRole:
            return self.headers[section]
        return None

    def insertRow(self, row, parent=QtCore.QModelIndex()):
        self.beginInsertRows(parent, row, row)
        p = Player('nom', 'prénom')
        self._players.insert(row, p)
        self.endInsertRows()
        self.players_changed.emit()
        return True

    def removeRow(self, row, player, parent=QtCore.QModelIndex()):
        self.beginRemoveRows(parent, row, row)
        if player in self._players:
            self._players.remove(player)
        self.endRemoveRows()
        self.players_changed.emit()
        return True