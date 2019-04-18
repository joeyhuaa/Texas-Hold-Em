# This program simulates poker hands
# No betting involved
# Purely mathematical outcomes
# Can run as many simulations as user inputs

from Cards import Deck

# deal random hands to all players (2)
# simulate run out till showdown
# keep win counter for all players
# display win % at the end
# sort hands in ascending order from left to right

def outcome(hands=[]):


def simulate():

    # input
    try:
        num_games = input('Number of games: ')

        # deal hands
        for i in range(1,num_games+1):

            # shuffle deck
            deck = Deck()
            deck.shuffle()

            # deal hands and community cards
            hero_hand = [deck.deal(), deck.deal()]
            vill_hand = [deck.deal(), deck.deal()]
            community = [deck.deal(), deck.deal(), deck.deal(), deck.deal(), deck.deal()]

            # form the best possible 5-card hands for each player
            # linear search for repetitions
            for


    except TypeError:
        print('Just enter a goddamn number dude.')


