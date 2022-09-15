from Domain.Exceptions.CoordinatesOutOfBoundsException import CoordinatesOutOfBoundsException
from Domain.Exceptions.InvalidCoordinateFormatException import InvalidCoordinateFormatException


class ValidateCoordinatesService:
    @staticmethod
    def execute(validate_coordinates_command):
        try:
            row = int(validate_coordinates_command.get_row_coordinate())
            col = int(validate_coordinates_command.get_column_coordinate())
        except ValueError:
            raise InvalidCoordinateFormatException()

        if row < 0 or col < 0 or \
                row >= validate_coordinates_command.get_rows() or col >= validate_coordinates_command.get_columns():
            raise CoordinatesOutOfBoundsException()
