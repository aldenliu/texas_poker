import texas_poker
import numpy as np
from game_context import GameContext
poker = np.array(range(0,52))
# ROUND parameter, curerntly useless
#PRE_FLOP = 1
#FLOP_ROUND = 2
#TURN_ROUND = 3
#RIVER_ROUND = 4

SMALL_BLIND_COST = 150
BIG_BLIND_COST = SMALL_BLIND_COST * 2

class Player:
    def __init__(self):
        self.chip = 10000
        self._is_fold = False
        self._bet = 0
        pass

    def set_game_context(self, context):
        self._game_context = context

    def set_strategy(self, stragety):
        self._strategy = stragety

    def draw(self, draw_poker):
        self._draw_poker = draw_poker

    def do_small_blind(self):
        self.chip -= SMALL_BLIND_COST
        self._bet += SMALL_BLIND_COST

    def do_big_blind(self):
        self.chip -= BIG_BLIND_COST
        self._bet += BIG_BLIND_COST

    def action(self):
        return self._strategy.action()

class PokerGame:
    def __init__(self, players):
        self._player_cnt = len(players)
        self._players = players
        chips = [player.chip for player in self._players]
        self._game_context = GameContext(self._player_cnt, chips)
        np.random.shuffle(poker)
        self._shuffled_poker = poker
        self._deal()
        self._start_game()
        pass

    def _deal(self):
        for i in range(self._player_cnt):
            draw_poker = self._shuffled_poker[i*2: i*2+2]
            self._players[i].draw(draw_poker)

    def _start_game(self):
        self._pre_flop()
        self._flop_round()
        self._turn_round()
        self._river_round()

    def _bid(self):
        for i in range(0, self._player_cnt):
            self._players[i].action()

    def _pre_flop(self):
        self._players[0].do_small_blind()
        self._players[1].do_big_blind()
        self._bid()

    def _flop_round(self):
        poker_start_index = 2 * self._player_cnt
        flop_poker = self._shuffled_poker[poker_start_index : poker_start_index + 3]
        self._game_context.set_flop_poker(flop_poker)
        self._bid()

    def _turn_round(self):
        poker_start_index = 2 * self._player_cnt + 3
        turn_poker = self._shuffled_poker[poker_start_index]
        self._game_context.set_turn_poker(flop_poker)
        self._bid()

    def _river_round(self):
        poker_start_index = 2 * self._player_cnt + 4
        river_poker = self._shuffled_poker[poker_start_index]
        self._game_context.set_river_poker(river_poker)
        self.bid()

def main():
    players = []
    for i in range(0, 6):
        players.append(Player())
    game = PokerGame(players)

if __name__ == '__main__':
    main()
