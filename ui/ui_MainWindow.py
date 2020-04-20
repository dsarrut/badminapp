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

import badminapp_rc

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(1319, 842)
        self.action_debug_mode = QAction(MainWindow)
        self.action_debug_mode.setObjectName(u"action_debug_mode")
        self.action_debug_mode.setCheckable(True)
        icon = QIcon()
        icon.addFile(u":/icons/128x128/actions/system-run-6.png", QSize(), QIcon.Normal, QIcon.Off)
        self.action_debug_mode.setIcon(icon)
        self.action_exit = QAction(MainWindow)
        self.action_exit.setObjectName(u"action_exit")
        icon1 = QIcon()
        icon1.addFile(u":/icons/128x128/actions/application-exit-5.png", QSize(), QIcon.Normal, QIcon.Off)
        self.action_exit.setIcon(icon1)
        self.action_save = QAction(MainWindow)
        self.action_save.setObjectName(u"action_save")
        icon2 = QIcon()
        icon2.addFile(u":/icons/128x128/actions/document-export.png", QSize(), QIcon.Normal, QIcon.Off)
        self.action_save.setIcon(icon2)
        self.action_load = QAction(MainWindow)
        self.action_load.setObjectName(u"action_load")
        icon3 = QIcon()
        icon3.addFile(u":/icons/128x128/actions/document-open-5.png", QSize(), QIcon.Normal, QIcon.Off)
        self.action_load.setIcon(icon3)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.gridLayout = QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName(u"gridLayout")
        self.tab = QTabWidget(self.centralwidget)
        self.tab.setObjectName(u"tab")
        self.tab.setAutoFillBackground(True)
        self.tab_player = QWidget()
        self.tab_player.setObjectName(u"tab_player")
        self.layout_2 = QGridLayout(self.tab_player)
        self.layout_2.setObjectName(u"layout_2")
        self.widget = QWidget(self.tab_player)
        self.widget.setObjectName(u"widget")
        self.widget.setAutoFillBackground(True)

        self.layout_2.addWidget(self.widget, 0, 0, 1, 1)

        self.tab.addTab(self.tab_player, "")
        self.tab_round1 = QWidget()
        self.tab_round1.setObjectName(u"tab_round1")
        self.tab_round1.setAutoFillBackground(True)
        self.layout = QGridLayout(self.tab_round1)
        self.layout.setObjectName(u"layout")
        self.tab.addTab(self.tab_round1, "")

        self.gridLayout.addWidget(self.tab, 0, 0, 1, 1)

        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 1319, 21))
        self.menucoucou = QMenu(self.menubar)
        self.menucoucou.setObjectName(u"menucoucou")
        MainWindow.setMenuBar(self.menubar)

        self.menubar.addAction(self.menucoucou.menuAction())
        self.menucoucou.addAction(self.action_save)
        self.menucoucou.addAction(self.action_load)
        self.menucoucou.addSeparator()
        self.menucoucou.addAction(self.action_debug_mode)
        self.menucoucou.addAction(self.action_exit)

        self.retranslateUi(MainWindow)

        self.tab.setCurrentIndex(0)


        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"Badmin-App", None))
        self.action_debug_mode.setText(QCoreApplication.translate("MainWindow", u"Debug mode", None))
#if QT_CONFIG(tooltip)
        self.action_debug_mode.setToolTip(QCoreApplication.translate("MainWindow", u"Debug mode", None))
#endif // QT_CONFIG(tooltip)
        self.action_exit.setText(QCoreApplication.translate("MainWindow", u"Quitter", None))
#if QT_CONFIG(shortcut)
        self.action_exit.setShortcut(QCoreApplication.translate("MainWindow", u"Ctrl+Q", None))
#endif // QT_CONFIG(shortcut)
        self.action_save.setText(QCoreApplication.translate("MainWindow", u"Sauvergarder la liste des joueurs", None))
#if QT_CONFIG(shortcut)
        self.action_save.setShortcut(QCoreApplication.translate("MainWindow", u"Ctrl+S", None))
#endif // QT_CONFIG(shortcut)
        self.action_load.setText(QCoreApplication.translate("MainWindow", u"Charger une liste de joueurs", None))
#if QT_CONFIG(shortcut)
        self.action_load.setShortcut(QCoreApplication.translate("MainWindow", u"Ctrl+O", None))
#endif // QT_CONFIG(shortcut)
        self.tab.setTabText(self.tab.indexOf(self.tab_player), QCoreApplication.translate("MainWindow", u"Joueurs", None))
        self.tab.setTabText(self.tab.indexOf(self.tab_round1), QCoreApplication.translate("MainWindow", u"Tour n\u00b01", None))
        self.menucoucou.setTitle(QCoreApplication.translate("MainWindow", u"Options", None))
    # retranslateUi

