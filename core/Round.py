from .Match import Match
from .Team import Team
import random

class Round:

    def __init__(self, tournament):
        self.tournament = tournament
        self.number = len(tournament.rounds)+1
        self.matches = []
        self.fields_number = 5
        self.fields = {}
        self.waiting_players = []
        self._max_point_value = 29
        self._win_point_value = 21

    def __str__(self):
        s = f'Round {self.number}'
        return s

    @property
    def max_point_value(self):
        return self._max_point_value

    @property
    def win_point_value(self):
        return self._win_point_value

    def set_players_list(self, players):
        self.players = players

    def create_matches(self):
        print('FIXME round create matches do it with random')
        pl = random.sample(self.players, len(self.players))
        # no field number for the moment
        # create matches
        i=0
        n = len(pl)
        f = 1
        self.matches = []
        self.waiting_players = []
        while i<n-4:
            p1 = pl[i]
            p2 = pl[i+1]
            p3 = pl[i+2]
            p4 = pl[i+3]
            t1 = Team(p1, p2)
            t2 = Team(p3, p4)
            m = Match(self, t1, t2, f)
            self.matches.append(m)
            i = i+4
            if f == 0 or f >= self.fields_number:
                f = 0
            else:
                f = f + 1
        while i<n:
            self.waiting_players.append(pl[i])
            i = i+1

    def random_scores(self):
        for m in self.matches:
            m.random_scores()

    def create_next_round(self):
        r = self.tournament.new_round()
        return r

    def nb_of_terminated_matches(self):
        nb_win = 0
        for m in self.matches:
            if m.status != 0 and m.status != -1:
                nb_win = nb_win + 1
        return nb_win

    def update_fields(self):
        free_fields = []
        print('FIXME bug here in update_fields')
        for m in self.matches:
            if m.status == 1 or m.status == 2:
                free_fields.append(m.field)
        for m in self.matches:
            if len(free_fields) == 0:
                continue
            if m.field == 0:
                m.field = free_fields.pop()

    def swap_field(self, match, field):
        '''
        Exchange the match field with the given field
        '''
        current_field = match.field
        other_match = None
        for m in self.matches:
            if m.field == field:
                other_match = m
                continue
        if other_match == None:
            print('Bug in swap_field ?')
            return
        other_match.field = current_field
        match.field = field
        match.match_field_changed.emit()
        other_match.match_field_changed.emit()

    def set_max_point_value(self, s):
        self._max_point_value = s

    def set_win_point_value(self, s):
        self._win_point_value = s