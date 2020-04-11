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
        self.lineEdit = QLineEdit(PlayersListWidget)
        self.lineEdit.setObjectName(u"lineEdit")
        self.lineEdit.setMinimumSize(QSize(200, 0))
        self.lineEdit.setMaximumSize(QSize(200, 16777215))

        self.horizontalLayout.addWidget(self.lineEdit)

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

        self.table_widget = QTableWidget(PlayersListWidget)
        if (self.table_widget.columnCount() < 8):
            self.table_widget.setColumnCount(8)
        __qtablewidgetitem = QTableWidgetItem()
        self.table_widget.setHorizontalHeaderItem(0, __qtablewidgetitem)
        __qtablewidgetitem1 = QTableWidgetItem()
        self.table_widget.setHorizontalHeaderItem(1, __qtablewidgetitem1)
        __qtablewidgetitem2 = QTableWidgetItem()
        self.table_widget.setHorizontalHeaderItem(2, __qtablewidgetitem2)
        __qtablewidgetitem3 = QTableWidgetItem()
        self.table_widget.setHorizontalHeaderItem(3, __qtablewidgetitem3)
        __qtablewidgetitem4 = QTableWidgetItem()
        self.table_widget.setHorizontalHeaderItem(4, __qtablewidgetitem4)
        __qtablewidgetitem5 = QTableWidgetItem()
        self.table_widget.setHorizontalHeaderItem(5, __qtablewidgetitem5)
        __qtablewidgetitem6 = QTableWidgetItem()
        self.table_widget.setHorizontalHeaderItem(6, __qtablewidgetitem6)
        __qtablewidgetitem7 = QTableWidgetItem()
        self.table_widget.setHorizontalHeaderItem(7, __qtablewidgetitem7)
        if (self.table_widget.rowCount() < 4):
            self.table_widget.setRowCount(4)
        __qtablewidgetitem8 = QTableWidgetItem()
        self.table_widget.setVerticalHeaderItem(0, __qtablewidgetitem8)
        __qtablewidgetitem9 = QTableWidgetItem()
        self.table_widget.setVerticalHeaderItem(1, __qtablewidgetitem9)
        __qtablewidgetitem10 = QTableWidgetItem()
        self.table_widget.setVerticalHeaderItem(2, __qtablewidgetitem10)
        __qtablewidgetitem11 = QTableWidgetItem()
        self.table_widget.setVerticalHeaderItem(3, __qtablewidgetitem11)
        self.table_widget.setObjectName(u"table_widget")
        self.table_widget.setAlternatingRowColors(True)
        self.table_widget.setSelectionMode(QAbstractItemView.SingleSelection)
        self.table_widget.setSelectionBehavior(QAbstractItemView.SelectItems)
        self.table_widget.setSortingEnabled(True)
        self.table_widget.verticalHeader().setVisible(False)

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
        ___qtablewidgetitem = self.table_widget.horizontalHeaderItem(0)
        ___qtablewidgetitem.setText(QCoreApplication.translate("PlayersListWidget", u"Nom", None));
        ___qtablewidgetitem1 = self.table_widget.horizontalHeaderItem(1)
        ___qtablewidgetitem1.setText(QCoreApplication.translate("PlayersListWidget", u"Pr\u00e9nom", None));
        ___qtablewidgetitem2 = self.table_widget.horizontalHeaderItem(2)
        ___qtablewidgetitem2.setText(QCoreApplication.translate("PlayersListWidget", u"Classement", None));
        ___qtablewidgetitem3 = self.table_widget.horizontalHeaderItem(3)
        ___qtablewidgetitem3.setText(QCoreApplication.translate("PlayersListWidget", u"Matchs jou\u00e9s", None));
        ___qtablewidgetitem4 = self.table_widget.horizontalHeaderItem(4)
        ___qtablewidgetitem4.setText(QCoreApplication.translate("PlayersListWidget", u"Matchs gagn\u00e9s", None));
        ___qtablewidgetitem5 = self.table_widget.horizontalHeaderItem(5)
        ___qtablewidgetitem5.setText(QCoreApplication.translate("PlayersListWidget", u"Set perdus", None));
        ___qtablewidgetitem6 = self.table_widget.horizontalHeaderItem(6)
        ___qtablewidgetitem6.setText(QCoreApplication.translate("PlayersListWidget", u"Points", None));
        ___qtablewidgetitem7 = self.table_widget.horizontalHeaderItem(7)
        ___qtablewidgetitem7.setText(QCoreApplication.translate("PlayersListWidget", u"player index", None));
        ___qtablewidgetitem8 = self.table_widget.verticalHeaderItem(0)
        ___qtablewidgetitem8.setText(QCoreApplication.translate("PlayersListWidget", u"1", None));
        ___qtablewidgetitem9 = self.table_widget.verticalHeaderItem(1)
        ___qtablewidgetitem9.setText(QCoreApplication.translate("PlayersListWidget", u"2", None));
        ___qtablewidgetitem10 = self.table_widget.verticalHeaderItem(2)
        ___qtablewidgetitem10.setText(QCoreApplication.translate("PlayersListWidget", u"3", None));
        ___qtablewidgetitem11 = self.table_widget.verticalHeaderItem(3)
        ___qtablewidgetitem11.setText(QCoreApplication.translate("PlayersListWidget", u"4", None));
    # retranslateUi

