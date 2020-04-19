# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'PlayerWidget.ui'
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


class Ui_PlayerWidget(object):
    def setupUi(self, PlayerWidget):
        if PlayerWidget.objectName():
            PlayerWidget.setObjectName(u"PlayerWidget")
        PlayerWidget.resize(47, 16)
        self.gridLayout = QGridLayout(PlayerWidget)
        self.gridLayout.setObjectName(u"gridLayout")
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.label = QLabel(PlayerWidget)
        self.label.setObjectName(u"label")

        self.gridLayout.addWidget(self.label, 0, 0, 1, 1)


        self.retranslateUi(PlayerWidget)

        QMetaObject.connectSlotsByName(PlayerWidget)
    # setupUi

    def retranslateUi(self, PlayerWidget):
        PlayerWidget.setWindowTitle(QCoreApplication.translate("PlayerWidget", u"Form", None))
        self.label.setText(QCoreApplication.translate("PlayerWidget", u"TextLabel", None))
    # retranslateUi

