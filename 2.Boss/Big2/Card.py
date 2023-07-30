from .Suit import Suit
from .Rank import Rank


class Card:
    def __init__(self, card_form: str):
        suit = card_form.split('[')[0]
        rank = "_" + card_form.split('[')[1][:-1]
        self.rank = Rank[rank]
        self.suit = Suit[suit]

    def __repr__(self):
        if self.rank.name[-1] == '0':
            rank = 10
        else:
            rank = self.rank.name[-1]
        return f"{self.suit.name}[{rank}]"

    def __gt__(self, other):
        if self.rank.value > other.rank.value:
            return True
        elif self.rank.value == other.rank.value:
            return self.suit.value > other.suit.value

    def __ne__(self, other):
        return self.rank.value != other.rank.value

    def __eq__(self, other):
        return self.rank.value == other.rank.value and self.suit.value == other.suit.value
