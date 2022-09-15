class InvalidDropPieceSelectedException(Exception):
    def __init__(self, message=None):
        print(message) if message else print('The entered coordinates do not correspond to an available captured piece')
