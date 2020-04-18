
from PySide2 import QtWidgets
from PySide2.QtCore import Slot, Qt, QModelIndex, QSortFilterProxyModel, QItemSelectionModel
from PySide2.QtGui import QColor, QBrush, QPixmap
from PySide2.QtWidgets import QAbstractItemView, QHeaderView
from .ui_PlayersListWidget import Ui_PlayersListWidget
from core import Player
from .PlayersTableModel import PlayersTableModel
from .PlayersTableSortFilterProxyModel import PlayersTableSortFilterProxyModel

class PlayersListWidget(QtWidgets.QWidget, Ui_PlayersListWidget):

    def __init__(self, parent=None, players=None):
        '''
        Constructor
        '''
        super().__init__(parent)
        self.setupUi(self)
        self.set_players(players)

        # init
        self.selected_player = None

        # set connections
        self.button_del.clicked.connect(self.slot_on_player_del)
        self.button_add.clicked.connect(self.slot_on_player_add)
        self.edit_filter.setClearButtonEnabled(True)

    def set_players(self, players):
        self.players = players
        self.button_del.setEnabled(False)
        if len(players)>0:
            self.set_model()


    @Slot()
    def slot_on_cell_activated(self, selected, deselected):
        # get current index
        idx = selected.indexes()
        if len(idx) == 0:
            return
        idx = selected.indexes()[0]
        # convert to internal index (can be sorted)
        self.selected_row = idx.row()
        idx = self.filter_proxy_model.mapToSource(idx)
        idx = self.model.index(idx.row(), self.model.index_id)
        # look current player
        player = None
        for p in self.players:
            if p.id == idx.data():
                player = p
        if player:
            self.button_del.setText("Supprimer "+str(player))
            self.button_del.setEnabled(True)
            self.selected_player = player
        else:
            self.button_del.setText("Supprimer")
            self.button_del.setEnabled(False)
            self.selected_player = None


    def slot_on_player_del(self):
        p = self.selected_player
        if not p:
            return
        self.table_widget.clearSelection()
        self.model.removeRow(self.selected_row, self.selected_player)

        # set next one selected
        self.filter_proxy_model.invalidate()
        if self.selected_row == len(self.players):
            self.selected_row = self.selected_row-1
        idx = self.model.index(self.selected_row, 0)
        self.table_widget.setCurrentIndex(idx)
        self.table_widget.selectRow(idx.row())
        self.table_widget.setFocus()
        self.table_widget.repaint()

    def slot_on_player_add(self):
        # not sure what to do with the row
        row = 0
        self.edit_filter.clear()
        self.model.insertRow(row)
        idx = self.model.index(row, self.model.index_id)
        idx = self.filter_proxy_model.mapFromSource(idx)
        self.table_widget.setCurrentIndex(idx)
        self.table_widget.selectRow(idx.row())
        self.table_widget.setFocus()
        self.table_widget.repaint()


    def set_model(self):
        self.model = PlayersTableModel(self.players)
        self.table_widget.setModel(self.model)

        # filter and sorting
        self.filter_proxy_model = PlayersTableSortFilterProxyModel() #QSortFilterProxyModel()
        self.filter_proxy_model.setSourceModel(self.model)
        #self.filter_proxy_model.setDynamicSortFilter(False)
        self.filter_proxy_model.setFilterKeyColumn(self.model.index_name) #3is names
        self.filter_proxy_model.setSortLocaleAware(True)
        self.filter_proxy_model.setSortCaseSensitivity(Qt.CaseInsensitive)
        self.table_widget.setModel(self.filter_proxy_model)
        self.table_widget.setSortingEnabled(True)

        # connect
        self.model.players_changed.connect(self.slot_on_data_changed)
        self.edit_filter.textChanged.connect(self.filter_proxy_model.setFilterRegExp)

        #self.view.horizontalHeader()
        self.table_widget.setColumnHidden(self.model.index_name, True)
        self.table_widget.setColumnHidden(self.model.index_id, True)

        # column sizes
        #self.table_widget.horizontalHeader().setStretchLastSection(True
        header = self.table_widget.horizontalHeader()
        #header.setSectionResizeMode(0, QtWidgets.QHeaderView.ResizeToContents)
        #header.setSectionResizeMode(1, QtWidgets.QHeaderView.ResizeToContents)
        #header.setSectionResizeMode(2, QtWidgets.QHeaderView.ResizeToContents)
        #header.setSectionResizeMode(3, QtWidgets.QHeaderView.ResizeToContents)
        #header.setSectionResizeMode(4, QtWidgets.QHeaderView.ResizeToContents)
        #self.table_widget.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)

        # center column
        class AlignDelegate(QtWidgets.QStyledItemDelegate):
            def initStyleOption(self, option, index):
                super(AlignDelegate, self).initStyleOption(option, index)
                option.displayAlignment = Qt.AlignCenter
        delegate = AlignDelegate(self.table_widget)
        self.table_widget.setItemDelegateForColumn(2, delegate)
        self.table_widget.setItemDelegateForColumn(3, delegate)
        self.table_widget.setItemDelegateForColumn(4, delegate)
        self.table_widget.setItemDelegateForColumn(5, delegate)

        self.table_widget.setSizeAdjustPolicy(QtWidgets.QAbstractScrollArea.AdjustToContents)

        # selection policy
        self.table_widget.setSelectionModel(QItemSelectionModel(self.model))
        selection = self.table_widget.selectionModel()
        selection.selectionChanged.connect(self.slot_on_cell_activated)
        self.slot_on_data_changed()

    @Slot()
    def slot_on_data_changed(self):
        n = len(self.players)
        if n<=1:
            self.label_status.setText(f'{n} joueur')
        else:
            self.label_status.setText(f'{n} joueurs')

