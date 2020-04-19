
from PySide2 import QtWidgets
from PySide2.QtCore import Slot, Signal, QSize
from PySide2.QtGui import QPixmap, QPalette, QColor, QFont
from PySide2.QtWidgets import QAction
from .ui_MatchWidget import Ui_MatchWidget
from ui import TeamWidget
import platform

class MatchWidget(QtWidgets.QWidget, Ui_MatchWidget):

    match_has_changed = Signal()
    match_status_has_changed = Signal()

    def __init__(self, parent=None):
        '''
        Constructor
        '''
        super().__init__(parent)
        self.setupUi(self)

        self.adjust_font_size_according_platform()

        l11 = lambda value: self.spin_set_changed(value, 1, 1)
        l12 = lambda value: self.spin_set_changed(value, 1, 2)
        l13 = lambda value: self.spin_set_changed(value, 1, 3)
        l21 = lambda value: self.spin_set_changed(value, 2, 1)
        l22 = lambda value: self.spin_set_changed(value, 2, 2)
        l23 = lambda value: self.spin_set_changed(value, 2, 3)
        self.spin_box_t1_s1.valueChanged.connect(l11)
        self.spin_box_t1_s2.valueChanged.connect(l12)
        self.spin_box_t1_s3.valueChanged.connect(l13)
        self.spin_box_t2_s1.valueChanged.connect(l21)
        self.spin_box_t2_s2.valueChanged.connect(l22)
        self.spin_box_t2_s3.valueChanged.connect(l23)

        self.match_has_changed.connect(self.match_changed)

    def set_match(self, match):
        '''
        Change the current match
        '''
        self.match = match
        m = self.match.max_point_value
        self.spin_box_t1_s1.setMaximum(m)
        self.spin_box_t1_s2.setMaximum(m)
        self.spin_box_t1_s3.setMaximum(m)
        self.spin_box_t2_s1.setMaximum(m)
        self.spin_box_t2_s2.setMaximum(m)
        self.spin_box_t2_s3.setMaximum(m)
        match.round.round_termination_changed.connect(self.slot_on_round_termination_changed)
        self.match_changed()
        self.repaint()

    def get_spin_box(self,team, set):
        '''
        return the spin box according to the team number and set number
        '''
        if team == 1:
            if set == 1:
                return self.spin_box_t1_s1
            if set == 2:
                return self.spin_box_t1_s2
            if set == 3:
                return self.spin_box_t1_s3
        if set == 1:
            return self.spin_box_t2_s1
        if set == 2:
            return self.spin_box_t2_s2
        if set == 3:
            return self.spin_box_t2_s3

    @Slot()
    def spin_set_changed(self, value, team, set):
        '''
        Slot: a spin changed its value
        '''
        s = self.match.set(set).score(team)
        # prevent same change
        if value != s:
            self.match.set(set).set_score(team, value)

    @Slot()
    def slot_on_set_status_changed(self):
        '''
        Slot: the status of a set has changed
        '''
        m = self.match
        # update set color
        self.update_spin_color()
        # update spin enabled/disabled
        if m.set1.status == -1 or m.set1.status == 0:
            self.get_spin_box(1, 2).setEnabled(False)
            self.get_spin_box(2, 2).setEnabled(False)
            self.get_spin_box(1, 3).setEnabled(False)
            self.get_spin_box(2, 3).setEnabled(False)
            return
        self.get_spin_box(1, 2).setEnabled(True)
        self.get_spin_box(2, 2).setEnabled(True)
        if m.set2.status == -1 or m.set2.status == 0:
            self.get_spin_box(1, 3).setEnabled(False)
            self.get_spin_box(2, 3).setEnabled(False)
            return
        if m.set1.status == m.set2.status:
            self.get_spin_box(1, 3).setEnabled(False)
            self.get_spin_box(2, 3).setEnabled(False)
            return
        self.get_spin_box(1, 3).setEnabled(True)
        self.get_spin_box(2, 3).setEnabled(True)


    def update_spin_color(self):
        '''
        Slot: update the spin color if the set is win
        '''
        m = self.match
        self.set_spin_box_color(m.set1.status, 1)
        self.set_spin_box_color(m.set2.status, 2)
        self.set_spin_box_color(m.set3.status, 3)


    @Slot()
    def slot_on_match_status_changed(self):
        '''
        Slot: update when the match status has changed
        '''
        status = self.match.status
        self.match_status_has_changed.emit()
        s = 25
        if not self.match.is_valid():
            self.status1.setMaximumSize(QSize(s, s))
            self.status1.setPixmap(QPixmap(u":/icons/128x128/status/dialog-error-7.png"))
            self.status1.setVisible(True)
            self.status2.setVisible(False)
            return
        if status != 0:
            self.status1.setMaximumSize(QSize(s, s))
            self.status2.setMaximumSize(QSize(s, s))
            if status == 1:
                self.status2.setPixmap(QPixmap(u":/icons/128x128/emotes/face-angry.png"))
                self.status1.setPixmap(QPixmap(u":/icons/128x128/emotes/face-wink-4.png"))
            else:
                self.status1.setPixmap(QPixmap(u":/icons/128x128/emotes/face-angry.png"))
                self.status2.setPixmap(QPixmap(u":/icons/128x128/emotes/face-wink-4.png"))
            self.status1.setVisible(True)
            self.status2.setVisible(True)
            # update Field
            self.label_field.setEnabled(False)
        else:
            self.status1.setMaximumSize(QSize(s, s))
            self.status1.setPixmap(QPixmap(u":/icons/olympic-40778_1280.png"))
            self.status1.setVisible(True)
            self.status2.setVisible(False)
            self.label_field.setEnabled(True)

    @Slot()
    def match_changed(self):
        '''
        Slot: the match has changed, update everything
        '''

        # update team, field
        self.update_teams()
        self.update_match_field()

        # set the signal
        self.match.set1.set_status_changed.connect(self.slot_on_set_status_changed)
        self.match.set2.set_status_changed.connect(self.slot_on_set_status_changed)
        self.match.set3.set_status_changed.connect(self.slot_on_set_status_changed)
        self.match.match_status_changed.connect(self.slot_on_match_status_changed)

        # set the context menu
        self.update_context_menu()
        self.match.match_field_changed.connect(self.update_context_menu)

        # update scores
        m = self.match
        for t in range(1,3):
            for s in range(1,4):
                self.get_spin_box(t,s).setValue(m.set(s).score(t))

        # prevent change if terminated
        if self.match.round.terminated:
            self.lock()

        # signal / slot
        self.slot_on_set_status_changed()
        self.slot_on_match_status_changed()


    def set_spin_box_color(self, winner, set):
        if winner == 0 or winner == -1:
            self.set_spin_box_color_with_color(1, set, 'white')
            self.set_spin_box_color_with_color(2, set, 'white')
            return
        looser = 1
        if winner == 1:
            looser = 2
        self.set_spin_box_color_with_color(winner, set, 'lightgreen')
        self.set_spin_box_color_with_color(looser, set, 'white')


    def set_spin_box_color_with_color(self, team, set, color):
        w = self.get_spin_box(team, set)
        pal = w.palette()
        pal.setColor(QPalette.Base, QColor(color))
        w.setPalette(pal)


    def adjust_font_size_according_platform(self):
        self.platform = platform.platform()
        if not 'Darwin' in self.platform:
            return
        font = QFont()
        font.setPointSize(13)
        self.team1.setFont(font)
        self.team2.setFont(font)
        w = 270
        self.team1.setMinimumSize(QSize(w, 0))
        self.team1.setMaximumSize(QSize(w, 16777215))
        self.team1.setMinimumSize(QSize(w, 0))
        self.team1.setMaximumSize(QSize(w, 16777215))
        font = QFont()
        font.setPointSize(13)
        for i in range(1,4):
            for j in range(1,3):
                self.get_spin_box(j,i).setFont(font)
                self.get_spin_box(j,i).setMinimumSize(QSize(50, 30))


    def update_match_field(self):
        font = self.label_field.font()
        if self.match.field != 0:
            font.setPointSize(29)
            self.label_field.setFont(font)
            self.label_field.setText(str(self.match.field))
            if self.match.status == 1 or self.match.status == 2:
                self.label_field.setEnabled(False)
            else:
                self.label_field.setEnabled(True)
        else:
            font.setPointSize(10)
            self.label_field.setFont(font)
            self.label_field.setText("Attente \nterrain")
            self.label_field.setEnabled(True)

    def update_context_menu(self):
        # this function is needed to create the lambda with both parameters
        def create_lambda(f):
            return lambda checked: self.match.swap_field(f)

        # delete old context menu
        for a in self.label_field.actions():
            self.label_field.removeAction(a)

        # create new context menu
        a = QAction(self)
        a.setText(f"Pas de terrain")
        l = create_lambda(0)
        a.triggered.connect(l)
        self.label_field.addAction(a)
        for f in range(1,self.match.round.fields_number+1):
            if self.match.field == f:
                continue
            a = QAction(self)
            a.setText(f"Terrain n°{f}")
            l = create_lambda(f)
            a.triggered.connect(l)
            self.label_field.addAction(a)

        # update
        self.update_match_field()

    def update_teams(self):
        # remove previous widgets
        self.verticalLayout.removeWidget(self.team1)
        self.verticalLayout.removeWidget(self.team2)
        self.team1.setParent(None)
        self.team2.setParent(None)
        del self.team1
        del self.team2
        # add team widgets
        self.team1 = TeamWidget.TeamWidget(self, self.match.team1)
        self.verticalLayout.addWidget(self.team1)
        self.team2 = TeamWidget.TeamWidget(self, self.match.team2)
        self.verticalLayout.addWidget(self.team2)

    @Slot()
    def slot_on_round_termination_changed(self):
        f = True
        if self.match.round.terminated:
            f = False
        for team in range(1,3):
            for set in range(1,4):
                s = self.get_spin_box(team,set)
                s.setEnabled(f)

