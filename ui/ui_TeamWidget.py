# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'TeamWidget.ui'
##
## Created by: Qt User Interface Compiler version 5.14.1
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import (QCoreApplication, QMetaObject, QObject, QPoint,
    QRect, QSize, QUrl, Qt)
from PySide2.QtGui import (QBrush, QColor, QConicalGradient, QCursor, QFont,
    QFontDatabase, QIcon, QLinearGradient, QPalette, QPainter, QPixmap,
    QRadialGradient)
from PySide2.QtWidgets import *


class Ui_TeamWidget(object):
    def setupUi(self, TeamWidget):
        if TeamWidget.objectName():
            TeamWidget.setObjectName(u"TeamWidget")
        TeamWidget.resize(250, 21)
        TeamWidget.setMinimumSize(QSize(250, 0))
        TeamWidget.setMaximumSize(QSize(250, 16777215))
        self.horizontalLayout = QHBoxLayout(TeamWidget)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.label_player1 = QLabel(TeamWidget)
        self.label_player1.setObjectName(u"label_player1")
        self.label_player1.setAcceptDrops(False)

        self.horizontalLayout.addWidget(self.label_player1)

        self.label_separator = QLabel(TeamWidget)
        self.label_separator.setObjectName(u"label_separator")
        font = QFont()
        font.setPointSize(13)
        font.setBold(True)
        font.setWeight(75)
        self.label_separator.setFont(font)

        self.horizontalLayout.addWidget(self.label_separator)

        self.label_player2 = QLabel(TeamWidget)
        self.label_player2.setObjectName(u"label_player2")
        self.label_player2.setAcceptDrops(False)

        self.horizontalLayout.addWidget(self.label_player2)

        self.horizontalSpacer = QSpacerItem(128, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout.addItem(self.horizontalSpacer)


        self.retranslateUi(TeamWidget)

        QMetaObject.connectSlotsByName(TeamWidget)
    # setupUi

    def retranslateUi(self, TeamWidget):
        TeamWidget.setWindowTitle(QCoreApplication.translate("TeamWidget", u"Form", None))
        self.label_player1.setText(QCoreApplication.translate("TeamWidget", u"TextLabel", None))
        self.label_separator.setText(QCoreApplication.translate("TeamWidget", u"-", None))
        self.label_player2.setText(QCoreApplication.translate("TeamWidget", u"TextLabel", None))
    # retranslateUi

