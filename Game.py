class Game:
    # keeps track of the state of the game, pot size, street

    def __init__(self, players):
        self.street = 0     # 0 is pre-flop, 1 is flop, etc.
        self.pot = 3
        self.round = 0
        self.outcomes = []
        self.players = players
        # self.dealer =

    def new_round(self):
        self.street = 0
        self.pot = 3
        self.round += 1


