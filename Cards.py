#
# This module has classes for a set of playing cards and a deck of cards
#
# the Card class
# methods:
#	__init__: generate a card with given suit rank
#	__str__: print the given card
#   cmp: compare 2 cards, return 1, 0, -1 as appropriate
#			order is S, H, D, C (suits) and A, K, Q, J, 10, ... (ranks)
#	rcmp: compare the rank of 2 cards, return 1, 0, -1 as appropriate
#	scmp: compare the suit of 2 cards, return 1, 0, -1 as appropriate
#
class Card:
    # first, the suits and ranks, in order
    # note the order is important as it is used to compare
    suits = ["c", "d", "h", "s"]
    ranks = ["2", "3", "4", "5", "6", "7", "8",
             "9", "T", "J", "Q", "K", "A"]

    # create a card; default is AS
    def __init__(self, rank="A", suit="s"):
        self.rank = rank
        self.suit = suit

    # generate a string representing the card
    def __str__(self):
        return self.rank + self.suit

    # compare suits
    def scmp(self, c):
        # get the number of the suits
        # for each card; the sign of the
        # difference is the result
        ss = Card.suits.index(self.suit)
        cs = Card.suits.index(c.suit)
        return ss - cs

    # compare ranks
    def rcmp(self, c):
        # get the number of the ranks
        # for each card; the sign of the
        # difference is the result
        sr = Card.ranks.index(self.rank)
        cr = Card.ranks.index(c.rank)
        return sr - cr

    # compare, taking rank and suit into account
    def cmp(self, c):
        # test suits
        sv = self.scmp(c)
        if sv != 0:
            return sv

        # test ranks; if you get here, whatever
        # this returns is it!
        return self.rcmp(c)


#
# the Deck class
# represent it as a list of cards
# methods:
#	__init__: initialize deck with 52 cards in order (low to high)
#	__str__: generate a string of cards with blanks between them
#   shuffle: shuffle the deck
# requires:
#	class Cards (above)
#	import random (for the shuffling)
#
class Deck:

    # create a deck of cards
    def __init__(self):
        self.cards = [Card(r,s) for s in Card.suits for r in Card.ranks]

    # print the cards in the deck separated by blanks
    # note we have a leading blank so we strip it
    def __str__(self):
        s = ''
        for c in self.cards:
            s = s + ' ' + str(c)
        return s.strip()

    # get number of cards remaining in the deck
    def __len__(self):
        return len(self.cards)

    # shuffle the deck using the random module
    def shuffle(self):
        import random as rng
        rng.shuffle(self.cards)

    # deal a random card and remove it from deck
    def deal(self):
        return self.cards.pop(0)
