

class PlayerStats:

    def __init__(self):
        self.match_count = 0
        self.match_win_count = 0
        self.set_loose_count = 0
        self.points_diff = 0

    def __str__(self):
        return f'Stats {self.match_count} {self.match_win_count} {self.set_loose_count} {self.points_diff}' # FIXME

    def add(self, stats):
        self.match_count = self.match_count + stats.match_count
        self.match_win_count = self.match_win_count + stats.match_win_count
        self.set_loose_count = self.set_loose_count + stats.set_loose_count
        self.points_diff = self.points_diff + stats.points_diff

    def reset(self):
        self.match_count = 0
        self.match_win_count = 0
        self.set_loose_count = 0
        self.points_diff = 0


