from Infrastructure.Services.BoardVisualizer import BoardVisualizer
from Domain.Exceptions.CoordinatesOutOfBoundsException import CoordinatesOutOfBoundsException
from Domain.Entities.Piece import Color
from Domain.Exceptions.InvalidCoordinateFormatException import InvalidCoordinateFormatException
from Domain.Services.ValidateCoordinatesCommand import ValidateCoordinatesCommand
from Infrastructure.Clients.Client import Client


class CommandLineClient(Client):
    def __init__(self, game):
        Client.__init__(self, game)
        self.game = game

    @staticmethod
    def prompt_move(rows, columns, turn, color, validate_coordinate_service):
        CommandLineClient.__print_turn_info(turn, color)

        origin_coordinates = CommandLineClient.__get_coordinates(
            rows + 1,
            columns,
            CommandLineClient.PROMPT_FROM,
            validate_coordinate_service
        )
        destination_coordinates = CommandLineClient.__get_coordinates(
            rows,
            columns,
            CommandLineClient.PROMPT_TO,
            validate_coordinate_service
        )

        return (int(origin_coordinates[0]), int(origin_coordinates[1])),\
               (int(destination_coordinates[0]), int(destination_coordinates[1]))

    @staticmethod
    def __print_turn_info(turn, color):
        next_color = CommandLineClient.COLOR_BLACK if color == Color.BLACK else CommandLineClient.COLOR_WHITE
        print('Turn ' + str(turn) + ' - ' + next_color)

    @staticmethod
    def __get_coordinates(rows, columns, text, validate_coordinate_service):
        while True:
            coordinates = input(text + '\n')
            try:
                validate_coordinates_command = ValidateCoordinatesCommand(
                    rows,
                    columns,
                    coordinates[0],
                    coordinates[1]
                )
                validate_coordinate_service.execute(validate_coordinates_command)
            except (IndexError, ValueError, CoordinatesOutOfBoundsException, InvalidCoordinateFormatException) as e:
                print(e)
                continue

            break

        return coordinates

    def show_game_state(self):
        BoardVisualizer.visualize(
            self.game.board,
            self.game.get_captured_by_color(Color.WHITE),
            self.game.get_captured_by_color(Color.BLACK)
        )
