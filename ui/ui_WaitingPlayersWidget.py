# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'WaitingPlayersWidget.ui'
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

import badminapp_rc

class Ui_WaitingPlayersWidget(object):
    def setupUi(self, WaitingPlayersWidget):
        if WaitingPlayersWidget.objectName():
            WaitingPlayersWidget.setObjectName(u"WaitingPlayersWidget")
        WaitingPlayersWidget.resize(401, 182)
        self.gridLayout = QGridLayout(WaitingPlayersWidget)
        self.gridLayout.setObjectName(u"gridLayout")
        self.frame = QFrame(WaitingPlayersWidget)
        self.frame.setObjectName(u"frame")
        self.frame.setFrameShape(QFrame.Box)
        self.frame.setFrameShadow(QFrame.Raised)
        self.verticalLayout_2 = QVBoxLayout(self.frame)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.label_5 = QLabel(self.frame)
        self.label_5.setObjectName(u"label_5")
        font = QFont()
        font.setPointSize(9)
        font.setBold(True)
        font.setWeight(75)
        self.label_5.setFont(font)

        self.verticalLayout_2.addWidget(self.label_5)

        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.label = QLabel(self.frame)
        self.label.setObjectName(u"label")

        self.verticalLayout.addWidget(self.label)

        self.label_2 = QLabel(self.frame)
        self.label_2.setObjectName(u"label_2")

        self.verticalLayout.addWidget(self.label_2)

        self.label_3 = QLabel(self.frame)
        self.label_3.setObjectName(u"label_3")

        self.verticalLayout.addWidget(self.label_3)


        self.horizontalLayout.addLayout(self.verticalLayout)

        self.horizontalSpacer_3 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout.addItem(self.horizontalSpacer_3)

        self.label_4 = QLabel(self.frame)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setEnabled(True)
        self.label_4.setMaximumSize(QSize(120, 120))
        self.label_4.setPixmap(QPixmap(u":/icons/hamac.png"))
        self.label_4.setScaledContents(True)

        self.horizontalLayout.addWidget(self.label_4)

        self.horizontalSpacer_2 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout.addItem(self.horizontalSpacer_2)


        self.verticalLayout_2.addLayout(self.horizontalLayout)


        self.gridLayout.addWidget(self.frame, 0, 1, 1, 1)

        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.gridLayout.addItem(self.horizontalSpacer, 0, 0, 1, 1)

        self.horizontalSpacer_4 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.gridLayout.addItem(self.horizontalSpacer_4, 0, 2, 1, 1)


        self.retranslateUi(WaitingPlayersWidget)

        QMetaObject.connectSlotsByName(WaitingPlayersWidget)
    # setupUi

    def retranslateUi(self, WaitingPlayersWidget):
        WaitingPlayersWidget.setWindowTitle(QCoreApplication.translate("WaitingPlayersWidget", u"Form", None))
        self.label_5.setText(QCoreApplication.translate("WaitingPlayersWidget", u"Joueurs ne participants pas \u00e0 ce tour ...", None))
        self.label.setText(QCoreApplication.translate("WaitingPlayersWidget", u"TextLabel", None))
        self.label_2.setText(QCoreApplication.translate("WaitingPlayersWidget", u"TextLabel", None))
        self.label_3.setText(QCoreApplication.translate("WaitingPlayersWidget", u"TextLabel", None))
        self.label_4.setText("")
    # retranslateUi

