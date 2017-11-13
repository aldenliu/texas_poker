import random
UNKOWN = 0
FOLD = 1
CALL = 2
RAISE = 3
RERAISE = 4
CHECK = 5

class Strategy():
    def __init__(self):
        pass

    def action(self, chip, bet, cur_bid):
        return (UNKOWN, 0)

class RandomStrategy(Strategy):
    def __init__(self):
        pass

    def action(self, chip, bet, cur_bid):
        behavior = random.randint(1,5)
        if behavior == RAISE:
            return (RAISE, chip / 3)
        if behavior == RERAISE:
            return (RERAISE, cur_bid * 2)
        else:
            return (behavior, 0)

