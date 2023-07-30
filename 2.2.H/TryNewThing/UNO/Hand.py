
class Hand:
    def __init__(self):
        self.card = []
        self.size = len(self.card)

    def add_card(self, card):
        self.size += 1
        self.card.append(card)

    def show(self, hand_index: int):
        self.size -= 1
        return self.card.pop(hand_index)
