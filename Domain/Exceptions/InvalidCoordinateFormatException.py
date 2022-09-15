class InvalidCoordinateFormatException(Exception):
    def __init__(self, message=None):
        print(message) if message else print('The given coordinates must be two positive integers without space')
