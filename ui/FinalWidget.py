from PySide2 import QtWidgets
from .ui_FinalWidget import Ui_FinalWidget
from operator import attrgetter

class FinalWidget(QtWidgets.QWidget, Ui_FinalWidget):

    def __init__(self, parent, tournament, container):
        super().__init__(parent)
        self.setupUi(self)

        self.tournament = tournament
        self.parent = parent
        self.container = container

        #for r in self.tournament.rounds:
        #    r.round_termination_changed.connect(self.slot_update)
        #    r.round_started_changed.connect(self.slot_update)
        #    r.round_waiting_list_changed.connect(self.slot_update)

        self.button_remove.clicked.connect(self.slot_on_remove)
        self.slot_update()

    def slot_update(self):
        players = self.tournament.players
        pl = sorted(players,
                    key=attrgetter('stats.match_win_count',
                                   'stats.set_diff',
                                   'stats.points_diff'),
                    reverse=True)
        for p in players:
            p.player_name_changed.connect(self.slot_update)
            #p.player_stats_changed.connect(self.slot_update)
        self.set_player_stats(pl[0], self.label_stats1, self.label_player1)
        self.set_player_stats(pl[1], self.label_stats2, self.label_player2)
        self.set_player_stats(pl[2], self.label_stats3, self.label_player3)
        nbp = len(players)
        nbr = len(self.tournament.rounds)
        s = f'Tournoi terminé ! \n{nbp} joueurs \n{nbr} tours'
        self.label_tournament.setText(s)

    def set_player_stats(self, player, widget, label):
        pm = player.stats.match_count
        wm = player.stats.match_win_count
        ws = player.stats.set_diff
        wp = player.stats.points_diff

        s = f'{pm} matches joués\n{wm} matchs gagnés\n+{ws} sets\n+{wp} points'
        widget.setText(s)
        label.setText(str(player))

    def slot_on_remove(self):
        self.parent.remove_final(self.container)