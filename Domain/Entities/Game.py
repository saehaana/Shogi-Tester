import datetime

from Domain.Entities.Piece import Color


class Game:
    board = None
    piece_factory = None
    start_date = None
    end_date = None
    pieces_white = None
    pieces_black = None
    captured_white = None
    captured_black = None

    finished = False
    winner = None
    turn = None
    current_player = None

    def __init__(self, board, piece_factory):
        self.board = board
        self.piece_factory = piece_factory

    def start_game(self):
        self.start_date = datetime.datetime.now()
        self.board.initialize_board(self.piece_factory)
        self.turn = 1
        self.current_player = Color.WHITE

        self.captured_white = []
        self.captured_black = []

    def finish_game(self):
        self.end_date = datetime.datetime.now()
        self.finished = True

    def is_finished(self):
        return self.finished

    def get_turn(self):
        return self.turn

    def get_current_player(self):
        return self.current_player

    def next_turn(self):
        self.turn += 1
        self.current_player = Color.WHITE if self.current_player == Color.BLACK else Color.BLACK

    def add_captured(self, color, piece):
        if color == Color.WHITE:
            self.captured_white.append(piece)
        else:
            self.captured_black.append(piece)

    def remove_captured(self, color, piece):
        if color == Color.WHITE:
            self.captured_white.remove(piece)
        else:
            self.captured_black.remove(piece)

    def get_captured_by_color(self, color):
        return self.captured_white if color == Color.WHITE else self.captured_black

    def to_string(self):
        self.board.to_string(self.captured_white, self.captured_black)