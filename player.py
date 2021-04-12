from abc import abstractmethod

class Player(object):
    '''
    Abstract Class for a player.
    Each strategy is a class that inherits this class
    and must override get_decision function.
    '''
    def __init__(self):
        pass

    @abstractmethod
    def get_bet_value(self, shuffled):
        '''
        Returns the amount to be bet in this round.
        Shuffled - indicates whether the deck has been shuffled prior to the round.
        '''
        pass

    @abstractmethod
    def get_decision(self, info):
        '''
        Each move player recieves a variable info.
        Info = (availiable_decisions, dealer_card, my_ids, players_cards)
        Return must be an element of the avaliable_decisions list
        dealer_card - Dealer's face_up card
        my_ids - list of indices indicating this player's hands. Usually one id,
        but in case of a split contains two ids pointing to both hands.
        players_cards - a list containing cards of all players
        '''
        pass


    def get_card_value(self, card):
        if card.value in ['J', 'Q', 'K', '10']:
            return 10
        elif card.value == 'A':
            return [1, 11]
        else:
            return int(card.value)

    def get_hand_value(self, hand):
        usable_aces = 0
        hand_value = 0
        for card in hand:
            if card.value != 'A':
                hand_value += self.get_card_value(card)
            else:
                usable_aces += 1
                hand_value += 11

        while hand_value > 21 and usable_aces > 0:
            hand_value -= 10
            usable_aces -= 1

        self.usable_aces = usable_aces # This variables returns the number of usable aces

        return hand_value

class HitUntilThPlayer(Player):
    '''
    Player that hits if they have less than the hit_th.
    '''
    def __init__(self, hit_th):
        Player().__init__()
        self.hit_th = hit_th

    def get_bet_value(self, shuffled):
        return 1

    def get_decision(self, info):
        availiable_decisions, dealer_card, my_ids, players_cards = info()
        my_score = self.get_hand_value(players_cards[my_ids[0]])
        if my_score < self.hit_th:
            return 'Hit'
        else:
            return 'Stand'

a = HitUntilThPlayer(10)
from card import Card
hand = [Card('clubs', 'A'), Card('clubs', 'A'), Card('clubs', 'A'), Card('clubs', '10')]
print(a.get_hand_value(hand))
