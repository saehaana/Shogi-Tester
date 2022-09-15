from Domain.Entities.Piece import Piece, Color


class Pawn(Piece):
    def __init__(self, color):
        Piece.__init__(self, color)
        self.description = 'Pawn'
        self.representation = 'P'

    def can_reach(self, origin_row, origin_col, destination_row, destination_col, color=None):
        if origin_row == destination_row and origin_col == destination_col:
            return False

        if color == Color.WHITE:
            if destination_col != origin_col or destination_row < origin_row or destination_row - origin_row > 1:
                return False
            else:
                return True
        else:
            if destination_col != origin_col or destination_row > origin_row or origin_row - destination_row > 1:
                return False
            else:
                return True
