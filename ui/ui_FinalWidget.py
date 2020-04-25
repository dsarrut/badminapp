# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'FinalWidget.ui'
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


class Ui_FinalWidget(object):
    def setupUi(self, FinalWidget):
        if FinalWidget.objectName():
            FinalWidget.setObjectName(u"FinalWidget")
        FinalWidget.resize(1068, 566)
        FinalWidget.setAutoFillBackground(False)
        FinalWidget.setStyleSheet(u"background-image: url(:/icons/cup-960-512.png);\n"
" background-repeat: no-repeat;\n"
"")
        self.gridLayout = QGridLayout(FinalWidget)
        self.gridLayout.setObjectName(u"gridLayout")
        self.scrollArea = QScrollArea(FinalWidget)
        self.scrollArea.setObjectName(u"scrollArea")
        self.scrollArea.setAutoFillBackground(True)
        self.scrollArea.setWidgetResizable(True)
        self.scrollAreaWidgetContents = QWidget()
        self.scrollAreaWidgetContents.setObjectName(u"scrollAreaWidgetContents")
        self.scrollAreaWidgetContents.setGeometry(QRect(0, 0, 1048, 546))
        self.label_player2 = QLabel(self.scrollAreaWidgetContents)
        self.label_player2.setObjectName(u"label_player2")
        self.label_player2.setGeometry(QRect(1, 270, 291, 21))
        font = QFont()
        font.setPointSize(13)
        self.label_player2.setFont(font)
        self.label_player2.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)
        self.label_player1 = QLabel(self.scrollAreaWidgetContents)
        self.label_player1.setObjectName(u"label_player1")
        self.label_player1.setGeometry(QRect(200, 40, 591, 23))
        font1 = QFont()
        font1.setPointSize(14)
        self.label_player1.setFont(font1)
        self.label_player1.setAlignment(Qt.AlignCenter)
        self.label_stats2 = QLabel(self.scrollAreaWidgetContents)
        self.label_stats2.setObjectName(u"label_stats2")
        self.label_stats2.setGeometry(QRect(280, 360, 151, 64))
        font2 = QFont()
        font2.setPointSize(10)
        self.label_stats2.setFont(font2)
        self.label_stats2.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)
        self.label_stats1 = QLabel(self.scrollAreaWidgetContents)
        self.label_stats1.setObjectName(u"label_stats1")
        self.label_stats1.setGeometry(QRect(460, 270, 141, 64))
        self.label_stats1.setFont(font2)
        self.label_stats1.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)
        self.label_stats3 = QLabel(self.scrollAreaWidgetContents)
        self.label_stats3.setObjectName(u"label_stats3")
        self.label_stats3.setGeometry(QRect(630, 360, 141, 64))
        self.label_stats3.setFont(font2)
        self.label_stats3.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)
        self.label_player3 = QLabel(self.scrollAreaWidgetContents)
        self.label_player3.setObjectName(u"label_player3")
        self.label_player3.setGeometry(QRect(680, 280, 351, 21))
        self.label_player3.setFont(font)
        self.label_player3.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)
        self.label_tournament = QLabel(self.scrollAreaWidgetContents)
        self.label_tournament.setObjectName(u"label_tournament")
        self.label_tournament.setGeometry(QRect(20, 10, 181, 64))
        font3 = QFont()
        font3.setPointSize(11)
        font3.setBold(False)
        font3.setWeight(50)
        self.label_tournament.setFont(font3)
        self.label_tournament.setFrameShape(QFrame.Panel)
        self.label_tournament.setFrameShadow(QFrame.Raised)
        self.label_tournament.setAlignment(Qt.AlignCenter)
        self.scrollArea.setWidget(self.scrollAreaWidgetContents)

        self.gridLayout.addWidget(self.scrollArea, 0, 0, 1, 1)


        self.retranslateUi(FinalWidget)

        QMetaObject.connectSlotsByName(FinalWidget)
    # setupUi

    def retranslateUi(self, FinalWidget):
        FinalWidget.setWindowTitle(QCoreApplication.translate("FinalWidget", u"Form", None))
        self.label_player2.setText(QCoreApplication.translate("FinalWidget", u"MarcelChose Truc Bidule", None))
        self.label_player1.setText(QCoreApplication.translate("FinalWidget", u"MarcelChose Truc Bidule", None))
        self.label_stats2.setText(QCoreApplication.translate("FinalWidget", u"5 matchs jou\u00e9s\n"
"4 match gagn\u00e9s\n"
"+8 sets\n"
"+123 points", None))
        self.label_stats1.setText(QCoreApplication.translate("FinalWidget", u"5 matchs jou\u00e9s\n"
"4 match gagn\u00e9s\n"
"+8 sets\n"
"+123 points", None))
        self.label_stats3.setText(QCoreApplication.translate("FinalWidget", u"5 matchs jou\u00e9s\n"
"4 match gagn\u00e9s\n"
"+8 sets\n"
"+123 points", None))
        self.label_player3.setText(QCoreApplication.translate("FinalWidget", u"MarcelChose Truc Bidule", None))
        self.label_tournament.setText(QCoreApplication.translate("FinalWidget", u"Tournoi termin\u00e9 ! \n"
"32 joueurs \n"
"4 tours", None))
    # retranslateUi

