from unittest import TestCase
from Big2.HandCards import HandCards
from Big2.Card import Card


class TestHandCards(TestCase):
    def test_create_sorted_full_house(self):
        hand = HandCards()
        hand.add_card(Card("D[2]"))
        hand.add_card(Card("C[4]"))
        hand.add_card(Card("C[3]"))
        hand.add_card(Card("D[10]"))
        hand.add_card(Card("S[7]"))
        hand.add_card(Card("S[8]"))
        hand.add_card(Card("S[A]"))
        hand.add_card(Card("H[9]"))
        hand.add_card(Card("H[Q]"))
        hand.add_card(Card("S[J]"))
        hand.add_card(Card("D[Q]"))
        hand.add_card(Card("H[2]"))
        hand.add_card(Card("D[A]"))
        hand.sort_spec_rule()
        self.assertEqual(str(hand), 'C[3] C[4] S[7] S[8] H[9] D[10] S[J] D[Q] H[Q] D[A] S[A] D[2] H[2] ')
