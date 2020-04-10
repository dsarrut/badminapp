
from PySide2 import QtWidgets
from .ui_WaitingPlayersWidget import Ui_WaitingPlayersWidget
from PySide2.QtWidgets import QLabel

class WaitingPlayersWidget(QtWidgets.QWidget, Ui_WaitingPlayersWidget):

    def __init__(self, parent=None):
        '''
        Constructor
        '''
        super().__init__(parent)
        self.setupUi(self)

        self.remove_labels()

    def remove_labels(self):
        # remove current labels
        c = self.verticalLayout.takeAt(0)
        while c:
            c.widget().setParent(None)
            del c
            c = self.verticalLayout.takeAt(0)
        self.labels = []

    def set_waiting_players(self, waiting_list):
        self.waiting_list = waiting_list
        self.remove_labels()
        for p in self.waiting_list:
            l = QLabel(self)
            l.setText(str(p))
            self.verticalLayout.addWidget(l)
            self.labels.append(l)