from Domain.Entities.Piece import Piece


class Bishop(Piece):
    def __init__(self, color):
        Piece.__init__(self, color)
        self.description = 'Bishop'
        self.representation = 'B'
        self.obstructable = True

    def can_reach(self, origin_row, origin_col, destination_row, destination_col, color=None):
        if origin_row == destination_row and origin_col == destination_col:
            return False

        if abs(origin_row - destination_row) != abs(origin_col - destination_col):
            return False
        else:
            return True
