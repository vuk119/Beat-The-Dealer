from deck import Deck

class Dealer:

    def __init__(self, n_players=1, n_decks=1, print_game=False):
        self.n_decks = n_decks
        self.n_players = n_players
        self.deck = Deck(n_decks)
        self.print_game = print_game

    def shuffle(self):
        self.deck.shuffle()

    def reset_game(self):
        self.dealer_hand = []
        self.player_hands = []
        for _ in range(self.n_players):
            self.player_hands.append([])
        self.shuffle()

    def init_deal(self):
        # This condition should be altered
        if self.deck.remaining_cards() < 10:
            self.shuffle()

        # Get 

        self.dealer_hand.append(self.deck.draw())
        self.dealer_hand.append(self.deck.draw())

        if self.print_game is True:
            print(f"Dealer's face up card is {self.dealer_hand[0]}\n")

        for i in range(self.n_players):
            # Each player recieves 2 cards
            # In real BJ they are dealt one card each and then another
            # Here it doesn't really matter
            self.player_hands[i].append(self.deck.draw())
            self.player_hands[i].append(self.deck.draw())
            if self.print_game is True:
                print(f"Player {i} draws {self.player_hands[i][0]} and {self.player_hands[i][1]}")


d = Dealer(3, print_game=True)
d.reset_game()
d.init_deal()
