from enum import Enum


class Color(Enum):
    WHITE = 0
    BLACK = 1


class Piece:
    description = None
    color = None
    obstructable = False
    representation = None
    symbol = None

    SYMBOL_BLACK = '^'
    SYMBOL_WHITE = 'v'

    def __init__(self, color=Color.WHITE):
        self.color = color
        self.symbol = self.SYMBOL_WHITE if color == Color.WHITE else self.SYMBOL_BLACK

    def create_white(self):
        return self.__init__(Color.WHITE)

    def create_black(self):
        return self.__init__(Color.BLACK)

    def get_color(self):
        return self.color

    def is_obstructable(self):
        return self.obstructable

    def can_reach(self, origin_row, origin_col, destination_row, destination_col, color=None):
        pass

    def convert(self):
        self.symbol = self.SYMBOL_BLACK if self.color == Color.WHITE else self.SYMBOL_WHITE
        self.color = Color.WHITE if self.color == Color.BLACK else Color.BLACK

    def to_string(self):
        return self.representation + self.symbol
