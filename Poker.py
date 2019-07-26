# This program simulates poker hands
# No betting involved
# Purely mathematical outcomes
# Can run as many simulations as user inputs

# deal random hands to all players (2)
# simulate run out till showdown
# keep win counter for all players
# display win % at the end
# sort hands in ascending order from left to right
import sys
from PokerHands import PokerHand
from Cards import Card
from Cards import Deck

deck = Deck()

# takes user input and returns cards as a PokerHand object
def get_starting_hand(input):
    if input == 'r':
        return PokerHand([deck.deal(), deck.deal()])
    else:
        card1 = Card(input.split()[0][0], input.split()[0][1])
        card2 = Card(input.split()[1][0], input.split()[1][1])
        deck.remove(card1)
        deck.remove(card2)
        return PokerHand([card1, card2])

# combines hole cards and community cards to find the best 5-card hand
def get_best_hand(holecards, commcards):
    from itertools import combinations

    # repeatedly take 5-card combinations from the 7-card hand
    seven_cards = holecards + commcards
    seven_cards.sort()
    five_card_combos = list(combinations(seven_cards, 5))

    # since five_card_combos is a list of tuples,
    # must turn into a list of PokerHand objects
    hands = [PokerHand(list(hand_tuple)) for hand_tuple in five_card_combos]

    # insertion sort hands by rank
    for i in range(1, len(hands)):
        j = i - 1

        while j >= 0 and hands[i].rcmp(hands[j]) < 0:
            hands[i], hands[j] = hands[j], hands[i]
            j -= 1
            i -= 1

    # return the last hand because it's the best hand??
    return hands[len(hands)-1]

def display_outcome(hero, vill):
    print('~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~')
    print('Hero hole cards:', str(hero_hand))
    print('Vill hole cards:', str(vill_hand))
    print('Community cards:', str(community))

    result = hero.rcmp(vill)

    if result > 0:
        print('Hero wins with ' + hero.get_rank())
    elif result < 0:
        print('Villain wins with ' + vill.get_rank())
    else:
        print('Tie')

def simulate():
    deck.shuffle()
    try:
        # input
        hero_holecards = input('Enter hole cards for hero, or "r" for a random hand: ')
        vill_holecards = input('Enter hole cards for villain, or "r" for a random hand: ')
        num_games = int(input('Number of games: '))

        # retrieve starting hands
        for n in range(num_games):
            global hero_hand
            hero_hand = get_starting_hand(hero_holecards)
            global vill_hand
            vill_hand = get_starting_hand(vill_holecards)

            # deal community cards
            global community
            community = PokerHand([deck.deal() for _ in range(5)])

            # find the best hand
            hero_besthand = get_best_hand(hero_hand, community)
            vill_besthand = get_best_hand(vill_hand, community)

            # display the winner
            display_outcome(hero_besthand, vill_besthand)

            # reset
            deck.shuffle_reset()

    except TypeError:
        print('Just enter a damn number xD')
    except EOFError:
        sys.exit(0)

def main():
    simulate()

main()

## BUGS ##





