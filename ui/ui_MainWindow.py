# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'MainWindow.ui'
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


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(1319, 842)
        self.action_random_score = QAction(MainWindow)
        self.action_random_score.setObjectName(u"action_random_score")
        self.actionyop = QAction(MainWindow)
        self.actionyop.setObjectName(u"actionyop")
        self.action_exit = QAction(MainWindow)
        self.action_exit.setObjectName(u"action_exit")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.gridLayout = QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName(u"gridLayout")
        self.tab = QTabWidget(self.centralwidget)
        self.tab.setObjectName(u"tab")
        self.tab.setAutoFillBackground(True)
        self.tab_player = QWidget()
        self.tab_player.setObjectName(u"tab_player")
        self.tab.addTab(self.tab_player, "")
        self.tab_round1 = QWidget()
        self.tab_round1.setObjectName(u"tab_round1")
        self.tab_round1.setAutoFillBackground(True)
        self.layout = QGridLayout(self.tab_round1)
        self.layout.setObjectName(u"layout")
        self.tab.addTab(self.tab_round1, "")

        self.gridLayout.addWidget(self.tab, 0, 0, 1, 1)

        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 1319, 21))
        self.menucoucou = QMenu(self.menubar)
        self.menucoucou.setObjectName(u"menucoucou")
        self.menutoto = QMenu(self.menubar)
        self.menutoto.setObjectName(u"menutoto")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.menubar.addAction(self.menucoucou.menuAction())
        self.menubar.addAction(self.menutoto.menuAction())
        self.menucoucou.addAction(self.actionyop)
        self.menucoucou.addAction(self.action_exit)
        self.menutoto.addAction(self.action_random_score)

        self.retranslateUi(MainWindow)

        self.tab.setCurrentIndex(1)


        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"Badmin-App", None))
        self.action_random_score.setText(QCoreApplication.translate("MainWindow", u"random score", None))
        self.actionyop.setText(QCoreApplication.translate("MainWindow", u"yop", None))
        self.action_exit.setText(QCoreApplication.translate("MainWindow", u"Quitter", None))
#if QT_CONFIG(shortcut)
        self.action_exit.setShortcut(QCoreApplication.translate("MainWindow", u"Ctrl+Q", None))
#endif // QT_CONFIG(shortcut)
        self.tab.setTabText(self.tab.indexOf(self.tab_player), QCoreApplication.translate("MainWindow", u"Joueurs", None))
        self.tab.setTabText(self.tab.indexOf(self.tab_round1), QCoreApplication.translate("MainWindow", u"Tour n\u00b01", None))
        self.menucoucou.setTitle(QCoreApplication.translate("MainWindow", u"coucou", None))
        self.menutoto.setTitle(QCoreApplication.translate("MainWindow", u"toto", None))
    # retranslateUi

