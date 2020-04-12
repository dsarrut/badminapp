from random import randint
import io
from PySide2.QtCore import Slot, Signal, QObject


word_file = "qrc/nouns.txt"
WORDS = io.open("qrc/nouns.txt", mode="r", encoding="utf-8").read().splitlines()

def random_word():
    value = randint(0, len(WORDS))
    return WORDS[value].split(';')[0]

class Player(QObject):

    _last_id = 0
    player_name_changed = Signal()

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

