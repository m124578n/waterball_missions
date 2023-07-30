from .Card import Card


class Hand:
    def __init__(self):
        self.card = []
        self.size = len(self.card)

    def add_card(self, card: Card):
        self.size += 1
        self.card.append(card)

    def show(self, hand_index: int) -> Card:
        self.size -= 1
        return self.card.pop(hand_index)
