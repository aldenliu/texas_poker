import texas_poker
import numpy as np
from game_context import GameContext
from texas_strategy import RandomStrategy
from texas_poker import compare_poker, get_max_number
from texas_strategy import FOLD, CALL, RAISE, RERAISE, CHECK
import pdb
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

    def set_win_bets(self, win_bets):
        self._chip += win_bets

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

    def get_poker(self):
        return self._draw_poker

class PokerGame:
    def __init__(self, players):
        self._player_cnt = len(players)
        self._available_player_cnt = len(players)
        self._players = players
        chips = [player._chip for player in self._players]
        self._game_context = GameContext(self._player_cnt, chips)
        for player in self._players:
            player.set_game_context(self._game_context)
        np.random.shuffle(poker)
        self._shuffled_poker = poker
        self._deal()
        self._start_game()
        pass

    def _deal(self):
        for i in range(self._player_cnt):
            draw_poker = self._shuffled_poker[i*2: i*2+2]
            self._players[i].draw(draw_poker)
        self._game_context.set_table_poker(self._shuffled_poker[self._player_cnt * 2 : self._player_cnt * 2 + 5])

    def _end(self):
        on_table_status = [player.is_on_table() for player in self._players]
        on_table_cnt = on_table_status.count(True)
        candidate_index = on_table_status.index(True)
        for i in range(1, on_table_cnt):
            competitor_index = on_table_status.index(True)
            candidate_poker = np.append(self._players[candidate_index].get_poker(), self._game_context.get_table_poker())
            competitor_poker = np.append(self._players[competitor_index].get_poker(), self._game_context.get_table_poker())
            candidate_best = get_max_number(candidate_poker)
            competitor_best = get_max_number(competitor_poker)
            if compare_poker(candidate_best, competitor_best) < 0:
                candidate_index = competitor_index
        win_index = candidate_index
        win_bets = self._game_context.get_all_bets()
        self._players[win_index].set_win_bets(win_bets)

    def _start_game(self):
        if self._pre_flop() == 1:
            return self._end()
        if self._flop_round() == 1:
            return self._end()
        if self._turn_round() == 1:
            return self._end()
        if self._river_round() == 1:
            return self._end()

    def _bid(self):
        for i in range(0, self._player_cnt):
            if self._players[i].is_on_table():
                (action, cost) = self._players[i].action()
                if not self._players[i].is_on_table():
                    self._available_player_cnt -= 1
                self._game_context.record_action(i, action, cost)
            return 1
        return 0

    def _pre_flop(self):
        self._players[0].do_small_blind()
        self._players[1].do_big_blind()
        return self._bid()

    def _flop_round(self):
        self._game_context.set_flop_poker()
        return self._bid()

    def _turn_round(self):
        self._game_context.set_turn_poker()
        return self._bid()

    def _river_round(self):
        return self._game_context.set_river_poker()
        self._bid()

def main():
    players = []
    for i in range(0, 6):
        player = Player()
        player.set_strategy(RandomStrategy())
        players.append(player)
    game = PokerGame(players)
    bets = [player.get_bets() for player in players]
    print(bets)

if __name__ == '__main__':
    main()
