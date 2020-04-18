from random import randint
from PySide2.QtCore import Signal, QObject

class Set(QObject):

    set_status_changed = Signal()

    def __init__(self, match, num_set):
        QObject.__init__(self)
        self._score1 = 0
        self._score2 = 0
        self._status = 0 # -1 invalid, 0 in progress, 1 or 2 for winner
        self._num_set = num_set
        self._match = match
        self._point_current_max = 21

    def __str__(self):
        return f'{self._score1}/{self._score2}'

    @property
    def match(self):
        return self._match

    @property
    def round(self):
        return self.match.round

    @property
    def status(self):
        return self._status

    @property
    def is_valid(self):
        return self._status != -1

    @property
    def score1(self):
        return self._score1

    @property
    def score2(self):
        return self._score2

    @property
    def max_point_value(self):
        return self.match.round.max_point_value

    @property
    def win_point_value(self):
        return self.match.round.win_point_value

    def max(self, i):
        if i == 1:
            return self._point_current_max
        if i == 2:
            return self._point_current_max

    def update(self):
        # internal : max point, win point
        m = self.win_point_value-2
        if self.score1 > m and self.score2 > m:
            self._point_current_max = min(self.score1, self.score2)+2
        else:
            self._point_current_max = self.win_point_value
        # status
        old_status = self._status
        if self.score1 > self._point_current_max:
            self._status = -1
        elif self.score2 > self._point_current_max:
            self._status = -1
        else:
            self._status = self.compute_winner()
        if old_status != self._status:
            self.set_status_changed.emit()
        #else:
        #    # update players stats (will be also call if set_status_changed)
        #    self.match.update_stats_from_set(self._num_set)
        #    # FIXME here update all players stats ?
        #    self.match.update_players_stats()
        self.match.update_stats_from_match()

    @score1.setter
    def score1(self, value):
        if value == self._score1:
            return
        self._score1 = value
        self.update()

    @score2.setter
    def score2(self, value):
        if value == self._score2:
            return
        self._score2 = value
        self.update()

    def set_score(self, i, value):
        if i == 1:
            self.score1 = value
            return
        if i == 2:
            self.score2 = value
            return
        raise Exception(f'Set.set_score must be 1 or 2 while it is {i}')

    def score(self, i):
        if i == 1:
            return self.score1
        if i == 2:
            return self.score2
        raise Exception(f'Set.score must be 1 or 2 while it is {i}')


    def compute_winner(self):
        #if not self.is_valid:
        #    return 0
        if self.score1 == self.max_point_value:
            if self.score2 != self.max_point_value:
                return 1
        if self.score2 == self.max_point_value:
            if self.score1 != self.max_point_value:
                return 2
        if self.score1 >= self.win_point_value:
            if self.score2 <= self.score1 - 2:
                return 1
        if self.score2 >= self.win_point_value:
            if self.score1 <= self.score2-2:
                return 2
        return 0

    def random_scores(self):
        win = randint(1, 2)
        w = self.win_point_value
        if win == 1:
            self.score1 = w
            self.score2 = randint(0,w-2)
        if win == 2:
            self.score2 = w
            self.score1 = randint(0,w-2)

