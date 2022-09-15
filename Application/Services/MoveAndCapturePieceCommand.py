class MoveAndCapturePieceCommand:
    board = None
    origin_coordinates = None
    destination_coordinates = None
    color = None

    def __init__(self, board, origin_coordinates, destination_coordinates, color):
        self.board = board
        self.origin_coordinates = origin_coordinates
        self.destination_coordinates = destination_coordinates
        self.color = color

    def get_board(self):
        return self.board

    def get_origin_coordinates(self):
        return self.origin_coordinates

    def get_destination_coordinates(self):
        return self.destination_coordinates

    def get_color(self):
        return self.color
