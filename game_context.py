import numpy as np
import texas_poker
from texas_strategy import *

FLOP_SHOWED = np.array([1,1,1,0,0])
TURN_SHOWED = np.array([1,1,1,1,0])
RIVER_SHOWED = np.array([1,1,1,1,1])
class GameContext():
    def __init__(self, player_cnt, chips):
        self._chips = chips
        self._player_cnt = player_cnt
        self._bets = np.zeros(player_cnt)
        self._cur_bid = 0
        self._cur_inc_bid = 0
        self._preflop_action = texas_poker.empty_array
        self._flop_action = texas_poker.empty_array
        self._turn_action = texas_poker.empty_array
        self._river_action = texas_poker.empty_array
        self._on_table = np.ones(player_cnt)

    def get_cur_bid(self):
        return self._cur_bid

    def set_small_blind(self, player_index):
        self._bets[player_index] += SMALL_BLIND_COST
        self._cur_bid = SMALL_BLIND_COST

    def get_all_bets(self):
        return sum([bet for bet in self._bets])

    def set_big_blind(self, player_index):
        self._bets[player_index] += BIG_BLIND_COST
        self._cur_bid = BIG_BLIND_COST

    def set_table_poker(self, poker):
        self._poker = poker
        self._poker_is_showed = np.zeros(self._player_cnt)

    def get_table_poker(self):
        return self._poker

    def set_flop_poker(self):
        self._poker_is_showed = FLOP_SHOWED

    def set_turn_poker(self):
        self._poker_is_showed = TURN_SHOWED

    def set_river_poker(self):
        self._poker_is_showed = RIVER_SHOWED

    def _call(self, player_index):
        self._bets[player_index] += self._cur_inc_bid
        self._action[player_index] = CALL

    def record_action(self, player_index, action, bid_cost = 0):
        if action == FOLD:
            self._on_table[player_index] = 0
            return
        if action == CALL:
            self._call(player_index)
            return
        if action == CHECK:
            return

