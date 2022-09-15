from Domain.Exceptions.DestinationSquareOccupiedException import DestinationSquareOccupiedException
from Domain.Exceptions.InvalidDropPieceSelectedException import InvalidDropPieceSelectedException
from Domain.Services.ValidateCoordinatesCommand import ValidateCoordinatesCommand
from Domain.Services.ValidateCoordinatesService import ValidateCoordinatesService


class ValidateDropService:
    @staticmethod
    def execute(validate_drop_command):
        board = validate_drop_command.get_board()
        droppable_pieces = validate_drop_command.get_droppable_pieces()
        origin_coordinates = validate_drop_command.get_origin_coordinates()
        destination_coordinates = validate_drop_command.get_destination_coordinates()

        if origin_coordinates[0] != board.get_rows() or not (0 <= origin_coordinates[1] <= len(droppable_pieces)):
            raise InvalidDropPieceSelectedException()

        ValidateCoordinatesService.execute(
            ValidateCoordinatesCommand(
                board.get_rows(),
                board.get_columns(),
                destination_coordinates[0],
                destination_coordinates[1]
            )
        )

        if not board.is_square_empty(destination_coordinates[0], destination_coordinates[1]):
            raise DestinationSquareOccupiedException('The drop destination square contains another piece')
