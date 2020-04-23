#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import sys
from PySide2.QtWidgets import QApplication
from ui import RoundWidget
from core.Player import Player
from core.Round import Round


n = 29
players = []
for i in range(n):
    players.append(Player())

round = Round()
round.set_players_list(players)
round.create_matches()

app = QApplication(sys.argv)
m = RoundWidget(None)
m.set_round(round)
m.show()
app.exec_()