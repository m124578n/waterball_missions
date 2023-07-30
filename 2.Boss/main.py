from Big2.HumanPlayer import HumanPlayer
from Big2.Big2 import Big2
from Big2.CardPatternHandler import *


if __name__ == "__main__":
    players = [HumanPlayer(0), HumanPlayer(1), HumanPlayer(2), HumanPlayer(3)]
    big2 = Big2(players, IsSingle(IsPair(IsFullHouse(IsStraight(None)))))
    big2.start()
