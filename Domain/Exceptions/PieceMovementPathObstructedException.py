class PieceMovementPathObstructedException(Exception):
    def __init__(self, message=None):
        print(message) if message else print('The path of the movement is obstructed by other pieces')
