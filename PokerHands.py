# Poker Hand class: combinations of 5 Cards
# Define all ranks of poker hands and a way to compare rankings
from Cards import Card

class PokerHand:

    ranks = {'high card':1, 'one pair':2, 'two pair':3, 'three of a kind':4, 'straight':5,
             'flush':6, 'full house':7, 'four of a kind':8, 'straight flush':9}

    def __init__(self, cards):
        self.cards = cards
        self.index = 0

    def __iter__(self):
        return self

    def __next__(self):
        if self.index >= len(self.cards):
            raise StopIteration
        index = self.index
        self.index += 1
        return self.cards[index]

    def __str__(self):
        self.sort()
        s = ''
        for card in self.cards:
            s = s + ' ' + str(card)
        return s.strip()

    def __add__(self, other):
        return PokerHand(self.cards + other.cards)

    def sort(self):
        # insertion sort cards in a hand in ascending order
        for i in range(1, len(self.cards)):
            j = i - 1

            while j >= 0 and self.cards[i].rcmp(self.cards[j]) < 0:
                self.cards[i], self.cards[j] = self.cards[j], self.cards[i]
                j -= 1
                i -= 1

    def rcmp(self, other):
        # if the two hands differ in rank
        self_rank = PokerHand.ranks[self.get_rank()]
        other_rank = PokerHand.ranks[other.get_rank()]
        return self_rank - other_rank

    def get_value(self):
        # add up the total value of all the individual cards
        # and return the sum
        sum = 0
        for card in self.cards:
            sum += card.ranks.index(card.rank)
        return sum

    def get_rank(self):
        # start from the highest rank possible, and look to see if the hand qualifies
        # if yes, return the current rank
        # if not, move down one rank and repeat
        # return the rank in string form
        self.sort()

        if self.is_straight() and self.is_flush():
            return 'straight flush'
        elif self.is_quads():
            return 'four of a kind'
        elif self.is_boat():
            return 'full house'
        elif self.is_flush():
            return 'flush'
        elif self.is_straight():
            return 'straight'
        elif self.is_triple():
            return 'three of a kind'
        elif self.is_two_pair():
            return 'two pair'
        elif self.is_one_pair():
            return 'one pair'
        else:
            return 'high card'

    def is_quads(self):
        ranks = [card.rank for card in self.cards]
        x = ranks[0]
        if len(set(ranks)) is 2 and (ranks.count(x) is 1 or ranks.count(x) is 4):
            return True
        else:
            return False

    def is_boat(self):
        ranks = [card.rank for card in self.cards]
        x = ranks[0]
        if len(set(ranks)) is 2 and (ranks.count(x) is 2 or ranks.count(x) is 3):
            return True
        else:
            return False

    def is_flush(self):
        suits = [card.suit for card in self.cards]
        if len(set(suits)) is 1:
            return True
        else:
            return False

    def is_straight(self):
        for card in self.cards:
            index = self.cards.index(card)
            difference = Card.ranks.index(card.rank) - Card.ranks.index(self.cards[0].rank)

            if index is difference:
                continue
            else:
                return False
        return True

    def is_triple(self):
        ranks = [card.rank for card in self.cards]
        x = ranks[2]
        if len(set(ranks)) is 3 and ranks.count(x) is 3:
            return True
        else:
            return False

    def is_two_pair(self):
        ranks = [card.rank for card in self.cards]
        x = ranks[0]
        if len(set(ranks)) is 3 and (ranks.count(x) is 1 or ranks.count(x) is 2):
            return True
        else:
            return False

    def is_one_pair(self):
        ranks = [card.rank for card in self.cards]
        if len(set(ranks)) is 4:
            return True
        else:
            return False

# from Cards import Deck
# deck = Deck()
# deck.shuffle()
#
# cards = [deck.deal() for i in range(5)]
# hand = PokerHand(cards)
# print(hand)
# print(hand.get_rank())
# print(hand.get_value())
