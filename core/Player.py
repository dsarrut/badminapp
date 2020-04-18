from random import randint
import io
from PySide2.QtCore import Slot, Signal, QObject
from .PlayerStats import PlayerStats

word_file = "qrc/nouns.txt"
WORDS = io.open("qrc/nouns.txt", mode="r", encoding="utf-8").read().splitlines()

def random_word():
    value = randint(0, len(WORDS))
    return WORDS[value].split(';')[0]

class Player(QObject):

    _last_id = 0
    player_name_changed = Signal()
    player_stats_changed = Signal()

    def __init__(self, first=None, last=None):
        QObject.__init__(self)
        if not first:
            first = random_word()
        if not last:
            last = random_word()
        self._first_name = first.capitalize()
        self._last_name = last.capitalize()
        self.id = Player._last_id+1
        Player._last_id = self.id
        self.matches = []
        self._stats = PlayerStats()
        #self.update_stats()

    def __str__(self):
        s = f'{self._first_name} {self._last_name}'
        return s

    @property
    def first_name(self):
        return self._first_name

    @property
    def last_name(self):
        return self._last_name

    def set_name(self,i,value):
        #print('player set name ', str(self), i, value)
        if i == 0:
            self._first_name = value
            self.player_name_changed.emit()
            #print('--> player set name ', str(self))
            return
        if i == 1:
            self._last_name = value
            self.player_name_changed.emit()
            #print('--> player set name ', str(self))
            return

    def get_name(self, i):
        if i == 0:
            return self._first_name
        if i == 1:
            return self._last_name

    def add_match(self, match):
        if match == None:
            return
        print('player add a match', self)
        self.matches.append(match)

    def update_match(self, match):
        print('FIXME ???')
        return
        exists = False
        if match in self.matches:
            exists = True
        if match.status == 0 or match.status == -1:
            if exists:
                self.matches.remove(match)
                self.update_stats()
            return
        if not exists:
            self.matches.append(match)
            self.update_stats()

    def update_stats(self):
        print('FIXME REMOVE')
        return
        self.win_matches = 0
        self.loose_sets = 0
        self.win_points = 0
        self.loose_points = 0
        for m in self.matches:
            t = m.get_player_team(self)
            # ot = other team
            if t ==1:
                ot = 2
            else:
                ot = 1
            w = m.status
            # the following should never happens
            if w == 0 or w == -1:
                print('Error player match stat', self, m)
                continue

            # always here
            self.win_points = self.win_points + m.set1.score(t)
            self.win_points = self.win_points + m.set2.score(t)
            self.loose_points = self.loose_points + m.set1.score(ot)
            self.loose_points = self.loose_points + m.set2.score(ot)
            if not m.two_sets_only:
                self.win_points = self.win_points + m.set3.score(t)
                self.loose_points = self.loose_points + m.set3.score(ot)

            # if current team is the winner
            if t == w:
                self.win_matches = self.win_matches + 1
                if not m.two_sets_only:
                    self.loose_sets = self.loose_sets+1

            # current is the looser
            else:
                self.loose_sets = self.loose_sets + 2


    def update_stats(self):
        self._stats = PlayerStats()
        for m in self.matches:
            if m.status == 0 or m.status == -1:
                continue
            print(m)
            stats = m.get_player_match_stats(self)
            self._stats.add(stats)
            print(self._stats)
        self.player_stats_changed.emit()

    @property
    def stats(self):
        return self._stats
