from Domain.Entities.Bishop import Bishop
from Domain.Entities.GoldGeneral import GoldGeneral
from Domain.Entities.King import King
from Domain.Entities.Knight import Knight
from Domain.Entities.Lance import Lance
from Domain.Entities.Pawn import Pawn
from Domain.Entities.Rook import Rook
from Domain.Entities.SilverGeneral import SilverGeneral


class PieceFactory:
    @staticmethod
    def create_bishop(color):
        return Bishop(color)

    @staticmethod
    def create_gold_general(color):
        return GoldGeneral(color)

    @staticmethod
    def create_king(color):
        return King(color)

    @staticmethod
    def create_knight(color):
        return Knight(color)

    @staticmethod
    def create_lance(color):
        return Lance(color)

    @staticmethod
    def create_pawn(color):
        return Pawn(color)

    @staticmethod
    def create_rook(color):
        return Rook(color)

    @staticmethod
    def create_silver_general(color):
        return SilverGeneral(color)
