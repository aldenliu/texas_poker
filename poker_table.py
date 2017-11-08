import texas_poker
import numpy as np
from game_context import GameContext
from texas_strategy import Strategy
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
        self._chip = 10000
        self._is_fold = False
        self._bet = 0
        self._on_table = True
        pass

    def set_game_context(self, context):
        self._game_context = context

    def set_strategy(self, stragety):
        self._strategy = stragety

    def draw(self, draw_poker):
        self._draw_poker = draw_poker

    def do_small_blind(self):
        self._chip -= SMALL_BLIND_COST
        self._bet += SMALL_BLIND_COST

    def do_big_blind(self):
        self._chip -= BIG_BLIND_COST
        self._bet += BIG_BLIND_COST

    def is_on_table(self):
        return self._on_table

    def action(self):
        cur_bid = self._game_context.get_cur_bid()
        (action, cost) = self._strategy.action(self._chip, self._bet, cur_bid)
        if action == FOLD:
            self._on_table = False
        return (action, cost)
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
            if self._players[i].is_on_table():
                (action, cost) = self._players[i].action()
                self._game_context.record_action(i, action, cost)

    def _pre_flop(self):
        self._players[0].do_small_blind()
        self._players[1].do_big_blind()
        self._bid()

    def _flop_round(self):
        self._game_context.set_flop_poker()
        self._bid()

    def _turn_round(self):
        self._game_context.set_turn_poker()
        self._bid()

    def _river_round(self):
        self._game_context.set_river_poker()
        self._bid()

def main():
    players = []
    for i in range(0, 6):
        player = Player()
        player.set_strategy(Strategy())
        players.append(player)
    game = PokerGame(players)

if __name__ == '__main__':
    main()
