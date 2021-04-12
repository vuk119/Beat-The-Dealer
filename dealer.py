from deck import Deck
from bj import BJ

class Dealer:

    def __init__(self, players, n_decks=1, print_game=False):
        self.n_decks = n_decks
        self.n_players = len(players)
        self.players = players
        self.deck = Deck(n_decks)
        self.print_game = print_game

    def cprint(self, string):
        # Controlled print only if control_var is True
        if self.print_game is True:
            print(string)

    def shuffle(self):
        self.deck.shuffle()

    def reset_game(self):
        self.dealer_hand = []
        self.player_hands = []
        self.bets = [0] * self.n_players
        self.player_totals = [0] * self.n_players
        for _ in range(self.n_players):
            self.player_hands.append([])
        self.shuffle()

    def collect_bets(self):
        for i, player in enumerate(self.players):
            self.bets[i] = player.get_bet(self.shuffled)

    def init_deal(self):
        # This condition should be altered
        # TO DO: Implement immediate blackjack

        if self.deck.remaining_cards() < 10:
            self.shuffle()
            self.shuffled = True
        else:
            self.shuffled = False

        self.collect_bets()

        self.dealer_hand.append(self.deck.draw())
        self.dealer_hand.append(self.deck.draw())

        self.cprint(f"Dealer's face up card is {self.dealer_hand[0]}\n")

        for i in range(self.n_players):
            # Each player recieves 2 cards
            # In real BJ they are dealt one card each and then another
            # Here it doesn't really matter
            self.player_hands[i].append(self.deck.draw())
            self.player_hands[i].append(self.deck.draw())

            self.cprint(f"Player {i} draws {self.player_hands[i][0]} and {self.player_hands[i][1]}.")
            self.cprint(f"Player {i} has a score of {BJ.get_hand_value(self.player_hands[i])[0]}")
            self.cprint("\n")

    def play(self):
        # Plays one round of BJ
        # TO DO: Implement split, insurance and doubledown
        self.init_deal()

        # Players Decisions
        for i, player in enumerate(self.players):
            self.cprint(f"Player {i} turn:")
            avaliable_decision = ['Hit', 'Stand'] # TO DO: Implement this properly
            dealer_card = self.dealer_hand[0]
            my_ids = [i]
            info = (avaliable_decision, dealer_card, my_ids, self.player_hands)
            decision = player.get_decision(info)

            while decision != 'Stand':
                if decision == 'Hit':
                    self.player_hands[i].append(self.deck.draw())
                    self.cprint(f"Player {i} draws {self.player_hands[i][-1]}.")

                total = BJ.get_hand_value(self.player_hands[i])[0]

                if total >= 21:
                    self.cprint(f"Player {i} went bust with a total of {total}")
                    self.player_totals[i] = total
                    break
                else:
                    self.cprint(f"Player {i} has a total of {total}")

                info = (avaliable_decision, dealer_card, my_ids, self.player_hands)
                decision = player.get_decision(info)

            if decision == 'Stand':
                self.cprint(f"Player {i} stands.")

            total = BJ.get_hand_value(self.player_hands[i])[0]
            self.player_totals[i] = total
            self.cprint("\n")

        # Dealer's play
        self.cprint(f"Dealer's face up card is {self.dealer_hand[0]}")
        self.cprint(f"Dealer's face down card is {self.dealer_hand[1]}")
        d_total = BJ.get_hand_value(self.dealer_hand)[0]
        while d_total < 17:
            self.dealer_hand.append(self.deck.draw())
            self.cprint(f"Dealer draw {self.dealer_hand[-1]}")
            d_total = BJ.get_hand_value(self.dealer_hand)[0]

        self.cprint(f"Dealer's total score is {d_total}")
        if d_total > 21:
            self.cprint(f"Dealer went bust.")
        self.cprint("\n")

        # Game Report
        for i in range(self.n_players):
            total = self.player_totals[i]
            if d_total > 21 and total <= 21:
                self.cprint(f"Player {i}, score {total}: WON")
            elif total > 21:
                self.cprint(f"Player {i}, score {total}: BUST")
            elif d_total == total:
                self.cprint(f"Player {i}, score {total}: PUSH")
            elif d_total > total:
                self.cprint(f"Player {i}, score {total}: LOST")
            elif d_total < total:
                self.cprint(f"Player {i}, score {total}: WON")



from player import HitUntilPlayer, ManualPlayer

a = HitUntilPlayer(17)
b = HitUntilPlayer(16)
m = ManualPlayer()
d = Dealer([a, b, m], print_game=True)
d.reset_game()
d.play()
