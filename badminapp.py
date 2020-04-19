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

round = t.new_round()
round.fields_number = 5

app = QApplication(sys.argv)
m = MainWindow()
m.set_tournament(t)
m.set_round(round)
#app.setStyleSheet(qdarkstyle.load_stylesheet_pyqt5())
#app.setStyleSheet(qdarkstyle.load_stylesheet(qt_api='pyqt5'))
#app.setStyleSheet(qdarkstyle.load_stylesheet(qt_api='pyside2'))

m.show()
app.exec_()
