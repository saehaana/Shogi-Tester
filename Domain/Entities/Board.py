from Domain.Entities.Bishop import Bishop
from Domain.Entities.Lance import Lance
from Domain.Entities.Rook import Rook
from Infrastructure.Services.BoardVisualizer import BoardVisualizer
from Domain.Entities.Piece import Color
from Domain.Entities.Square import Square


class Board:
    LEFT_LANCE_INDEX = 0
    RIGHT_LANCE_INDEX = -1
    LEFT_KNIGHT_INDEX = 1
    RIGHT_KNIGHT_INDEX = -2
    LEFT_SILVER_GENERAL_INDEX = 2
    RIGHT_SILVER_GENERAL_INDEX = -3
    LEFT_GOLD_GENERAL_INDEX = 3
    RIGHT_GOLD_GENERAL_INDEX = -4
    KING_INDEX = 4
    WHITE_BISHOP_INDEX = -2
    WHITE_ROOK_INDEX = 1
    BLACK_BISHOP_INDEX = 1
    BLACK_ROOK_INDEX = -2

    columns = -1
    rows = -1
    grid = None

    def __init__(self, rows, columns):
        if rows <= 0 or columns <= 0:
            raise ValueError

        self.rows = rows
        self.columns = columns
        self.grid = [[Square() for i in range(columns)] for j in range(rows)]

    def get_rows(self):
        return self.rows

    def get_columns(self):
        return self.columns

    def get_grid(self):
        return self.grid

    def initialize_board(self, piece_factory):
        self.create_pieces(piece_factory, Color.WHITE)
        self.create_pieces(piece_factory, Color.BLACK)

    def create_pieces(self, piece_factory, color):
        if color == Color.WHITE:
            first_row = 0
            second_row = 1
            third_row = 2

            self.grid[second_row][self.WHITE_BISHOP_INDEX].set_piece(piece_factory.create_bishop(color))
            self.grid[second_row][self.WHITE_ROOK_INDEX].set_piece(piece_factory.create_rook(color))
        else:
            first_row = -1
            second_row = -2
            third_row = -3

            self.grid[second_row][self.BLACK_BISHOP_INDEX].set_piece(piece_factory.create_bishop(color))
            self.grid[second_row][self.BLACK_ROOK_INDEX].set_piece(piece_factory.create_rook(color))

        self.grid[first_row][self.LEFT_LANCE_INDEX].set_piece(piece_factory.create_lance(color))
        self.grid[first_row][self.RIGHT_LANCE_INDEX].set_piece(piece_factory.create_lance(color))

        self.grid[first_row][self.LEFT_KNIGHT_INDEX].set_piece(piece_factory.create_knight(color))
        self.grid[first_row][self.RIGHT_KNIGHT_INDEX].set_piece(piece_factory.create_knight(color))

        self.grid[first_row][self.LEFT_SILVER_GENERAL_INDEX].set_piece(piece_factory.create_silver_general(color))
        self.grid[first_row][self.RIGHT_SILVER_GENERAL_INDEX].set_piece(piece_factory.create_silver_general(color))

        self.grid[first_row][self.LEFT_GOLD_GENERAL_INDEX].set_piece(piece_factory.create_gold_general(color))
        self.grid[first_row][self.RIGHT_GOLD_GENERAL_INDEX].set_piece(piece_factory.create_gold_general(color))

        self.grid[first_row][self.KING_INDEX].set_piece(piece_factory.create_king(color))

        for i in range(self.columns):
            self.grid[third_row][i].set_piece(piece_factory.create_pawn(color))

    def is_square_empty(self, row, col):
        return self.grid[row][col].is_empty()

    def is_square_occupied_by_friendly(self, row, col, color):
        return not self.grid[row][col].is_empty() and self.grid[row][col].get_piece().get_color() == color

    def is_square_occupied_by_enemy(self, row, col, color):
        return not self.grid[row][col].is_empty() and self.grid[row][col].get_piece().get_color() != color

    def is_square_reachable_by_piece(self, origin_row, origin_col, destination_row, destination_col, color):
        piece = self.grid[origin_row][origin_col].get_piece()
        return piece.can_reach(origin_row, origin_col, destination_row, destination_col, color)

    def is_path_obstructed(self, origin_row, origin_col, destination_row, destination_col):
        piece = self.grid[origin_row][origin_col].get_piece()

        if isinstance(piece, Bishop):
            row_direction = -1 if origin_row > destination_row else 1
            col_direction = -1 if origin_col > destination_col else 1

            distance = abs(origin_row - destination_row) - 1
            for i in range(distance):
                origin_row += row_direction
                origin_col += col_direction
                if not self.grid[origin_row][origin_col].is_empty():
                    return True

        if isinstance(piece, Lance):
            row_direction = -1 if origin_row > destination_row else 1

            distance = abs(origin_row - destination_row) - 1
            for i in range(distance):
                origin_row += row_direction
                if not self.grid[origin_row][origin_col].is_empty():
                    return True

        if isinstance(piece, Rook):
            if origin_row == destination_row:
                col_direction = -1 if origin_col > destination_col else 1

                distance = abs(origin_col - destination_col) - 1
                for i in range(distance):
                    origin_col += col_direction
                    if not self.grid[origin_row][origin_col].is_empty():
                        return True
            else:
                row_direction = -1 if origin_row > destination_row else 1

                distance = abs(origin_row - destination_row) - 1
                for i in range(distance):
                    origin_row += row_direction
                    if not self.grid[origin_row][origin_col].is_empty():
                        return True

        return False

    def get_piece_in_square(self, row, col):
        return self.grid[row][col].get_piece()

    def to_string(self, captured_white=None, captured_black=None):
        BoardVisualizer.visualize(self.grid, captured_white, captured_black)
