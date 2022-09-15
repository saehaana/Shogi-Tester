class DropPieceCommand:
    board = None
    droppable_pieces = None
    origin_coordinates = None
    destination_coordinates = None

    def __init__(self, board, droppable_pieces, origin_coordinates, destination_coordinates):
        self.board = board
        self.droppable_pieces = droppable_pieces
        self.origin_coordinates = origin_coordinates
        self.destination_coordinates = destination_coordinates

    def get_board(self):
        return self.board

    def get_origin_coordinates(self):
        return self.origin_coordinates

    def get_destination_coordinates(self):
        return self.destination_coordinates

    def get_droppable_pieces(self):
        return self.droppable_pieces
