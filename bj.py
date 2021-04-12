'''
A namespace for functions used by more than one class.
'''

class BJ:
    def get_card_value(card):
        if card.value in ['J', 'Q', 'K', '10']:
            return 10
        elif card.value == 'A':
            return [1, 11]
        else:
            return int(card.value)

    def get_hand_value(hand):
        '''
        Returns total hand value and the number of soft aces
        '''
        usable_aces = 0
        hand_value = 0
        for card in hand:
            if card.value != 'A':
                hand_value += BJ.get_card_value(card)
            else:
                usable_aces += 1
                hand_value += 11

        while hand_value > 21 and usable_aces > 0:
            hand_value -= 10
            usable_aces -= 1

        if usable_aces == 1:
            # It is only possible to have one usable ace at a time.
            soft = True
        else:
            soft = False

        return hand_value, soft
