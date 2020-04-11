from .Round import Round

class Tournament:

    def __init__(self):
        self.rounds = []
        self.players = []

    def __str__(self):
        s = f'Tournament players: {len(self.players)}, rounds: {len(self.rounds)}'
        return s

    def set_players(self, players):
        self.players = players

    def new_round(self):
        r = Round(self)
        if len(self.rounds) > 0:
            pr = self.rounds[-1]
            r.fields_number = pr.fields_number
            r.set_win_point_value(pr.win_point_value)
            r.set_max_point_value(pr.max_point_value)
        self.rounds.append(r)
        r.set_players_list(self.players)
        return r