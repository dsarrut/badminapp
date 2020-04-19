#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import sys
from PySide2.QtWidgets import QApplication
from ui import MatchWidget
from core import Match
from core import Team


match = Match()

app = QApplication(sys.argv)
m = MatchWidget(None)
m.set_match(match)
m.show()
app.exec_()
