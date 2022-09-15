from Domain.Services.ValidateDropCommand import ValidateDropCommand
from Domain.Services.ValidateDropService import ValidateDropService


class DropPieceService:
    @staticmethod
    def execute(drop_piece_command):
        board = drop_piece_command.get_board()
        droppable_pieces = drop_piece_command.get_droppable_pieces()
        origin_coordinates = drop_piece_command.get_origin_coordinates()
        destination_coordinates = drop_piece_command.get_destination_coordinates()

        ValidateDropService.execute(
            ValidateDropCommand(
                board,
                droppable_pieces,
                origin_coordinates,
                destination_coordinates
            )
        )

        piece = droppable_pieces[origin_coordinates[1]]
        piece.convert()
        board.get_grid()[destination_coordinates[0]][destination_coordinates[1]].set_piece(
            piece
        )

        return droppable_pieces[origin_coordinates[1]]
