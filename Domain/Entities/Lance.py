from Domain.Entities.Piece import Piece, Color


class Lance(Piece):
    def __init__(self, color):
        Piece.__init__(self, color)
        self.description = 'Lance'
        self.representation = 'L'
        self.obstructable = True

    def can_reach(self, origin_row, origin_col, destination_row, destination_col, color=None):
        if origin_row == destination_row and origin_col == destination_col:
            return False

        if origin_col != destination_col:
            return False

        if color == Color.WHITE:
            return origin_row < destination_row
        else:
            return origin_row > destination_row
