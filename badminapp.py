#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import sys
from PySide2.QtWidgets import QApplication
from ui import MainWindow
from core.Player import Player
from core.Round import Round
from core.Tournament import Tournament

t = Tournament()
n = 31
players = []
for i in range(n):
    players.append(Player())
t.set_players_list(players)

round = t.new_round()
round.fields_number = 5
#round.create_matches()

app = QApplication(sys.argv)
m = MainWindow()
m.set_tournament(t)
m.set_round(round)
m.show()
app.exec_()
