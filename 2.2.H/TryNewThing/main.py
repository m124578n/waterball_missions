from ShowDown import ShowDown, AIPlayer as SAI, HumanPlayer as SH
from UNO import UNO, AIPlayer as UAI, HumanPlayer as UH


def decide_player(number: int):
    players = []
    for x in range(number):
        players.append(UH())
    if len(players) != 4:
        for x in range(4 - number):
            players.append(UAI())
    return players


if __name__ == '__main__':
    player = int(input("請選擇人數："))
    game = UNO(decide_player(player))
    game.start()
