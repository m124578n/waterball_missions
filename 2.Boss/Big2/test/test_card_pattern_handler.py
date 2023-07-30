from unittest import TestCase
from Big2.CardPattern import FullHouse, Pair, Straight, Single
from Big2.Card import Card
from Big2.CardPatternHandler import IsFullHouse, IsPair, IsSingle, IsStraight


class TestCardPatternHandler(TestCase):
    def test_is_full_house(self):
        cards = [Card("S[2]"), Card("C[2]"), Card("C[3]"), Card("H[2]"), Card("S[3]")]
        handler = IsFullHouse(None)
        target = handler.check(cards)
        full_house = FullHouse(cards)
        self.assertEqual(type(full_house), type(target))

    def test_is_not_full_house(self):
        cards = [Card("S[4]"), Card("C[2]"), Card("C[3]"), Card("H[2]"), Card("S[3]")]
        handler = IsFullHouse(None)
        target = handler.check(cards)
        self.assertEqual(False, target)

    def test_is_pair(self):
        cards = [Card("C[2]"), Card("S[2]")]
        handler = IsPair(None)
        target = handler.check(cards)
        self.assertEqual(type(Pair(cards)), type(target))

    def test_is_not_pair(self):
        cards = [Card("C[3]"), Card("S[2]")]
        handler = IsPair(None)
        target = handler.check(cards)
        self.assertEqual(False, target)

    def test_is_single(self):
        cards = [Card("C[2]")]
        handler = IsSingle(None)
        target = handler.check(cards)
        self.assertEqual(type(Single(cards)), type(target))

    def test_is_not_single(self):
        cards = [Card("C[2]"), Card("S[2]")]
        handler = IsSingle(None)
        target = handler.check(cards)
        self.assertEqual(False, target)

    def test_is_straight(self):
        cards = [Card("C[8]"), Card("C[5]"), Card("C[6]"), Card("C[7]"), Card("C[9]")]
        handler = IsStraight(None)
        target = handler.check(cards)
        self.assertEqual(type(Straight(cards)), type(target))

    def test_is_not_straight(self):
        cards = [Card("S[9]"), Card("C[5]"), Card("C[6]"), Card("C[7]"), Card("C[9]")]
        handler = IsStraight(None)
        target = handler.check(cards)
        self.assertEqual(False, target)

    def test_CoR_all_pattern(self):
        cards = [Card("C[3]"), Card("C[Q]"), Card("C[K]"), Card("C[A]"), Card("C[2]")]
        handler = IsSingle(IsPair(IsFullHouse(IsStraight(None))))
        target = handler.check(cards)
        self.assertEqual(type(Straight(cards)), type(target))

    def test_not_pass_CoR_all_pattern1(self):
        cards = [Card("C[8]"), Card("C[5]"), Card("C[6]"), Card("C[7]"), Card("C[10]")]
        handler = IsSingle(IsPair(IsFullHouse(IsStraight(None))))
        target = handler.check(cards)
        self.assertEqual(False, target)

    def test_not_pass_CoR_all_pattern2(self):
        cards = [Card("C[3]"), Card("C[Q]"), Card("C[Q]"), Card("C[A]"), Card("C[2]")]
        handler = IsSingle(IsPair(IsFullHouse(IsStraight(None))))
        target = handler.check(cards)
        self.assertEqual(False, target)
