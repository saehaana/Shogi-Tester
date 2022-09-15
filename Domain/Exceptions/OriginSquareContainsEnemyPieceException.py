class OriginSquareContainsEnemyPieceException(Exception):
    def __init__(self, message=None):
        print(message) if message else print('The origin square contains an enemy piece')
