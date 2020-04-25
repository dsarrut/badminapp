
from PySide2 import QtWidgets
from .ui_WaitingPlayersWidget import Ui_WaitingPlayersWidget
from PySide2.QtWidgets import QLabel
from .WaitingPlayerWidget import WaitingPlayerWidget

class WaitingPlayersWidget(QtWidgets.QWidget, Ui_WaitingPlayersWidget):

    def __init__(self, parent=None):
        '''
        Constructor
        '''
        super().__init__(parent)
        self.setupUi(self)

        self.remove_widgets()

    def remove_widgets(self):
        # remove current labels
        c = self.verticalLayout.takeAt(0)
        while c:
            c.widget().setParent(None)
            del c
            c = self.verticalLayout.takeAt(0)
        self.labels = []

    def set_waiting_players(self, round):
        self.round = round
        self.waiting_list = round.waiting_players
        self.remove_widgets()
        for p in self.waiting_list:
            wp = WaitingPlayerWidget(self, p, round)
            self.verticalLayout.addWidget(wp)
            self.labels.append(wp)
        self.round.round_waiting_list_changed.connect(self.slot_on_list_changed)

    def slot_on_list_changed(self):
        self.set_waiting_players(self.round)