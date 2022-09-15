class InvalidMovementForPieceException(Exception):
    def __init__(self, message=None):
        print(message) if message else print('The destination square is not reachable by the selected piece')
