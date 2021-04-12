from abc import abstractmethod
from bj import BJ

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
        Info = (availiable_decisions, dealer_card, my_ids, player_hands)
        Return must be an element of the avaliable_decisions list
        dealer_card - Dealer's face_up card
        my_ids - list of indices indicating this player's hands. Usually one id,
        but in case of a split contains two ids pointing to both hands.
        player_hands - a list containing cards of all players
        '''
        pass

class HitUntilPlayer(Player):
    '''
    Player that hits if they have less than the hit_th.
    '''
    def __init__(self, hit_th):
        Player().__init__()
        self.hit_th = hit_th

    def get_bet(self, shuffled):
        return 1

    def get_decision(self, info):
        availiable_decisions, dealer_card, my_ids, player_hands = info
        my_score, soft = BJ.get_hand_value(player_hands[my_ids[0]])
        if my_score < self.hit_th:
            return 'Hit'
        else:
            return 'Stand'

# a = HitUntilPlayer(10)
# from card import Card
# hand = [Card('clubs', 'A'), Card('clubs', 'A'), Card('clubs', 'A')]
# print(BJ.get_hand_value(hand))
