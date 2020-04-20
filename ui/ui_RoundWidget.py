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
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.groupBox = QGroupBox(self.page)
        self.groupBox.setObjectName(u"groupBox")
        self.groupBox.setMaximumSize(QSize(16777215, 60))
        self.groupBox.setFlat(False)
        self.gridLayout_4 = QGridLayout(self.groupBox)
        self.gridLayout_4.setObjectName(u"gridLayout_4")
        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.button_random = QPushButton(self.groupBox)
        self.button_random.setObjectName(u"button_random")
        icon = QIcon()
        icon.addFile(u":/icons/128x128/actions/roll-2.png", QSize(), QIcon.Normal, QIcon.On)
        self.button_random.setIcon(icon)
        self.button_random.setIconSize(QSize(25, 25))

        self.horizontalLayout.addWidget(self.button_random)

        self.button_swiss = QPushButton(self.groupBox)
        self.button_swiss.setObjectName(u"button_swiss")
        icon1 = QIcon()
        icon1.addFile(u":/css/60px-Nuvola_Swiss_flag.svg.png", QSize(), QIcon.Normal, QIcon.On)
        self.button_swiss.setIcon(icon1)
        self.button_swiss.setIconSize(QSize(25, 25))

        self.horizontalLayout.addWidget(self.button_swiss)

        self.button_random_scores = QPushButton(self.groupBox)
        self.button_random_scores.setObjectName(u"button_random_scores")

        self.horizontalLayout.addWidget(self.button_random_scores)

        self.horizontalSpacer_3 = QSpacerItem(143, 13, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout.addItem(self.horizontalSpacer_3)

        self.label_players_2 = QLabel(self.groupBox)
        self.label_players_2.setObjectName(u"label_players_2")
        font = QFont()
        font.setPointSize(13)
        self.label_players_2.setFont(font)

        self.horizontalLayout.addWidget(self.label_players_2)

        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout.addItem(self.horizontalSpacer)

        self.label_center = QLabel(self.groupBox)
        self.label_center.setObjectName(u"label_center")
        self.label_center.setFont(font)

        self.horizontalLayout.addWidget(self.label_center)

        self.horizontalSpacer_4 = QSpacerItem(142, 13, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout.addItem(self.horizontalSpacer_4)

        self.button_previous_round = QPushButton(self.groupBox)
        self.button_previous_round.setObjectName(u"button_previous_round")
        icon2 = QIcon()
        icon2.addFile(u":/icons/128x128/actions/go-previous-9.png", QSize(), QIcon.Normal, QIcon.On)
        self.button_previous_round.setIcon(icon2)
        self.button_previous_round.setIconSize(QSize(25, 25))

        self.horizontalLayout.addWidget(self.button_previous_round)

        self.button_next_round = QPushButton(self.groupBox)
        self.button_next_round.setObjectName(u"button_next_round")
        icon3 = QIcon()
        icon3.addFile(u":/icons/128x128/actions/go-next-9.png", QSize(), QIcon.Normal, QIcon.On)
        self.button_next_round.setIcon(icon3)
        self.button_next_round.setIconSize(QSize(25, 25))

        self.horizontalLayout.addWidget(self.button_next_round)


        self.gridLayout_4.addLayout(self.horizontalLayout, 0, 0, 1, 1)

        self.label_left = QLabel(self.groupBox)
        self.label_left.setObjectName(u"label_left")

        self.gridLayout_4.addWidget(self.label_left, 0, 1, 1, 1)


        self.verticalLayout.addWidget(self.groupBox)

        self.main_layout = QGridLayout()
        self.main_layout.setSpacing(0)
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
        self.gridLayout_3 = QGridLayout(self.page_2)
        self.gridLayout_3.setObjectName(u"gridLayout_3")
        self.horizontalSpacer_8 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.gridLayout_3.addItem(self.horizontalSpacer_8, 0, 0, 1, 1)

        self.gridLayout = QGridLayout()
        self.gridLayout.setObjectName(u"gridLayout")
        self.verticalLayout_2 = QVBoxLayout()
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.label_2 = QLabel(self.page_2)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setFont(font)

        self.horizontalLayout_2.addWidget(self.label_2)

        self.spin_fields = QSpinBox(self.page_2)
        self.spin_fields.setObjectName(u"spin_fields")
        self.spin_fields.setMinimumSize(QSize(80, 0))
        self.spin_fields.setMaximumSize(QSize(80, 16777215))
        self.spin_fields.setFont(font)
        self.spin_fields.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_2.addWidget(self.spin_fields)


        self.verticalLayout_2.addLayout(self.horizontalLayout_2)

        self.horizontalLayout_3 = QHBoxLayout()
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.label_3 = QLabel(self.page_2)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setFont(font)

        self.horizontalLayout_3.addWidget(self.label_3)

        self.spin_win_point_value = QSpinBox(self.page_2)
        self.spin_win_point_value.setObjectName(u"spin_win_point_value")
        self.spin_win_point_value.setMinimumSize(QSize(80, 0))
        self.spin_win_point_value.setMaximumSize(QSize(80, 16777215))
        self.spin_win_point_value.setFont(font)
        self.spin_win_point_value.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_3.addWidget(self.spin_win_point_value)


        self.verticalLayout_2.addLayout(self.horizontalLayout_3)

        self.horizontalLayout_7 = QHBoxLayout()
        self.horizontalLayout_7.setObjectName(u"horizontalLayout_7")
        self.label_7 = QLabel(self.page_2)
        self.label_7.setObjectName(u"label_7")
        self.label_7.setFont(font)

        self.horizontalLayout_7.addWidget(self.label_7)

        self.spin_max_point_value = QSpinBox(self.page_2)
        self.spin_max_point_value.setObjectName(u"spin_max_point_value")
        self.spin_max_point_value.setMinimumSize(QSize(80, 0))
        self.spin_max_point_value.setMaximumSize(QSize(80, 16777215))
        self.spin_max_point_value.setFont(font)
        self.spin_max_point_value.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_7.addWidget(self.spin_max_point_value)


        self.verticalLayout_2.addLayout(self.horizontalLayout_7)


        self.gridLayout.addLayout(self.verticalLayout_2, 4, 0, 1, 3)

        self.verticalSpacer_5 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.gridLayout.addItem(self.verticalSpacer_5, 6, 2, 1, 1)

        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.gridLayout.addItem(self.verticalSpacer, 0, 2, 1, 1)

        self.verticalSpacer_7 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.gridLayout.addItem(self.verticalSpacer_7, 3, 1, 1, 1)

        self.label_players = QLabel(self.page_2)
        self.label_players.setObjectName(u"label_players")
        self.label_players.setFont(font)
        self.label_players.setAlignment(Qt.AlignCenter)

        self.gridLayout.addWidget(self.label_players, 2, 1, 1, 1)

        self.label_options = QLabel(self.page_2)
        self.label_options.setObjectName(u"label_options")
        self.label_options.setFont(font)
        self.label_options.setAlignment(Qt.AlignCenter)

        self.gridLayout.addWidget(self.label_options, 0, 1, 1, 1)

        self.verticalSpacer_6 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.gridLayout.addItem(self.verticalSpacer_6, 8, 1, 1, 1)

        self.verticalSpacer_3 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.gridLayout.addItem(self.verticalSpacer_3, 7, 2, 1, 1)

        self.verticalSpacer_4 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.gridLayout.addItem(self.verticalSpacer_4, 7, 0, 1, 1)

        self.verticalSpacer_8 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.gridLayout.addItem(self.verticalSpacer_8, 1, 1, 1, 1)


        self.gridLayout_3.addLayout(self.gridLayout, 0, 1, 1, 1)

        self.verticalLayout_3 = QVBoxLayout()
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.horizontalLayout_4 = QHBoxLayout()
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.label_5 = QLabel(self.page_2)
        self.label_5.setObjectName(u"label_5")

        self.horizontalLayout_4.addWidget(self.label_5)

        self.edit_filter = QLineEdit(self.page_2)
        self.edit_filter.setObjectName(u"edit_filter")
        self.edit_filter.setMinimumSize(QSize(200, 0))
        self.edit_filter.setMaximumSize(QSize(200, 16777215))

        self.horizontalLayout_4.addWidget(self.edit_filter)

        self.horizontalSpacer_5 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_4.addItem(self.horizontalSpacer_5)


        self.verticalLayout_3.addLayout(self.horizontalLayout_4)

        self.table_widget = QTableView(self.page_2)
        self.table_widget.setObjectName(u"table_widget")
        self.table_widget.setSelectionMode(QAbstractItemView.NoSelection)
        self.table_widget.setSelectionBehavior(QAbstractItemView.SelectRows)

        self.verticalLayout_3.addWidget(self.table_widget)


        self.gridLayout_3.addLayout(self.verticalLayout_3, 0, 2, 1, 1)

        self.horizontalSpacer_7 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.gridLayout_3.addItem(self.horizontalSpacer_7, 0, 4, 1, 1)

        self.horizontalSpacer_9 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.gridLayout_3.addItem(self.horizontalSpacer_9, 0, 3, 1, 1)

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
#if QT_CONFIG(tooltip)
        self.button_random.setToolTip(QCoreApplication.translate("RoundWidget", u"G\u00e9n\u00e9rer les matchs au hasard", None))
#endif // QT_CONFIG(tooltip)
        self.button_random.setText("")
#if QT_CONFIG(shortcut)
        self.button_random.setShortcut("")
#endif // QT_CONFIG(shortcut)
#if QT_CONFIG(tooltip)
        self.button_swiss.setToolTip(QCoreApplication.translate("RoundWidget", u"G\u00e9n\u00e9rer les matchs en \"ronde Suisse\"", None))
#endif // QT_CONFIG(tooltip)
#if QT_CONFIG(shortcut)
        self.button_swiss.setShortcut("")
#endif // QT_CONFIG(shortcut)
        self.button_random_scores.setText(QCoreApplication.translate("RoundWidget", u"scores rnd", None))
        self.label_players_2.setText(QCoreApplication.translate("RoundWidget", u"Participants 24/30", None))
        self.label_center.setText(QCoreApplication.translate("RoundWidget", u"14 matches - 5 en cours - 4 termin\u00e9s", None))
        self.button_previous_round.setText(QCoreApplication.translate("RoundWidget", u"Tour pr\u00e9c\u00e9dent", None))
#if QT_CONFIG(shortcut)
        self.button_previous_round.setShortcut("")
#endif // QT_CONFIG(shortcut)
        self.button_next_round.setText(QCoreApplication.translate("RoundWidget", u"Tour suivant", None))
#if QT_CONFIG(shortcut)
        self.button_next_round.setShortcut("")
#endif // QT_CONFIG(shortcut)
        self.label_left.setText("")
        self.label.setText(QCoreApplication.translate("RoundWidget", u"TextLabel", None))
        self.toolBox.setItemText(self.toolBox.indexOf(self.page), QCoreApplication.translate("RoundWidget", u"Tour n\u00b03", None))
        self.label_2.setText(QCoreApplication.translate("RoundWidget", u"Nombre de terrains :", None))
        self.label_3.setText(QCoreApplication.translate("RoundWidget", u"Score \u00e0 atteindre par set :", None))
        self.label_7.setText(QCoreApplication.translate("RoundWidget", u"Score maximum :", None))
        self.label_players.setText(QCoreApplication.translate("RoundWidget", u"Nombre de participants : 37/42", None))
        self.label_options.setText(QCoreApplication.translate("RoundWidget", u"Options du tour n\u00b03", None))
        self.label_5.setText(QCoreApplication.translate("RoundWidget", u"Filtre :", None))
        self.toolBox.setItemText(self.toolBox.indexOf(self.page_2), QCoreApplication.translate("RoundWidget", u"Options", None))
    # retranslateUi

