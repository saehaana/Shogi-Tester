from Domain.Entities.Piece import Piece, Color


class Knight(Piece):
    def __init__(self, color):
        Piece.__init__(self, color)
        self.description = 'Knight'
        self.representation = 'N'

    def can_reach(self, origin_row, origin_col, destination_row, destination_col, color=None):
        if origin_row == destination_row and origin_col == destination_col:
            return False

        if abs(destination_col - origin_col) != 1:
            return False

        if color == Color.WHITE:
            return destination_row - origin_row == 2
        else:
            return origin_row - destination_row == 2
