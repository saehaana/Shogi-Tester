class Square:
    piece = None
    promoting = False

    def __init__(self, promoting=False):
        self.promoting = promoting

    def set_piece(self, piece):
        self.piece = piece

    def remove_piece(self):
        self.piece = None

    def get_piece(self):
        return self.piece

    def is_empty(self):
        return self.piece is None

    def is_promoting(self):
        return self.promoting

    def to_string(self):
        return self.piece.to_string() if self.piece is not None else '  '
