# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'RoundWidget.ui'
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


class Ui_RoundWidget(object):
    def setupUi(self, RoundWidget):
        if RoundWidget.objectName():
            RoundWidget.setObjectName(u"RoundWidget")
        RoundWidget.resize(1262, 701)
        self.gridLayout_2 = QGridLayout(RoundWidget)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.gridLayout_2.setContentsMargins(0, 0, 0, 0)
        self.toolBox = QToolBox(RoundWidget)
        self.toolBox.setObjectName(u"toolBox")
        self.page = QWidget()
        self.page.setObjectName(u"page")
        self.page.setGeometry(QRect(0, 0, 1262, 659))
        self.verticalLayout = QVBoxLayout(self.page)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.groupBox = QGroupBox(self.page)
        self.groupBox.setObjectName(u"groupBox")
        self.groupBox.setMaximumSize(QSize(16777215, 60))
        self.horizontalLayout = QHBoxLayout(self.groupBox)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.button_random_scores = QPushButton(self.groupBox)
        self.button_random_scores.setObjectName(u"button_random_scores")

        self.horizontalLayout.addWidget(self.button_random_scores)

        self.horizontalSpacer_5 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout.addItem(self.horizontalSpacer_5)

        self.button_random = QPushButton(self.groupBox)
        self.button_random.setObjectName(u"button_random")

        self.horizontalLayout.addWidget(self.button_random)

        self.horizontalSpacer_6 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout.addItem(self.horizontalSpacer_6)

        self.label_left = QLabel(self.groupBox)
        self.label_left.setObjectName(u"label_left")

        self.horizontalLayout.addWidget(self.label_left)

        self.button_next_round = QPushButton(self.groupBox)
        self.button_next_round.setObjectName(u"button_next_round")

        self.horizontalLayout.addWidget(self.button_next_round)

        self.horizontalSpacer_3 = QSpacerItem(143, 13, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout.addItem(self.horizontalSpacer_3)

        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout.addItem(self.horizontalSpacer)

        self.label_center = QLabel(self.groupBox)
        self.label_center.setObjectName(u"label_center")
        font = QFont()
        font.setPointSize(13)
        self.label_center.setFont(font)

        self.horizontalLayout.addWidget(self.label_center)

        self.horizontalSpacer_4 = QSpacerItem(142, 13, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout.addItem(self.horizontalSpacer_4)

        self.horizontalSpacer_2 = QSpacerItem(143, 13, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout.addItem(self.horizontalSpacer_2)


        self.verticalLayout.addWidget(self.groupBox)

        self.main_layout = QGridLayout()
        self.main_layout.setObjectName(u"main_layout")
        self.label = QLabel(self.page)
        self.label.setObjectName(u"label")

        self.main_layout.addWidget(self.label, 0, 0, 1, 1)


        self.verticalLayout.addLayout(self.main_layout)

        self.verticalSpacer_2 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout.addItem(self.verticalSpacer_2)

        self.toolBox.addItem(self.page, u"Tour n\u00b03")
        self.page_2 = QWidget()
        self.page_2.setObjectName(u"page_2")
        self.page_2.setGeometry(QRect(0, 0, 1262, 659))
        self.layoutWidget = QWidget(self.page_2)
        self.layoutWidget.setObjectName(u"layoutWidget")
        self.layoutWidget.setGeometry(QRect(120, 60, 381, 128))
        self.verticalLayout_2 = QVBoxLayout(self.layoutWidget)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.label_2 = QLabel(self.layoutWidget)
        self.label_2.setObjectName(u"label_2")
        font1 = QFont()
        font1.setPointSize(19)
        self.label_2.setFont(font1)

        self.horizontalLayout_2.addWidget(self.label_2)

        self.spin_fields = QSpinBox(self.layoutWidget)
        self.spin_fields.setObjectName(u"spin_fields")
        self.spin_fields.setMinimumSize(QSize(80, 0))
        self.spin_fields.setMaximumSize(QSize(80, 16777215))
        self.spin_fields.setFont(font1)
        self.spin_fields.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_2.addWidget(self.spin_fields)


        self.verticalLayout_2.addLayout(self.horizontalLayout_2)

        self.horizontalLayout_3 = QHBoxLayout()
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.label_3 = QLabel(self.layoutWidget)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setFont(font1)

        self.horizontalLayout_3.addWidget(self.label_3)

        self.spin_win_point_value = QSpinBox(self.layoutWidget)
        self.spin_win_point_value.setObjectName(u"spin_win_point_value")
        self.spin_win_point_value.setMinimumSize(QSize(80, 0))
        self.spin_win_point_value.setMaximumSize(QSize(80, 16777215))
        self.spin_win_point_value.setFont(font1)
        self.spin_win_point_value.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_3.addWidget(self.spin_win_point_value)


        self.verticalLayout_2.addLayout(self.horizontalLayout_3)

        self.horizontalLayout_7 = QHBoxLayout()
        self.horizontalLayout_7.setObjectName(u"horizontalLayout_7")
        self.label_7 = QLabel(self.layoutWidget)
        self.label_7.setObjectName(u"label_7")
        self.label_7.setFont(font1)

        self.horizontalLayout_7.addWidget(self.label_7)

        self.spin_max_point_value = QSpinBox(self.layoutWidget)
        self.spin_max_point_value.setObjectName(u"spin_max_point_value")
        self.spin_max_point_value.setMinimumSize(QSize(80, 0))
        self.spin_max_point_value.setMaximumSize(QSize(80, 16777215))
        self.spin_max_point_value.setFont(font1)
        self.spin_max_point_value.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_7.addWidget(self.spin_max_point_value)


        self.verticalLayout_2.addLayout(self.horizontalLayout_7)

        self.toolBox.addItem(self.page_2, u"Options")

        self.gridLayout_2.addWidget(self.toolBox, 0, 0, 1, 1)


        self.retranslateUi(RoundWidget)

        self.toolBox.setCurrentIndex(0)
        self.toolBox.layout().setSpacing(0)


        QMetaObject.connectSlotsByName(RoundWidget)
    # setupUi

    def retranslateUi(self, RoundWidget):
        RoundWidget.setWindowTitle(QCoreApplication.translate("RoundWidget", u"Form", None))
        self.groupBox.setTitle("")
        self.button_random_scores.setText(QCoreApplication.translate("RoundWidget", u"rnd", None))
        self.button_random.setText(QCoreApplication.translate("RoundWidget", u"Go !", None))
        self.label_left.setText("")
        self.button_next_round.setText(QCoreApplication.translate("RoundWidget", u"Prochain tour", None))
        self.label_center.setText(QCoreApplication.translate("RoundWidget", u"14 matches - 5 en cours - 4 termin\u00e9s", None))
        self.label.setText(QCoreApplication.translate("RoundWidget", u"TextLabel", None))
        self.toolBox.setItemText(self.toolBox.indexOf(self.page), QCoreApplication.translate("RoundWidget", u"Tour n\u00b03", None))
        self.label_2.setText(QCoreApplication.translate("RoundWidget", u"Nombre de terrains :", None))
        self.label_3.setText(QCoreApplication.translate("RoundWidget", u"Score \u00e0 atteindre par set :", None))
        self.label_7.setText(QCoreApplication.translate("RoundWidget", u"Score maximum :", None))
        self.toolBox.setItemText(self.toolBox.indexOf(self.page_2), QCoreApplication.translate("RoundWidget", u"Options", None))
    # retranslateUi

