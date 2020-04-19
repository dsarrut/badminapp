import sys
from PySide2 import QtCore, QtGui, QtWidgets
from PySide2.QtCore import Qt, Signal
from core import Player
from core.Player import random_word

class PlayersTableModel(QtCore.QAbstractTableModel):

    players_changed = Signal()

    def __init__(self, players):
        super(PlayersTableModel, self).__init__()
        self._players = players
        self.headers=[]
        self.headers.append('Nom')
        self.headers.append('Prénom')
        #self.headers.append('Classement')
        self.headers.append('Matchs joués')
        self.headers.append('Matchs gagnés')
        self.headers.append('Diff sets')
        self.headers.append('Diff points')
        self.headers.append('name')
        self.headers.append('id')
        self.index_name = self.headers.index('name')
        self.index_id = self.headers.index('id')
        self.index_played_matches = 2
        self.index_win_matches = 3
        self.index_set_diffs = 4
        self.index_points = 5

    def data(self, index, role):
        if role == Qt.DisplayRole:
            # See below for the nested-list data structure.
            # .row() indexes into the outer list,
            # .column() indexes into the sub-list
            p = self._players[index.row()]
            #print(index.row(), p, p.stats)
            c = index.column()
            if c == 0:
                return p.first_name
            if c == 1:
                return p.last_name
            if c == self.index_id:
                return p.id
            if c == self.index_name:
                return str(p).lower()
            if c == self.index_played_matches:
                return p.stats.match_count
            if c == self.index_win_matches:
                return p.stats.match_win_count
            if c == self.index_set_diffs:
                n = p.stats.set_diff
                if n>0:
                    return f'+{n}'
                return n
            if c == self.index_points:
                n = p.stats.points_diff
                if n>0:
                    return f'+{n}'
                return n
            return str(666)


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
        first = random_word()
        sec = random_word()
        p = Player(first, sec)
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