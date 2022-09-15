from Application.Services.DropPieceCommand import DropPieceCommand
from Application.Services.DropPieceService import DropPieceService
from Application.Services.MoveAndCapturePieceCommand import MoveAndCapturePieceCommand
from Application.Services.MoveAndCapturePieceService import MoveAndCapturePieceService
from Application.Services.MovePieceCommand import MovePieceCommand
from Domain.Exceptions.InvalidDropPieceSelectedException import InvalidDropPieceSelectedException
from Domain.Exceptions.PieceMovementPathObstructedException import PieceMovementPathObstructedException
from Domain.Services.ValidateCoordinatesService import ValidateCoordinatesService
from Domain.Entities.Board import Board
from Domain.Exceptions.CoordinatesOutOfBoundsException import CoordinatesOutOfBoundsException
from Domain.Exceptions.DestinationSquareOccupiedException import DestinationSquareOccupiedException
from Domain.Exceptions.InvalidMovementForPieceException import InvalidMovementForPieceException
from Domain.Exceptions.OriginSquareContainsEnemyPieceException import OriginSquareContainsEnemyPieceException
from Domain.Exceptions.OriginSquareEmptyException import OriginSquareEmptyException
from Domain.Entities.Game import Game
from Application.Services.MovePieceService import MovePieceService
from Domain.Entities.PieceFactory import PieceFactory
from Infrastructure.Clients.CommandLineClient import CommandLineClient


ROWS = 9
COLUMNS = 9
CAPTURED_ROW_INDEX = 9

board = Board(ROWS, COLUMNS)
piece_factory = PieceFactory()
drop_piece_service = DropPieceService()
move_piece_service = MovePieceService()
move_and_capture_piece_service = MoveAndCapturePieceService()
validate_coordinates_service = ValidateCoordinatesService()

command_line_client = CommandLineClient(Game(board, piece_factory))
command_line_client.get_game().start_game()

while not command_line_client.get_game().is_finished():
    command_line_client.show_game_state()
    color = command_line_client.get_game().get_current_player()
    captured = None

    while True:
        try:
            origin_coordinates, destination_coordinates = CommandLineClient.prompt_move(
                board.get_rows(),
                board.get_columns(),
                command_line_client.get_game().get_turn(),
                color,
                validate_coordinates_service
            )

            if CAPTURED_ROW_INDEX == origin_coordinates[0]:
                dropped = drop_piece_service.execute(
                    DropPieceCommand(
                        board,
                        command_line_client.get_game().get_captured_by_color(color),
                        origin_coordinates,
                        destination_coordinates
                    )
                )
                command_line_client.get_game().remove_captured(color, dropped)
            elif board.is_square_occupied_by_enemy(destination_coordinates[0], destination_coordinates[1], color):
                captured = move_and_capture_piece_service.execute(
                    MoveAndCapturePieceCommand(board, origin_coordinates, destination_coordinates, color)
                )
                command_line_client.get_game().add_captured(color, captured)
            else:
                move_piece_service.execute(MovePieceCommand(board, origin_coordinates, destination_coordinates, color))
        except (
                CoordinatesOutOfBoundsException,
                DestinationSquareOccupiedException,
                InvalidDropPieceSelectedException,
                InvalidMovementForPieceException,
                OriginSquareEmptyException,
                OriginSquareContainsEnemyPieceException,
                PieceMovementPathObstructedException
        ) as e:
            print(e)
            continue

        break

    command_line_client.get_game().next_turn()
