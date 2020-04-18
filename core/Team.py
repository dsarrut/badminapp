from .helpers import *
from .Player import Player
from .PlayerStats import PlayerStats

class Team:

    def __init__(self, player1, player2):
        # later will be simple/double
        if not player1:
            player1 = Player()
        if not player2:
            player2 = Player()
        self.player1 = player1
        self.player2 = player2
        self._stats = PlayerStats()

    def __str__(self):
        s = f'{self.player1}/{self.player2}'
        return s

    def set_player(self, i, player):
        if i == 1:
            self.player1 = player
        if i == 2:
            self.player2 = player
        raise_except(f'Team must be 1 or 2 while it is {i}')

    def add_match(self, match):
        self.player1.add_match(match)
        self.player2.add_match(match)

    @property
    def stats(self):
        return self._stats

    def update_match_stats(self, match, team):
        self._stats.reset()

        # check match status
        s = match.status
        if s == 0 or s == -1:
            return

        # if there is a winner
        self._stats.match_count = 1
        print("team winner ",match.team(s), self)
        if match.team(s) == self:
            self._stats.match_win_count = 1
        else:
            self._stats.match_win_count = 0

        # count nb of loose set
        self._stats.set_loose_count = 0

        # count nb points
        self._stats.points_diff = 0
        if team == 1:
            ot = 2
        else:
            ot = 1
        for i in range(1,4):
            print(i)
            s = match.set(i).status
            if s == 0 or s == -1:
                continue
            diff = match.set(i).score(team) - match.set(i).score(ot)
            self._stats.points_diff = self._stats.points_diff + diff
            if team != match.set(i).status:
                self._stats.set_loose_count = self._stats.set_loose_count + 1


    def update_set_stats(self, team, set):
        s = set.match.status
        if s == 0 or s == -1:
            self._stats.reset()
            return
        s = set.status
        if team == 1:
            ot = 2
        else:
            ot = 1
        points = set.score(team) - set.score(ot)
        self._stats.points_diff = self._stats.points_diff + points
        if s != team:
            self._stats.set_loose_count = self._stats.set_loose_count +1

    def update_players_stats(self):
        self.player1.update_stats() # FIXME update only one match !!
        self.player2.update_stats()