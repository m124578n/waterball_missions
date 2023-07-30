from unittest import TestCase
from Big2.CardPattern import FullHouse, Pair, Straight, Single
from Big2.Card import Card


class TestCompare(TestCase):
    def test_compare_full_house(self):
        cards1 = [Card("S[2]"), Card("C[2]"), Card("C[3]"), Card("H[2]"), Card("S[3]")]
        cards2 = [Card("S[A]"), Card("C[A]"), Card("C[3]"), Card("H[A]"), Card("S[3]")]
        full_house1 = FullHouse(cards1)
        full_house2 = FullHouse(cards2)
        self.assertEqual(True, full_house1 > full_house2)

    def test_compare_straight(self):
        cards1 = [Card("C[5]"), Card("C[2]"), Card("C[A]"), Card("C[3]"), Card("C[4]")]
        cards2 = [Card("C[8]"), Card("C[5]"), Card("C[6]"), Card("C[7]"), Card("C[9]")]
        s1 = Straight(cards1)
        s2 = Straight(cards2)
        self.assertEqual(True, s1 > s2)

    def test_compare_pair(self):
        cards1 = [Card("C[2]"), Card("S[2]")]
        cards2 = [Card("H[2]"), Card("D[2]")]
        p1 = Pair(cards1)
        p2 = Pair(cards2)
        self.assertEqual(True, p1 > p2)

    def test_compare_single(self):
        cards1 = [Card("C[2]")]
        cards2 = [Card("H[2]")]
        s1 = Single(cards1)
        s2 = Single(cards2)
        self.assertEqual(True, s1 < s2)
