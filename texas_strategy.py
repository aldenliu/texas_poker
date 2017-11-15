import random
import pdb
UNKOWN = -1
BLIND = 0
FOLD = 1
CALL = 2
RAISE = 3
RERAISE = 4
CHECK = 5

VALID_MAP = {BLIND:set([CALL, RAISE, FOLD]), \
    CALL:set([CALL, RAISE, FOLD]), \
    RAISE:set([CALL, RERAISE, FOLD]), 
    RERAISE: set([CALL, RERAISE, FOLD]), 
    CHECK: set([RAISE, CHECK])}

class Strategy():
    def __init__(self):
        pass

    def action(self, chip, bet, cur_bid):
        return (UNKOWN, 0)

class RandomStrategy(Strategy):
    def __init__(self):
        pass

    def set_game_context(self, game_context):
        self._game_context = game_context

    def _is_behavior_valid(self, prev_action, behavior):
        if behavior in VALID_MAP[prev_action]:
            return True
        return False

    def action(self, chip, bet, cur_bid):
        prev_action = self._game_context.get_prev_action()
        behavior = random.randint(1,5)
        while not self._is_behavior_valid(prev_action, behavior):
            behavior = random.randint(1,5)
        if behavior == RAISE:
            total_bet = self._game_context.get_all_bets()
            bet = max(cur_bid * 2, int(total_bet / 3))
            bet = min(bet, chip)
            return (RAISE, bet)
        elif behavior == RERAISE:
            bet = cur_bid * 2
            bet = min(bet, chip)
            return (RERAISE, bet)
        elif behavior == CALL:
            bet = min(cur_bid, chip)
            return (behavior, bet)
        else:
            return (behavior, 0)

