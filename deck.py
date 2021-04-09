import random

from card import Card


class Deck:

    card_suits = ['clubs', 'diamonds', 'hearts', 'spades']
    card_values = ['A', '2', '3', '4', '5', '6', '7', '8', '9',
                    '10', 'J', 'Q', 'K']

    def __init__(self, n_decks=1):

        self.ptr = 0 # pointer to the card on from the top
        self.cards = []
        self.n_decks = n_decks # number of decks used

        for value in Deck.card_values:
            for suit in Deck.card_suits:
                for _ in range(n_decks):
                    self.cards.append(Card(suit, value))

    def __repr__(self):
        s = "["
        for c in self.cards:
            s += str(c) + ', '
        return s[:-2] + ']'

    def get_next_card(self):
        if self.ptr < len(self.n_decks * 52):
            self.ptr += 1
            return self.cards[self.ptr - 1]
        else:
            print("The deck is empty. Please, shuffle it.")

    def shuffle(self):
        self.ptr = 0
        random.shuffle(self.cards) # in place

d = Deck(1)
print(d)
d.shuffle()
print(d)
