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
        self._preflop_action = texas_poker.empty_array
        self._flop_action = texas_poker.empty_array
        self._turn_action = texas_poker.empty_array
        self._river_action = texas_poker.empty_array
        self._on_table = np.ones(player_cnt)
        self._action = []
        self._prev_action = BLIND

    def get_cur_bid(self):
        return self._cur_bid

    def set_blind(self, player_index, cost):
        self._bets[player_index] += cost
        self._cur_bid = cost

    def get_all_bets(self):
        return sum([bet for bet in self._bets])

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

    def reset_round(self):
        self._cur_bid = 0
        self._prev_action = CHECK

    def _call(self, player_index, bid_cost):
        self._bets[player_index] += bid_cost
        self._action.append((player_index, CALL, bid_cost))

    def _check(self, player_index):
        self._action.append((player_index, CHECK, 0))

    def _raise(self, player_index, raise_bid):
        self._cur_bid += raise_bid
        self._bets[player_index] += raise_bid
        self._action.append((player_index, RAISE, raise_bid))

    def record_action(self, player_index, action, bid_cost = 0):
        if action == BLIND:
            self._cur_bid = bid_cost
            self._prev_action = BLIND
            return 
        elif action == FOLD:
            self._on_table[player_index] = 0
            return
        elif action == CALL:
            self._call(player_index, bid_cost)
            self._prev_action = CALL
            return
        elif action == CHECK:
            self._check(player_index)
            self._prev_action = CHECK
            return
        elif action == RAISE:
            self._prev_action = RAISE
            self._raise(player_index, bid_cost)
            return
        elif action == RERAISE:
            self._prev_action = RAISE
            self._raise(player_index, bid_cost)
            return

    def get_prev_action(self):
        return self._prev_action

