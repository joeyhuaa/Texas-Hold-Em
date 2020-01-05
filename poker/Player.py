from PokerHands import PokerHand

class Player:
    def __init__(self, hole_cards_list):
        self.stack = 500
        self.hole_cards = PokerHand(hole_cards_list)

    def bet(self, amount):
        if amount <= self.stack:
            self.stack -= amount
            print('Raise ' + amount)
        else:
            print('You cannot bet more than you have.')

    def call(self, amount):
        self.stack -= amount
        print('Call ' + amount)







