class DestinationSquareOccupiedException(Exception):
    def __init__(self, message=None):
        print(message) if message else print('The destination square is occupied by another piece')
