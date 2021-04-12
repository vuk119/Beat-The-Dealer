class Card:

    def __init__(self, suit, value):

        if suit not in ['clubs', 'diamonds', 'hearts', 'spades']:
            raise ValueError(f"{suit} is not a valid suit.")
        else:
            self.suit = suit

        if value not in ['A', '2', '3', '4', '5', '6', '7', '8', '9',
                        '10', 'J', 'Q', 'K']:
            raise ValueError(f"{value} is not a valid value.")
        else:
            self.value = value

    def __repr__(self):
        return f"Card({self.value}, {self.suit})"

    def __str__(self):
        return f"Card({self.value}, {self.suit})"

# c = Card('clubs', 'A')
# print(c)
