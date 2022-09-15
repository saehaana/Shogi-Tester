from Domain.Services.ValidateMoveCommand import ValidateMoveCommand
from Domain.Services.ValidateMoveService import ValidateMoveService


class MovePieceService:
    @staticmethod
    def execute(move_piece_command):
        board = move_piece_command.get_board()
        origin_coordinates = move_piece_command.get_origin_coordinates()
        destination_coordinates = move_piece_command.get_destination_coordinates()
        color = move_piece_command.get_color()

        ValidateMoveService.execute(ValidateMoveCommand(board, origin_coordinates, destination_coordinates, color))

        board.get_grid()[destination_coordinates[0]][destination_coordinates[1]].set_piece(
            board.get_grid()[origin_coordinates[0]][origin_coordinates[1]].get_piece()
        )
        board.get_grid()[origin_coordinates[0]][origin_coordinates[1]].remove_piece()
