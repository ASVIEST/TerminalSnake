class Bonus:
    def __init__(self, symbol, x, y):
        self.x = x
        self.y = y
        self.symbol = symbol

    def __str__(self):
        return self.symbol
