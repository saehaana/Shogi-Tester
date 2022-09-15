from Domain.Exceptions.DestinationSquareOccupiedException import DestinationSquareOccupiedException
from Domain.Exceptions.InvalidMovementForPieceException import InvalidMovementForPieceException
from Domain.Exceptions.OriginSquareContainsEnemyPieceException import OriginSquareContainsEnemyPieceException
from Domain.Exceptions.OriginSquareEmptyException import OriginSquareEmptyException
from Domain.Exceptions.PieceMovementPathObstructedException import PieceMovementPathObstructedException
from Domain.Services.ValidateCoordinatesCommand import ValidateCoordinatesCommand
from Domain.Services.ValidateCoordinatesService import ValidateCoordinatesService


class ValidateMoveService:
    @staticmethod
    def execute(validate_move_command):
        board = validate_move_command.get_board()
        origin_coordinates = validate_move_command.get_origin_coordinates()
        destination_coordinates = validate_move_command.get_destination_coordinates()
        color = validate_move_command.get_color()

        ValidateCoordinatesService.execute(
            ValidateCoordinatesCommand(
                board.get_rows(),
                board.get_columns(),
                origin_coordinates[0],
                origin_coordinates[1]
            )
        )
        ValidateCoordinatesService.execute(
            ValidateCoordinatesCommand(
                board.get_rows(),
                board.get_columns(),
                destination_coordinates[0],
                destination_coordinates[1]
            )
        )

        if board.is_square_empty(origin_coordinates[0], origin_coordinates[1]):
            raise OriginSquareEmptyException()

        if not board.is_square_occupied_by_friendly(origin_coordinates[0], origin_coordinates[1], color):
            raise OriginSquareContainsEnemyPieceException()

        if board.is_square_occupied_by_friendly(destination_coordinates[0], destination_coordinates[1], color):
            raise DestinationSquareOccupiedException("Can't move to a square occupied by a friendly piece")

        if not board.is_square_reachable_by_piece(
                origin_coordinates[0],
                origin_coordinates[1],
                destination_coordinates[0],
                destination_coordinates[1],
                color
        ):
            raise InvalidMovementForPieceException()

        if board.is_path_obstructed(
                origin_coordinates[0],
                origin_coordinates[1],
                destination_coordinates[0],
                destination_coordinates[1]
        ):
            raise PieceMovementPathObstructedException()
