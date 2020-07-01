from math import sqrt

class Elo:

    def __init__(self, player1, player2, k, winner):
        self.p1 = player1
        self.p2 = player2
        self.winner = winner
        self.k = k

        self.transform_rating()
        self.expected_score()
        self.update_elo()

    def __repr__(self):
        return f"Elo({self.p1}, {self.p2}, {self.k}, {self.winner}"

    def transform_rating(self):
        self.p1t = sqrt(self.p1 / 400.0 ** 10)
        self.p2t = sqrt(self.p2 / 400.0 ** 10)

    def expected_score(self):
        self.p1e = self.p1t / (self.p1t + self.p2t)
        self.p2e = self.p2t / (self.p1t + self.p2t)

    def update_elo(self):
        if self.winner == 1:
            self.p1updated = self.p1 + self.k * (1 - self.p1e)
            self.p2updated = self.p2 + self.k * (0 - self.p2e)
        elif self.winner == 2:
            self.p1updated = self.p1 + self.k * (0 - self.p1e)
            self.p2updated = self.p2 + self.k * (1 - self.p2e)

    def get_elo(self):
        print(f"Winner: {self.winner} \n Player1: {self.p1} -> {self.p1updated} \n Player2: {self.p2} -> {self.p2updated}")
