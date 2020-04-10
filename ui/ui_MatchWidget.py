# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'MatchWidget.ui'
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

class Ui_MatchWidget(object):
    def setupUi(self, MatchWidget):
        if MatchWidget.objectName():
            MatchWidget.setObjectName(u"MatchWidget")
        MatchWidget.resize(547, 157)
        self.actionTest1 = QAction(MatchWidget)
        self.actionTest1.setObjectName(u"actionTest1")
        icon = QIcon()
        icon.addFile(u":/icons/128x128/actions/dialog-ok-2.png", QSize(), QIcon.Normal, QIcon.Off)
        self.actionTest1.setIcon(icon)
        self.actionTest2 = QAction(MatchWidget)
        self.actionTest2.setObjectName(u"actionTest2")
        self.verticalLayout_4 = QVBoxLayout(MatchWidget)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_4.addItem(self.verticalSpacer)

        self.horizontalLayout_3 = QHBoxLayout()
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.horizontalSpacer = QSpacerItem(13, 63, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_3.addItem(self.horizontalSpacer)

        self.w_field = QWidget(MatchWidget)
        self.w_field.setObjectName(u"w_field")
        self.gridLayout_2 = QGridLayout(self.w_field)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.label_field = QLabel(self.w_field)
        self.label_field.setObjectName(u"label_field")
        font = QFont()
        font.setPointSize(29)
        font.setBold(True)
        font.setWeight(75)
        self.label_field.setFont(font)
        self.label_field.setContextMenuPolicy(Qt.ActionsContextMenu)

        self.gridLayout_2.addWidget(self.label_field, 0, 0, 1, 1)


        self.horizontalLayout_3.addWidget(self.w_field)

        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.team1 = QLabel(MatchWidget)
        self.team1.setObjectName(u"team1")
        self.team1.setMinimumSize(QSize(250, 0))
        self.team1.setMaximumSize(QSize(250, 16777215))
        font1 = QFont()
        font1.setPointSize(8)
        self.team1.setFont(font1)
        self.team1.setAutoFillBackground(False)

        self.verticalLayout.addWidget(self.team1)

        self.team2 = QLabel(MatchWidget)
        self.team2.setObjectName(u"team2")
        self.team2.setMinimumSize(QSize(250, 0))
        self.team2.setMaximumSize(QSize(250, 16777215))
        self.team2.setFont(font1)

        self.verticalLayout.addWidget(self.team2)


        self.horizontalLayout_3.addLayout(self.verticalLayout)

        self.verticalLayout_2 = QVBoxLayout()
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.spin_box_t1_s1 = QSpinBox(MatchWidget)
        self.spin_box_t1_s1.setObjectName(u"spin_box_t1_s1")
        self.spin_box_t1_s1.setMinimumSize(QSize(50, 0))
        font2 = QFont()
        font2.setPointSize(9)
        font2.setBold(True)
        font2.setWeight(75)
        self.spin_box_t1_s1.setFont(font2)
        self.spin_box_t1_s1.setCursor(QCursor(Qt.IBeamCursor))
        self.spin_box_t1_s1.setMouseTracking(False)
        self.spin_box_t1_s1.setLayoutDirection(Qt.LeftToRight)
        self.spin_box_t1_s1.setAutoFillBackground(False)
        self.spin_box_t1_s1.setAlignment(Qt.AlignCenter)
        self.spin_box_t1_s1.setButtonSymbols(QAbstractSpinBox.UpDownArrows)
        self.spin_box_t1_s1.setAccelerated(False)
        self.spin_box_t1_s1.setProperty("showGroupSeparator", False)
        self.spin_box_t1_s1.setMaximum(29)

        self.horizontalLayout.addWidget(self.spin_box_t1_s1)

        self.spin_box_t1_s2 = QSpinBox(MatchWidget)
        self.spin_box_t1_s2.setObjectName(u"spin_box_t1_s2")
        self.spin_box_t1_s2.setMinimumSize(QSize(47, 0))
        self.spin_box_t1_s2.setFont(font2)
        self.spin_box_t1_s2.setCursor(QCursor(Qt.IBeamCursor))
        self.spin_box_t1_s2.setMouseTracking(False)
        self.spin_box_t1_s2.setLayoutDirection(Qt.LeftToRight)
        self.spin_box_t1_s2.setAlignment(Qt.AlignCenter)
        self.spin_box_t1_s2.setButtonSymbols(QAbstractSpinBox.UpDownArrows)
        self.spin_box_t1_s2.setAccelerated(False)
        self.spin_box_t1_s2.setProperty("showGroupSeparator", False)
        self.spin_box_t1_s2.setMaximum(29)

        self.horizontalLayout.addWidget(self.spin_box_t1_s2)

        self.spin_box_t1_s3 = QSpinBox(MatchWidget)
        self.spin_box_t1_s3.setObjectName(u"spin_box_t1_s3")
        self.spin_box_t1_s3.setMinimumSize(QSize(47, 0))
        self.spin_box_t1_s3.setFont(font2)
        self.spin_box_t1_s3.setCursor(QCursor(Qt.IBeamCursor))
        self.spin_box_t1_s3.setMouseTracking(False)
        self.spin_box_t1_s3.setLayoutDirection(Qt.LeftToRight)
        self.spin_box_t1_s3.setAlignment(Qt.AlignCenter)
        self.spin_box_t1_s3.setButtonSymbols(QAbstractSpinBox.UpDownArrows)
        self.spin_box_t1_s3.setAccelerated(False)
        self.spin_box_t1_s3.setProperty("showGroupSeparator", False)
        self.spin_box_t1_s3.setMaximum(29)

        self.horizontalLayout.addWidget(self.spin_box_t1_s3)


        self.verticalLayout_2.addLayout(self.horizontalLayout)

        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.spin_box_t2_s1 = QSpinBox(MatchWidget)
        self.spin_box_t2_s1.setObjectName(u"spin_box_t2_s1")
        self.spin_box_t2_s1.setMinimumSize(QSize(47, 0))
        self.spin_box_t2_s1.setFont(font2)
        self.spin_box_t2_s1.setCursor(QCursor(Qt.IBeamCursor))
        self.spin_box_t2_s1.setMouseTracking(False)
        self.spin_box_t2_s1.setLayoutDirection(Qt.LeftToRight)
        self.spin_box_t2_s1.setAlignment(Qt.AlignCenter)
        self.spin_box_t2_s1.setButtonSymbols(QAbstractSpinBox.UpDownArrows)
        self.spin_box_t2_s1.setAccelerated(False)
        self.spin_box_t2_s1.setProperty("showGroupSeparator", False)
        self.spin_box_t2_s1.setMaximum(29)

        self.horizontalLayout_2.addWidget(self.spin_box_t2_s1)

        self.spin_box_t2_s2 = QSpinBox(MatchWidget)
        self.spin_box_t2_s2.setObjectName(u"spin_box_t2_s2")
        self.spin_box_t2_s2.setMinimumSize(QSize(47, 0))
        self.spin_box_t2_s2.setFont(font2)
        self.spin_box_t2_s2.setCursor(QCursor(Qt.IBeamCursor))
        self.spin_box_t2_s2.setMouseTracking(False)
        self.spin_box_t2_s2.setLayoutDirection(Qt.LeftToRight)
        self.spin_box_t2_s2.setAlignment(Qt.AlignCenter)
        self.spin_box_t2_s2.setButtonSymbols(QAbstractSpinBox.UpDownArrows)
        self.spin_box_t2_s2.setAccelerated(False)
        self.spin_box_t2_s2.setProperty("showGroupSeparator", False)
        self.spin_box_t2_s2.setMaximum(29)

        self.horizontalLayout_2.addWidget(self.spin_box_t2_s2)

        self.spin_box_t2_s3 = QSpinBox(MatchWidget)
        self.spin_box_t2_s3.setObjectName(u"spin_box_t2_s3")
        self.spin_box_t2_s3.setMinimumSize(QSize(47, 0))
        self.spin_box_t2_s3.setFont(font2)
        self.spin_box_t2_s3.setCursor(QCursor(Qt.IBeamCursor))
        self.spin_box_t2_s3.setMouseTracking(False)
        self.spin_box_t2_s3.setLayoutDirection(Qt.LeftToRight)
        self.spin_box_t2_s3.setAlignment(Qt.AlignCenter)
        self.spin_box_t2_s3.setButtonSymbols(QAbstractSpinBox.UpDownArrows)
        self.spin_box_t2_s3.setAccelerated(False)
        self.spin_box_t2_s3.setProperty("showGroupSeparator", False)
        self.spin_box_t2_s3.setMaximum(29)

        self.horizontalLayout_2.addWidget(self.spin_box_t2_s3)


        self.verticalLayout_2.addLayout(self.horizontalLayout_2)


        self.horizontalLayout_3.addLayout(self.verticalLayout_2)

        self.verticalLayout_3 = QVBoxLayout()
        self.verticalLayout_3.setSpacing(0)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.status1 = QLabel(MatchWidget)
        self.status1.setObjectName(u"status1")
        self.status1.setEnabled(True)
        self.status1.setMaximumSize(QSize(32, 32))
        self.status1.setPixmap(QPixmap(u":/icons/128x128/emotes/face-angry.png"))
        self.status1.setScaledContents(True)

        self.verticalLayout_3.addWidget(self.status1)

        self.status2 = QLabel(MatchWidget)
        self.status2.setObjectName(u"status2")
        self.status2.setEnabled(True)
        self.status2.setMaximumSize(QSize(32, 32))
        self.status2.setPixmap(QPixmap(u":/icons/128x128/emotes/face-wink-4.png"))
        self.status2.setScaledContents(True)

        self.verticalLayout_3.addWidget(self.status2)


        self.horizontalLayout_3.addLayout(self.verticalLayout_3)

        self.horizontalSpacer_2 = QSpacerItem(13, 63, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_3.addItem(self.horizontalSpacer_2)


        self.verticalLayout_4.addLayout(self.horizontalLayout_3)

        self.verticalSpacer_2 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_4.addItem(self.verticalSpacer_2)

        QWidget.setTabOrder(self.spin_box_t1_s1, self.spin_box_t2_s1)
        QWidget.setTabOrder(self.spin_box_t2_s1, self.spin_box_t1_s2)
        QWidget.setTabOrder(self.spin_box_t1_s2, self.spin_box_t2_s2)
        QWidget.setTabOrder(self.spin_box_t2_s2, self.spin_box_t1_s3)
        QWidget.setTabOrder(self.spin_box_t1_s3, self.spin_box_t2_s3)

        self.retranslateUi(MatchWidget)

        QMetaObject.connectSlotsByName(MatchWidget)
    # setupUi

    def retranslateUi(self, MatchWidget):
        MatchWidget.setWindowTitle(QCoreApplication.translate("MatchWidget", u"Form", None))
        self.actionTest1.setText(QCoreApplication.translate("MatchWidget", u"Test1", None))
        self.actionTest2.setText(QCoreApplication.translate("MatchWidget", u"Test2", None))
        self.label_field.setText(QCoreApplication.translate("MatchWidget", u"3", None))
        self.team1.setText(QCoreApplication.translate("MatchWidget", u"Truc bidule tres long / Machine tttt encore plus", None))
        self.team2.setText(QCoreApplication.translate("MatchWidget", u"Truc bidule /  chose", None))
        self.status1.setText("")
        self.status2.setText("")
    # retranslateUi

