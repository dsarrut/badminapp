from .Set import Set
from .helpers import *
from .Team import Team
from .PlayerStats import PlayerStats
from PySide2.QtCore import Slot, Signal, QObject

class Match(QObject):

    match_status_changed = Signal()
    match_field_changed = Signal()

    _last_id = 0

    def __init__(self, round, team1, team2, field):
        QObject.__init__(self)
        self._round = round
        self.team1 = team1
        self.team2 = team2
        self.field = field
        self.set1 = Set(self, 1)
        self.set2 = Set(self, 2)
        self.set3 = Set(self, 3)
        self.team1.add_match(self)
        self.team2.add_match(self)
        self.set1.set_status_changed.connect(self.on_set_status_changed)
        self.set2.set_status_changed.connect(self.on_set_status_changed)
        self.set3.set_status_changed.connect(self.on_set_status_changed)
        self._status = 0 # -1 invalid, 0 in progress, 1 or 2 for winner
        self.id = Match._last_id+1
        Match._last_id = self.id

    def __str__(self):
        s = f'match {self.team1} vs {self.team2} : {self.set1} {self.set2} {self.set3}'
        return s

    @property
    def round(self):
        return self._round

    @property
    def max_point_value(self):
        return self.round.max_point_value

    @property
    def win_point_value(self):
        return self.round.win_point_value

    @property
    def status(self):
        return self._status

    def team(self, i):
        if i == 1:
            return self.team1
        if i == 2:
            return self.team2
        raise_except(f'Match.team must be 1 or 2 while it is {i}')

    def is_valid(self):
        if not self.set1.is_valid:
            return False
        if not self.set2.is_valid:
            return False
        if not self.set3.is_valid:
            return False
        return True

    def set(self, i):
        if i == 1:
            return self.set1
        if i == 2:
            return self.set2
        if i == 3:
            return self.set3
        raise_except(f'Match.set must be 1, 2 or 3 while it is {i}')

    @Slot()
    def on_set_status_changed(self):
        old_status = self._status
        if self.set1.status == -1 or self.set2.status == -1 or self.set3.status == -1:
            self._status = -1
        else:
            w = self.compute_winner()
            self._status = w
        if old_status != self._status:
            # update stats relatively to match status
            self.update_stats_from_match()
            # emit signal
            self.match_status_changed.emit()


    def compute_winner(self):
        ws1 = self.set1.compute_winner()
        if ws1 == 0:
            return 0
        ws2 = self.set2.compute_winner()
        if ws2 == 0:
            return 0
        if ws1 == ws2:
            self.two_sets_only = True
            return ws1
        self.two_sets_only = False
        ws3 = self.set3.compute_winner()
        return ws3


    def random_scores(self):
        self.set1.random_scores()
        self.set2.random_scores()
        ws1 = self.set1.compute_winner()
        ws2 = self.set2.compute_winner()
        if ws1 != ws2:
            self.set3.random_scores()
        else:
            self.set3.score1 = 0
            self.set3.score2 = 0

    def swap_field(self, field):
        self.round.swap_field(self, field)


    def get_player_team(self, player):
        if player == self.team1.player1 or player == self.team1.player2:
            return 1
        return 2

    def get_player_match_stats(self, player):
        t = self.get_player_team(player)
        return self.team(t).stats


    def update_stats_from_match(self):
        print('match update_stats from match')
        self.team1.update_match_stats(self, 1)
        self.team2.update_match_stats(self, 2)
        #self.update_stats_from_set(1)
        #self.update_stats_from_set(2)
        #self.update_stats_from_set(3)
        self.update_players_stats()

    def update_stats_from_set(self, num_set):
        print('match update_stats from set', num_set)
        #self.team1.update_set_stats(1, self.set(num_set))
        #self.team2.update_set_stats(2, self.set(num_set))
        #self.update_players_stats()

    def update_players_stats(self):
        self.team1.update_players_stats()
        self.team2.update_players_stats()
