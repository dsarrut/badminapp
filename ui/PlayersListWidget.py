
from PySide2 import QtWidgets
from PySide2.QtCore import Slot, Signal, QSize
from PySide2.QtGui import QPixmap, QPalette, QColor, QFont
from PySide2.QtWidgets import QAction
from .ui_PlayersListWidget import Ui_PlayersListWidget


class PlayersListWidget(QtWidgets.QWidget, Ui_PlayersListWidget):

    def __init__(self, parent=None):
        '''
        Constructor
        '''
        super().__init__(parent)
        self.setupUi(self)
        print('ici')