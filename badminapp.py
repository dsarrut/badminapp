#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import sys
from PySide2.QtWidgets import QApplication
from ui import MainWindow
from core.Player import Player
from core.Tournament import Tournament
import qdarkstyle


t = Tournament()
n = 31
players = []
for i in range(n):
    players.append(Player())
t.set_players(players)

app = QApplication(sys.argv)
m = MainWindow()
m.set_tournament(t)
m.slot_on_next_round()
m.tab.setCurrentIndex(0)
t.rounds[0].set_debug_mode(False)

m.show()
app.exec_()
