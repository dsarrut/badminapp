from .helpers import *
from .Player import Player

class Team:

    def __init__(self, player1=None, player2=None):
        # later will be simple/double
        if not player1:
            player1 = Player()
        if not player2:
            player2 = Player()
        self.player1 = player1
        self.player2 = player2

    def __str__(self):
        s = f'{self.player1}/{self.player2}'
        return s

    def set_player(self, i, player):
        if i == 1:
            self.player1 = player
        if i == 2:
            self.player2 = player
        raise_except(f'Team must be 1 or 2 while it is {i}')

