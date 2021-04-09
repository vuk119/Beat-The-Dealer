from deck import Deck

class Dealer:

    def __init__(self, n_players=1, n_decks=1):

        self.n_decks = n_decks
        self.n_players = n_players
        self.deck = Deck(n_decks)

    def shuffle(self):
        self.deck.shuffle()

    def reset_game(self):
        self.dealer_hand = []
        self.player_hands = []
        for _ in range(self.n_players):
            self.player_hands.append([])

    def init_deal(self):

        if self.deck.remaining_cards < 10:
            self.shuffle()


d = Dealer(3)
d.reset_game()
print(d.player_hands)
