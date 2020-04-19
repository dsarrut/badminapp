from random import randint
import io
from PySide2.QtCore import Signal, QObject
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
        self.selected = True # FIXME

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
        if i == 0:
            self._first_name = value
            self.player_name_changed.emit()
            return
        if i == 1:
            self._last_name = value
            self.player_name_changed.emit()
            return

    def get_name(self, i):
        if i == 0:
            return self._first_name
        if i == 1:
            return self._last_name

    def add_match(self, match):
        if match == None:
            return
        self.matches.append(match)

    def update_stats(self):
        self._stats = PlayerStats()
        for m in self.matches:
            if m.status == 0 or m.status == -1:
                continue
            stats = m.get_player_match_stats(self)
            self._stats.add(stats)
        self.player_stats_changed.emit()

    @property
    def stats(self):
        return self._stats
