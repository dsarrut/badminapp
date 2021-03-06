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

import badminapp_rc

class Ui_PlayersListWidget(object):
    def setupUi(self, PlayersListWidget):
        if PlayersListWidget.objectName():
            PlayersListWidget.setObjectName(u"PlayersListWidget")
        PlayersListWidget.resize(1285, 548)
        self.horizontalLayout_2 = QHBoxLayout(PlayersListWidget)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.frame = QFrame(PlayersListWidget)
        self.frame.setObjectName(u"frame")
        self.frame.setMaximumSize(QSize(680, 16777215))
        self.frame.setFrameShape(QFrame.StyledPanel)
        self.frame.setFrameShadow(QFrame.Raised)
        self.horizontalLayout = QHBoxLayout(self.frame)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.label = QLabel(self.frame)
        self.label.setObjectName(u"label")

        self.horizontalLayout.addWidget(self.label)

        self.edit_filter = QLineEdit(self.frame)
        self.edit_filter.setObjectName(u"edit_filter")
        self.edit_filter.setMinimumSize(QSize(200, 0))
        self.edit_filter.setMaximumSize(QSize(200, 16777215))

        self.horizontalLayout.addWidget(self.edit_filter)

        self.horizontalSpacer_6 = QSpacerItem(13, 21, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout.addItem(self.horizontalSpacer_6)

        self.label_status = QLabel(self.frame)
        self.label_status.setObjectName(u"label_status")

        self.horizontalLayout.addWidget(self.label_status)

        self.horizontalSpacer_3 = QSpacerItem(13, 21, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout.addItem(self.horizontalSpacer_3)

        self.button_add = QPushButton(self.frame)
        self.button_add.setObjectName(u"button_add")
        icon = QIcon()
        icon.addFile(u":/icons/128x128/actions/document-new-8.png", QSize(), QIcon.Normal, QIcon.On)
        self.button_add.setIcon(icon)

        self.horizontalLayout.addWidget(self.button_add)

        self.horizontalSpacer_2 = QSpacerItem(13, 21, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout.addItem(self.horizontalSpacer_2)

        self.button_del = QPushButton(self.frame)
        self.button_del.setObjectName(u"button_del")
        icon1 = QIcon()
        icon1.addFile(u":/icons/128x128/actions/edit-delete-shred.png", QSize(), QIcon.Normal, QIcon.On)
        self.button_del.setIcon(icon1)

        self.horizontalLayout.addWidget(self.button_del)

        self.horizontalSpacer_4 = QSpacerItem(13, 21, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout.addItem(self.horizontalSpacer_4)


        self.verticalLayout.addWidget(self.frame)

        self.table_widget = QTableView(PlayersListWidget)
        self.table_widget.setObjectName(u"table_widget")
        self.table_widget.setMaximumSize(QSize(625, 16777215))

        self.verticalLayout.addWidget(self.table_widget)


        self.horizontalLayout_2.addLayout(self.verticalLayout)

        self.horizontalSpacer_7 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_2.addItem(self.horizontalSpacer_7)

        self.label_2 = QLabel(PlayersListWidget)
        self.label_2.setObjectName(u"label_2")
        sizePolicy = QSizePolicy(QSizePolicy.Minimum, QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_2.sizePolicy().hasHeightForWidth())
        self.label_2.setSizePolicy(sizePolicy)
        self.label_2.setMaximumSize(QSize(350, 350))
        self.label_2.setFrameShape(QFrame.StyledPanel)
        self.label_2.setFrameShadow(QFrame.Sunken)
        self.label_2.setPixmap(QPixmap(u":/icons/bad.jpg"))
        self.label_2.setScaledContents(True)

        self.horizontalLayout_2.addWidget(self.label_2)

        self.horizontalSpacer_8 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_2.addItem(self.horizontalSpacer_8)


        self.retranslateUi(PlayersListWidget)

        QMetaObject.connectSlotsByName(PlayersListWidget)
    # setupUi

    def retranslateUi(self, PlayersListWidget):
        PlayersListWidget.setWindowTitle(QCoreApplication.translate("PlayersListWidget", u"Form", None))
        self.label.setText(QCoreApplication.translate("PlayersListWidget", u"Filtre :", None))
        self.label_status.setText(QCoreApplication.translate("PlayersListWidget", u"Il y actuellement 0 joueur", None))
        self.button_add.setText(QCoreApplication.translate("PlayersListWidget", u"Ajouter un joueur", None))
        self.button_del.setText(QCoreApplication.translate("PlayersListWidget", u"Supprimer", None))
        self.label_2.setText("")
    # retranslateUi

