from .SortedCards import SortedCards


class HandCards(SortedCards):
    def __init__(self):
        super().__init__()
        self.size = 0

    def add_card(self, card):
        self.size += 1
        self.cards.append(card)

    def show_card(self, player_decide_play: str):
        show_cards = []
        index: list[str] = player_decide_play.split(" ")
        for idx in index:
            show_cards.append(self.cards[int(idx)])
            self.size -= 1
        for card1 in show_cards:
            for card2 in self.cards:
                if card1 == card2:
                    self.cards.remove(card2)
                    break
        return show_cards

    def set_sort_rank_reverse(self):
        return False

