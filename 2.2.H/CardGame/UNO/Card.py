from ..CardTemplate import CardTemplate


class Card(CardTemplate):
    def __init__(self, color, number):
        self.color = color
        self.number = number
