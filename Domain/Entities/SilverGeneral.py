from Domain.Entities.Piece import Piece, Color


class SilverGeneral(Piece):
    def __init__(self, color):
        Piece.__init__(self, color)
        self.description = 'Silver General'
        self.representation = 'S'

    def can_reach(self, origin_row, origin_col, destination_row, destination_col, color=None):
        if origin_row == destination_row and origin_col == destination_col:
            return False

        if color == Color.WHITE:
            if abs(origin_row - destination_row) > 1 or abs(origin_col - destination_col) > 1 or (
                    destination_row < origin_row and destination_col == origin_col) or (
                    destination_row == origin_row and destination_col != origin_col):
                return False
            else:
                return True
        else:
            if abs(origin_row - destination_row) > 1 or abs(origin_col - destination_col) > 1 or (
                    destination_row > origin_row and destination_col == origin_col) or (
                    destination_row == origin_row and destination_col != origin_col):
                return False
            else:
                return True
