import texas_poker
import numpy as np
poker = np.array(range(0,52))

UNKOWN = 0
FOLD = 1
CALL = 2
RAISE = 3
RERAISE = 4
CHECK = 5


class Player:
    def __init__(self):
        self.chip = 10000
        pass

    def draw(self, draw_poker):
        self._draw_poker = draw_poker

    def action(self, )
        return 

class GameSituation():
    def __init__(self):
        pass
    
    def

class PokerGame:
    def __init__(self, player_cnt):
        self._player_cnt = player_cnt
        self._players_join_game()
        self._deal()
        self._start_game()
        pass

    def _players_join_game(self):
        self._players = []
        for i in range(0, self._player_cnt):
            self._players.append(Player())
        pass

    def _deal(self):
        np.random.shuffle(poker)
        for i in range(self._player_cnt):
            draw_poker = poker[i*2: i*2+2]
            self._players[i].draw(draw_poker)
        self._table_poker = poker[2 * self._player_cnt : 2 * self._player_cnt + 6]
        print(self._table_poker)
        print(self._players[0]._draw_poker)

    def _start_game(self):
        self._pre_flop()
        self._flop_round()
        self._turn_round()
        self._river_round()

    def _pre_flop(self):

def main():
    game = PokerGame(6)

if __name__ == '__main__':
    main()
