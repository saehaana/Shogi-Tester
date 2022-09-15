from Domain.Services.ValidateMoveCommand import ValidateMoveCommand
from Domain.Services.ValidateMoveService import ValidateMoveService


class MoveAndCapturePieceService:
    @staticmethod
    def execute(move_and_capture_piece_command):
        board = move_and_capture_piece_command.get_board()
        origin_coordinates = move_and_capture_piece_command.get_origin_coordinates()
        destination_coordinates = move_and_capture_piece_command.get_destination_coordinates()
        color = move_and_capture_piece_command.get_color()

        ValidateMoveService.execute(ValidateMoveCommand(board, origin_coordinates, destination_coordinates, color))

        captured = board.get_piece_in_square(
            destination_coordinates[0],
            destination_coordinates[1]
        )

        board.get_grid()[destination_coordinates[0]][destination_coordinates[1]].set_piece(
            board.get_grid()[origin_coordinates[0]][origin_coordinates[1]].get_piece()
        )
        board.get_grid()[origin_coordinates[0]][origin_coordinates[1]].remove_piece()

        return captured
