from random import randint
#from random import seed
import io

word_file = "qrc/nouns.txt"
WORDS = io.open("qrc/nouns.txt", mode="r", encoding="utf-8").read().splitlines()

#seed(1234)

def random_word():
    value = randint(0, len(WORDS))
    return WORDS[value].split(';')[0]

class Player:

    def __init__(self, first=None, last=None):
        if not first:
            first = random_word()
        if not last:
            last = random_word()
        self.first_name = first.capitalize()
        self.last_name = last.capitalize()

    def __str__(self):
        s = f'{self.first_name} {self.last_name}'
        return s

