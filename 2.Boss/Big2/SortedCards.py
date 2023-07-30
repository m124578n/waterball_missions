

class SortedCards:
    def __init__(self):
        self.cards = []

    def sort_spec_rule(self):
        self.cards = self.to_sort_suit(self.cards)
        self.cards = self.to_sort_rank(self.cards)

    def to_sort_suit(self, cards):
        return sorted(cards, key=lambda card: card.suit.value, reverse=self.set_sort_suit_reverse())

    def set_sort_suit_reverse(self):
        return False

    def to_sort_rank(self, cards):
        return sorted(cards, key=lambda card: card.rank.value, reverse=self.set_sort_rank_reverse())

    def set_sort_rank_reverse(self):
        return True

    def __repr__(self):
        string = ''
        for card in self.cards:
            string += str(card)
            string += ' '
        return string
