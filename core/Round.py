from .Match import Match
import random
from PySide2.QtCore import Signal, QObject
from operator import itemgetter, attrgetter
from random import randint

class Round(QObject):

    debug_mode_changed = Signal()
    round_termination_changed = Signal()
    round_started_changed = Signal()

    def __init__(self, tournament):
        QObject.__init__(self)
        self.tournament = tournament
        self.number = len(tournament.rounds)+1
        self.matches = []
        self.fields_number = 5
        self.fields = {}
        self.waiting_players = []
        self._max_point_value = 29
        self._win_point_value = 21
        self._debug_mode = False
        self.match_generation_mode = 'random'
        self.terminated = False
        self.started = False

    def __str__(self):
        s = f'Round {self.number}'
        return s

    @property
    def max_point_value(self):
        return self._max_point_value

    @property
    def win_point_value(self):
        return self._win_point_value

    @property
    def debug_mode(self):
        return self._debug_mode

    def set_round_has_started(self, v):
        if self.started == v:
            return
        self.started = v
        print('emit round start',v)
        self.round_started_changed.emit()

    def update_started(self):
        for m in self.matches:
            if m.started:
                self.set_round_has_started(True)
                return
        self.set_round_has_started(False)

    def set_debug_mode(self, value):
        self._debug_mode = value
        self.debug_mode_changed.emit()

    def set_players_list(self, players):
        self.players = players

    def create_matches(self):
        m = self.match_generation_mode
        self.selected_players = [p for p in self.players if p.selected]
        if m == 'swiss':
            self.create_matches_swiss()
        else:
            self.create_matches_random()

    def create_matches_swiss(self):
        pl = sorted(self.selected_players,
                    key=attrgetter('stats.match_win_count',
                                   'stats.set_diff',
                                   'stats.points_diff'),
                    reverse=True)
        # put waiting players at the end
        w = len(self.selected_players)%4
        wplayers = []
        for i in range(w):
            wplayers.append(randint(0,len(self.selected_players)-1))
        for p in wplayers:
            pl.append(pl.pop(p))
        self.create_matches_from_list(pl)

    def create_matches_random(self):
        # complete random
        pl = random.sample(self.selected_players, len(self.selected_players))
        self.create_matches_from_list(pl)

    def create_matches_from_list(self, pl):
        # create matches
        i=0
        n = len(pl)
        f = 1
        self.matches = []
        self.waiting_players = []
        while i<=n-4:
            # for swiss -> do not follow initial order
            # for rnd -> never mind
            p1 = pl[i]
            p2 = pl[i+3]
            p3 = pl[i+1]
            p4 = pl[i+2]
            #t1 = Team(p1, p2)
            #t2 = Team(p3, p4)
            #m = Match(self, t1, t2, f)
            m = Match(self, p1, p2, p3, p4, f)
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

    #def create_next_round(self):
    #    self.setTerminated(True)
    #    r = self.tournament.new_round()
    #    return r

    def nb_of_terminated_matches(self):
        nb_win = 0
        for m in self.matches:
            if m.status != 0 and m.status != -1:
                nb_win = nb_win + 1
        return nb_win

    def update_fields(self):
        free_fields = []
        #print('FIXME bug here in update_fields')
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
            if m.field == field and (m.status == 0 or m.status == -1):
                other_match = m
                continue
        match.field = field
        match.match_field_changed.emit()
        if other_match == None:
           return
        other_match.field = current_field
        other_match.match_field_changed.emit()


    def set_max_point_value(self, s):
        self._max_point_value = s

    def set_win_point_value(self, s):
        self._win_point_value = s

    def get_match_by_id(self, id):
        for m in self.matches:
            if id == m.id:
                return m
        return None

    def get_player_by_id(self, id):
        for p in self.players:
            if id == p.id:
                return p
        return None

    def setTerminated(self, v):
        self.terminated = v
        self.round_termination_changed.emit()

    def is_last_round(self):
        n = self.number
        if n == len(self.tournament.rounds):
            return True
        return False

    def remove_match_for_players(self, match):
        match.team1.remove_match(match)
        match.team2.remove_match(match)

    def reset_all_scores(self):
        for m in self.matches:
            m.reset_score()