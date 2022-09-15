class CoordinatesOutOfBoundsException(Exception):
    def __init__(self, message=None):
        print(message) if message else print('The provided coordinates are out of the bounds of the board')
