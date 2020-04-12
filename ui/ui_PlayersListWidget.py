# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'PlayersListWidget.ui'
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


class Ui_PlayersListWidget(object):
    def setupUi(self, PlayersListWidget):
        if PlayersListWidget.objectName():
            PlayersListWidget.setObjectName(u"PlayersListWidget")
        PlayersListWidget.resize(1066, 688)
        self.gridLayout = QGridLayout(PlayersListWidget)
        self.gridLayout.setObjectName(u"gridLayout")
        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.edit_filter = QLineEdit(PlayersListWidget)
        self.edit_filter.setObjectName(u"edit_filter")
        self.edit_filter.setMinimumSize(QSize(200, 0))
        self.edit_filter.setMaximumSize(QSize(200, 16777215))

        self.horizontalLayout.addWidget(self.edit_filter)

        self.pushButton = QPushButton(PlayersListWidget)
        self.pushButton.setObjectName(u"pushButton")
        icon = QIcon()
        icon.addFile(u":/icons/128x128/actions/edit-clear-locationbar-rtl.png", QSize(), QIcon.Normal, QIcon.On)
        self.pushButton.setIcon(icon)

        self.horizontalLayout.addWidget(self.pushButton)

        self.horizontalSpacer_3 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout.addItem(self.horizontalSpacer_3)

        self.button_add = QPushButton(PlayersListWidget)
        self.button_add.setObjectName(u"button_add")
        icon1 = QIcon()
        icon1.addFile(u":/icons/128x128/actions/document-new-8.png", QSize(), QIcon.Normal, QIcon.On)
        self.button_add.setIcon(icon1)

        self.horizontalLayout.addWidget(self.button_add)

        self.horizontalSpacer_2 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout.addItem(self.horizontalSpacer_2)

        self.button_del = QPushButton(PlayersListWidget)
        self.button_del.setObjectName(u"button_del")
        icon2 = QIcon()
        icon2.addFile(u":/icons/128x128/actions/edit-delete-shred.png", QSize(), QIcon.Normal, QIcon.On)
        self.button_del.setIcon(icon2)

        self.horizontalLayout.addWidget(self.button_del)

        self.horizontalSpacer_4 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout.addItem(self.horizontalSpacer_4)

        self.horizontalSpacer_5 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout.addItem(self.horizontalSpacer_5)

        self.label_status = QLabel(PlayersListWidget)
        self.label_status.setObjectName(u"label_status")

        self.horizontalLayout.addWidget(self.label_status)

        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout.addItem(self.horizontalSpacer)


        self.gridLayout.addLayout(self.horizontalLayout, 0, 0, 1, 1)

        self.table_widget = QTableView(PlayersListWidget)
        self.table_widget.setObjectName(u"table_widget")

        self.gridLayout.addWidget(self.table_widget, 1, 0, 1, 1)


        self.retranslateUi(PlayersListWidget)

        QMetaObject.connectSlotsByName(PlayersListWidget)
    # setupUi

    def retranslateUi(self, PlayersListWidget):
        PlayersListWidget.setWindowTitle(QCoreApplication.translate("PlayersListWidget", u"Form", None))
        self.pushButton.setText("")
        self.button_add.setText(QCoreApplication.translate("PlayersListWidget", u"Ajouter un joueur", None))
        self.button_del.setText(QCoreApplication.translate("PlayersListWidget", u"Supprimer", None))
        self.label_status.setText(QCoreApplication.translate("PlayersListWidget", u"Il y actuellement 0 joueur", None))
    # retranslateUi

