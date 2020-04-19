import sys
from PySide2 import QtCore, QtGui, QtWidgets
from PySide2.QtCore import Qt, Signal
from core import Player

class PlayersTableSortFilterProxyModel(QtCore.QSortFilterProxyModel):

    def __init__(self):
        super(PlayersTableSortFilterProxyModel, self).__init__()

    def lessThan(self, source_left, source_right):
        model = source_left.model()
        if model.index_points == source_left.column():
            pl = model._players[source_left.row()].stats.points_diff
            pr = model._players[source_right.row()].stats.points_diff
            if pl<=pr:
                return True
            return False

        if model.index_win_matches == source_left.column():
            pl = model._players[source_left.row()]
            pr = model._players[source_right.row()]
            if pl.stats.match_win_count < pr.stats.match_win_count:
                return True
            if pl.stats.match_win_count > pr.stats.match_win_count:
                return False
            if pl.stats.set_diff < pr.stats.set_diff:
                return True
            if pl.stats.set_diff > pr.stats.set_diff:
                return False
            if pl.stats.points_diff < pr.stats.points_diff:
                return True
            if pl.stats.points_diff > pr.stats.points_diff:
                return False
            if pl.stats.match_count < pr.stats.match_count:
                return True
            if pl.stats.match_count > pr.stats.match_count:
                return False
            # Strict equality here !!
            return True
        # default
        return super(PlayersTableSortFilterProxyModel, self).lessThan(source_left,source_right)
