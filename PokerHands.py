# Poker Hand class: combinations of 5 Cards
# Define all ranks of poker hands and a way to compare rankings

from Cards import Card
from Cards import Deck
deck = Deck()
deck.shuffle()

class PokerHand:

    ranks = ['high card', 'pair', 'two pair', 'triple', 'straight',
             'flush', 'full house', 'quads', 'straight flush']

    def __init__(self):
        self.cards = [deck.deal(),deck.deal(),deck.deal(),deck.deal(),deck.deal()]
        self.rank = None

    def __str__(self):
        s = ''
        for c in self.cards:
            s = s + ' ' + str(c)
        return s.strip()

    def cmp(self, h):
        sr = PokerHand.ranks.index(self.rank)
        hr = PokerHand.ranks.index(h.rank)
        return sr - hr

    def sort(self):
        # insertion sort
        for i in range(1, len(self.cards)-1):

            key = self.cards[i].rank
            j = i - 1

            while j >= 0 and key < self.cards[j].rank:
                self.cards[j+1] = self.cards[j]
                j -= 1
            self.cards[j+1] = key

    def straight(self):
        for card in self.cards:
            index = self.cards.index(card)
            difference = Card.ranks.index(card.rank) - Card.ranks.index(self.cards[0].rank)

            if index is difference:
                continue
            else:
                return False
        return True

    def flush(self):
        for card in self.cards:
            if card.suit is self.cards[0].suit:
                continue
            else:
                return False
        return True

    def boat(self):
        trip_counter = 0
        pair_counter = 0


    #def getrank(self):
        # start from the highest rank possible, and look to see if the hand qualifies
        # if not, move down one rank and repeat
        # if yes, return the current rank

        # loop through ranks, starting from straight flush, descending
        # for r in range(8,0,-1):
        #     # loop through the cards in the hand
        #     for c in range(0,len(self.cards)-1):
