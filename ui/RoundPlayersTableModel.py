from PySide2 import QtCore
from PySide2.QtCore import Qt, Signal
from PySide2.QtGui import QBrush

class RoundPlayersTableModel(QtCore.QAbstractTableModel):

    players_changed = Signal()

    def __init__(self, players):
        super(RoundPlayersTableModel, self).__init__()
        self._players = players
        self.headers=[]
        self.headers.append('Nom')
        self.headers.append('Prénom')
        self.headers.append('Matchs joués')
        self.headers.append('name')
        self.index_name = self.headers.index('name')
        self.index_played_matches = 2


    def data(self, index, role):

        if role == Qt.DisplayRole:
            p = self._players[index.row()]
            c = index.column()
            if c == 0:
                return p.first_name
            if c == 1:
                return p.last_name
            if c == self.index_name:
                return str(p).lower()
            if c == self.index_played_matches:
                return p.stats.match_count

        if role == Qt.CheckStateRole:
            p = self._players[index.row()]
            c = index.column()
            if c == 0:
                if p.selected:
                    return QtCore.Qt.Checked
                return QtCore.Qt.Unchecked

        if role == Qt.ForegroundRole:
            p = self._players[index.row()]
            if p.selected:
                    return QBrush(Qt.black)
            return QBrush(Qt.lightGray)


    def rowCount(self, index):
        # The length of the outer list.
        return len(self._players)


    def columnCount(self, index):
        # The following takes the first sub-list, and returns
        # the length (only works if all rows are an equal length)
        return len(self.headers)


    def flags(self, index):
        original_flags = super(RoundPlayersTableModel, self).flags(index)
        if index.column() == 0:
            return Qt.ItemIsUserCheckable | Qt.ItemIsSelectable | Qt.ItemIsEnabled
        return original_flags

    def setData(self, index, value, role):
        if not index.isValid():
            return False
        if role != Qt.CheckStateRole:
            return False
        row = index.row()
        column = index.column()
        if column != 0:
            return False
        if value == QtCore.Qt.Checked:
            self._players[row].selected = True
        else:
            self._players[row].selected = False
        r = self.createIndex(row, 3)
        self.dataChanged.emit(index, r)
        return True


    def headerData(self, section, orientation, role):
        if orientation == QtCore.Qt.Horizontal and role == QtCore.Qt.DisplayRole:
            return self.headers[section]
        return None
