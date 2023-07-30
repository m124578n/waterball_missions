from unittest import TestCase
from Big2.CardPattern import FullHouse, Pair, Straight, Single
from Big2.Card import Card


class TestCardPattern(TestCase):
    def test_create_sorted_full_house_01(self):
        cards = [Card("S[2]"), Card("C[2]"), Card("C[3]"), Card("H[2]"), Card("S[3]")]
        full_house = FullHouse(cards)
        self.assertEqual(str(full_house), 'C[2] H[2] S[2] C[3] S[3] ')

    def test_create_sorted_full_house_02(self):
        cards = [Card("S[4]"), Card("C[7]"), Card("H[4]"), Card("C[4]"), Card("S[7]")]
        full_house = FullHouse(cards)
        self.assertEqual(str(full_house), 'C[4] H[4] S[4] C[7] S[7] ')

    def test_create_sorted_pair(self):
        cards = [Card("C[2]"), Card("S[2]")]
        self.assertEqual(str(Pair(cards)), 'C[2] S[2] ')

    def test_create_c3(self):
        self.assertEqual(str(Card("C[3]")), 'C[3]')

    def test_create_sorted_straight_01(self):
        cards = [Card("C[8]"), Card("C[5]"), Card("C[6]"), Card("C[7]"), Card("C[9]")]
        self.assertEqual(str(Straight(cards)), 'C[5] C[6] C[7] C[8] C[9] ')

    def test_create_sorted_straight_02(self):
        cards = [Card("C[5]"), Card("C[2]"), Card("C[A]"), Card("C[3]"), Card("C[4]")]
        s = Straight(cards)
        self.assertEqual(str(s), 'C[A] C[2] C[3] C[4] C[5] ')

    def test_create_sorted_straight_03(self):
        cards = [Card("C[A]"), Card("C[2]"), Card("C[Q]"), Card("C[K]"), Card("C[J]")]
        s = Straight(cards)
        self.assertEqual(str(s), 'C[J] C[Q] C[K] C[A] C[2] ')

    def test_create_sorted_straight_04(self):
        cards = [Card("C[K]"), Card("C[10]"), Card("C[Q]"), Card("C[J]"), Card("C[A]")]
        s = Straight(cards)
        self.assertEqual(str(s), 'C[10] C[J] C[Q] C[K] C[A] ')

    def test_create_sorted_straight_05(self):
        cards = [Card("C[K]"), Card("C[J]"), Card("C[9]"), Card("C[Q]"), Card("C[10]")]
        s = Straight(cards)
        self.assertEqual(str(s), 'C[9] C[10] C[J] C[Q] C[K] ')

