from ..CardTemplate import CardTemplate


class Card(CardTemplate):
    def __init__(self, rank, suits):
        self.rank = rank
        self.suits = suits

    @staticmethod
    def show_down(cards):
        biggest_card = None
        card_index = None
        for index, card in enumerate(cards):
            if biggest_card is None:
                biggest_card = card
                card_index = index
            else:
                if biggest_card.rank.value < card.rank.value:
                    biggest_card = card
                    card_index = index
                elif biggest_card.rank.value == card.rank.value:
                    if biggest_card.suits.value < card.suits.value:
                        biggest_card = card
                        card_index = index
        return card_index


