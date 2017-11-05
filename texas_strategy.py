UNKOWN = 0
FOLD = 1
CALL = 2
RAISE = 3
RERAISE = 4
CHECK = 5

class Strategy():
    def __init__(self):
        pass

    def action(self):
        return FOLD


class RandomStrategy(Strategy):
    def __init__(self):
        pass
