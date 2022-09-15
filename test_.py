#CMSC 425
#Ausawin Saehaan
#Test file for all classes within GoldGeneral.py, SilverGeneral.py, Knight.py, Pawn.py, ValidateMoveService.py
import pytest
import unittest

#ValidateMoveService.py imports
from Domain.Entities.Board import Board
from Domain.Entities.Piece import Color
from Domain.Entities.PieceFactory import PieceFactory
from Domain.Services.ValidateMoveCommand import ValidateMoveCommand
from Domain.Services.ValidateMoveService import ValidateMoveService
from Domain.Exceptions.OriginSquareEmptyException import OriginSquareEmptyException
from Domain.Exceptions.OriginSquareContainsEnemyPieceException import OriginSquareContainsEnemyPieceException
from Domain.Exceptions.DestinationSquareOccupiedException import DestinationSquareOccupiedException
from Domain.Exceptions.InvalidMovementForPieceException import InvalidMovementForPieceException
from Domain.Exceptions.PieceMovementPathObstructedException import PieceMovementPathObstructedException

#GoldGeneral.py imports
from Domain.Entities.GoldGeneral import GoldGeneral
#SilverGeneral.py imports
from Domain.Entities.SilverGeneral import SilverGeneral
#Knight.py imports
from Domain.Entities.Knight import Knight
#Pawn.py imports
from Domain.Entities.Pawn import Pawn
from Domain.Entities.King import King
from Domain.Entities.Bishop import Bishop



#ValidateMoveService.py
class TestValidateMoveService(unittest.TestCase):
    #enter game start settings
    board = Board(9, 9) #board of 9 rows and columns
    board.initialize_board(PieceFactory()) #PieceFactory creates all game pieces

    #return valid since piece being moved is white
    def test_execute_validWHITE(self):
        #ValidateMoveCommand has def: __init__(self, board, origin_coordinates, destination_coordinates, color)
        ValidateMoveService.execute(ValidateMoveCommand(self.board, (0, 0), (1, 0), Color.WHITE))
        
    #return valid since piece being moved is black 
    def test_execute_validBLACK(self):
        ValidateMoveService.execute(ValidateMoveCommand(self.board, (6, 0), (5, 0), Color.BLACK))
        
    def test_is_square_empty(self):
        #prints message 'The origin square is empty'
        with self.assertRaises(OriginSquareEmptyException): 
            ValidateMoveService.execute(ValidateMoveCommand(self.board, (1, 0), (3, 0), Color.WHITE))
            
    def test_is_square_occupied_by_enemy(self):
        #prints message 'The origin square contains an enemy piece'
        with self.assertRaises(OriginSquareContainsEnemyPieceException):
            #white piece selection but coordinates of black piece
            ValidateMoveService.execute(ValidateMoveCommand(self.board, (6, 0), (5, 0), Color.WHITE))
            
    def test_is_square_occupied_by_friendly(self):
        #prints message 'Can't move to a square occupied by a friendly piece'
        with self.assertRaises(DestinationSquareOccupiedException): 
            #attempt to move black bishop to space but contains black pawn
            ValidateMoveService.execute(ValidateMoveCommand(self.board, (7, 1), (6, 1), Color.BLACK))

    def test_is_square_reachable_by_piece(self):
        #prints message 'The destination square is not reachable by the selected piece'
        with self.assertRaises(InvalidMovementForPieceException):
            #attempt to move white pawn 3 spaces forward (can only move 1 or 2 spaces forward)
            ValidateMoveService.execute(ValidateMoveCommand(self.board, (2, 4), (5, 4), Color.WHITE))

    def test_is_path_obstructed(self):
        #prints message 'The path of the movement is obstructed by other pieces'
        with self.assertRaises(PieceMovementPathObstructedException):
            #attempt to move black lance(rook) validly to an empty space, but friendly pawn is in the way
            ValidateMoveService.execute(ValidateMoveCommand(self.board, (8, 0), (5, 0), Color.BLACK))

#GoldGeneral.py
class TestGoldGeneral(unittest.TestCase):
    #Block1 choices 
    descriptionA1 = "Gold General"
    representationB1 = 'G'

    #Block2 choices 
    descriptionA2 = "Silver General"
    representationB2 = 'S'

    #tests for function's characteristics
    #Base Choice test
    #Base Choice blocks {A1,B1} : TT
    def test_initTT(self):
        #assertEqual(block assertion, class GoldGeneral value)
        self.assertEqual(self.descriptionA1, GoldGeneral(Color.WHITE).description)
        self.assertEqual(self.representationB1, GoldGeneral(Color.WHITE).representation)
        
    #{A2,B1} : FT
    def test_initFT(self):
        gamePiece = GoldGeneral(Color.WHITE)
        self.assertNotEqual(self.descriptionA2, gamePiece.description)
        self.assertEqual(self.representationB1, gamePiece.representation)

    #{A1,B2} : TF
    def test_initTF(self):
        gamePiece = GoldGeneral(Color.WHITE)
        self.assertEqual(self.descriptionA1, gamePiece.description)
        self.assertNotEqual(self.representationB2, gamePiece.representation)

    #{A2,B2} : FF
    def test_initFF(self):
        gamePiece = GoldGeneral(Color.WHITE)
        self.assertNotEqual(self.descriptionA2, gamePiece.description)
        self.assertNotEqual(self.representationB2, gamePiece.representation)

    #tests for can_reach()
    def testMovement(self):
        gamePiece = GoldGeneral(Color.BLACK)
        gamePieceWhite = GoldGeneral(Color.WHITE)
        origin_rowC1 = 8
        origin_colC1 = 3
        #can_reach(self,origin_row,origin_col,destination_row,destination_col, color)
        #Black piece moveset
        self.assertTrue(gamePiece.can_reach(origin_rowC1,origin_colC1,7,3,gamePiece.get_color())) #move forward
        self.assertTrue(gamePiece.can_reach(origin_rowC1,origin_colC1,8,2,gamePiece.get_color())) #move left
        self.assertTrue(gamePiece.can_reach(origin_rowC1,origin_colC1,8,4,gamePiece.get_color())) #move right
        self.assertTrue(gamePiece.can_reach(origin_rowC1,origin_colC1,7,4,gamePiece.get_color())) #move diagonal (up right)
        self.assertTrue(gamePiece.can_reach(origin_rowC1,origin_colC1,7,2,gamePiece.get_color())) #move diagonal (up left)
        
        origin_rowC2 = 7
        origin_colC2 = 3
        self.assertFalse(gamePiece.can_reach(origin_rowC2,origin_colC2,8,2,gamePiece.get_color())) #move diagonal (down left)
        self.assertFalse(gamePiece.can_reach(origin_rowC2,origin_colC2,8,4,gamePiece.get_color())) #move diagonal (down right)

        #White piece moveset
        self.assertTrue(gamePieceWhite.can_reach(origin_rowC1,origin_colC1,8,4,gamePieceWhite.get_color())) #move right
        self.assertFalse(gamePieceWhite.can_reach(origin_rowC1,origin_colC1,6,3,gamePieceWhite.get_color())) #move 2 spaces back

        
#SilverGeneral.py
class TestSilverGeneral(unittest.TestCase):
    #Block1 choices 
    descriptionA1 = "Silver General"
    representationB1 = 'S'

    #Block2 choices 
    descriptionA2 = "Gold General"
    representationB2 = 'G'

    #{A1,B1} : TT
    def test_initTT(self):
        gamePiece = SilverGeneral(Color.WHITE)
        self.assertEqual(self.descriptionA1, gamePiece.description)
        self.assertEqual(self.representationB1, gamePiece.representation)
        
    #{A2,B1} : FT
    def test_initFT(self):
        gamePiece = SilverGeneral(Color.WHITE)
        self.assertNotEqual(self.descriptionA2, gamePiece.description)
        self.assertEqual(self.representationB1, gamePiece.representation)

    #{A1,B2} : TF
    def test_initTF(self):
        gamePiece = SilverGeneral(Color.WHITE)
        self.assertEqual(self.descriptionA1, gamePiece.description)
        self.assertNotEqual(self.representationB2, gamePiece.representation)

    #{A2,B2} : FF
    def test_initFF(self):
        gamePiece = SilverGeneral(Color.WHITE)
        self.assertNotEqual(self.descriptionA2, gamePiece.description)
        self.assertNotEqual(self.representationB2, gamePiece.representation)

    #tests for can_reach()
    def testMovement(self):
        gamePiece = SilverGeneral(Color.BLACK)
        gamePieceWhite = SilverGeneral(Color.WHITE)
        
        origin_row = 7
        origin_col = 2
        #can_reach(self,origin_row,origin_col,destination_row,destination_col, color)
        #Black piece moveset
        self.assertTrue(gamePiece.can_reach(origin_row,origin_col,6,2,gamePiece.get_color())) #move forward
        self.assertTrue(gamePiece.can_reach(origin_row,origin_col,6,3,gamePiece.get_color())) #move diagonal (up right)
        self.assertTrue(gamePiece.can_reach(origin_row,origin_col,6,1,gamePiece.get_color())) #move diagonal (up left)
        self.assertTrue(gamePiece.can_reach(origin_row,origin_col,8,1,gamePiece.get_color())) #move diagonal (down left)
        self.assertTrue(gamePiece.can_reach(origin_row,origin_col,8,3,gamePiece.get_color())) #move diagonal (down right)
        
        self.assertFalse(gamePiece.can_reach(origin_row,origin_col,7,1,gamePiece.get_color())) #move left
        self.assertFalse(gamePiece.can_reach(origin_row,origin_col,7,3,gamePiece.get_color())) #move right
        self.assertFalse(gamePiece.can_reach(origin_row,origin_col,8,2,gamePiece.get_color())) #move backward

        #White piece moveset
        self.assertTrue(gamePieceWhite.can_reach(origin_row,origin_col,6,3,gamePieceWhite.get_color())) #move down right
        self.assertFalse(gamePieceWhite.can_reach(origin_row,origin_col,8,4,gamePieceWhite.get_color()))
        
        

#Knight.py
class TestKnight(unittest.TestCase):
    #Block1 choices 
    descriptionA1 = "Knight"
    representationB1 = 'N'

    #Block2 choices 
    descriptionA2 = "Lance"
    representationB2 = 'L'

    #{A1,B1} : TT
    def test_initTT(self):
        gamePiece = Knight(Color.WHITE)
        self.assertEqual(self.descriptionA1, gamePiece.description)
        self.assertEqual(self.representationB1, gamePiece.representation)
        
    #{A2,B1} : FT
    def test_initFT(self):
        gamePiece = Knight(Color.WHITE)
        self.assertNotEqual(self.descriptionA2, gamePiece.description)
        self.assertEqual(self.representationB1, gamePiece.representation)

    #{A1,B2} : TF
    def test_initTF(self):
        gamePiece = Knight(Color.WHITE)
        self.assertEqual(self.descriptionA1, gamePiece.description)
        self.assertNotEqual(self.representationB2, gamePiece.representation)

    #{A2,B2} : FF
    def test_initFF(self):
        gamePiece = Knight(Color.WHITE)
        self.assertNotEqual(self.descriptionA2, gamePiece.description)
        self.assertNotEqual(self.representationB2, gamePiece.representation)

    #tests for can_reach()
    def testMovement(self):
        gamePiece = Knight(Color.WHITE)
        gamePieceBlack = Knight(Color.BLACK)
        origin_row = 1
        origin_col = 4
        #can_reach(self,origin_row,origin_col,destination_row,destination_col, color)
        #White piece moveset
        self.assertTrue(gamePiece.can_reach(origin_row,origin_col,3,3,gamePiece.get_color())) #move L-shape left
        self.assertTrue(gamePiece.can_reach(origin_row,origin_col,3,5,gamePiece.get_color())) #move L-shape right
        
        self.assertFalse(gamePiece.can_reach(origin_row,origin_col,2,4,gamePiece.get_color())) #move forward
        self.assertFalse(gamePiece.can_reach(origin_row,origin_col,1,3,gamePiece.get_color())) #move left
        self.assertFalse(gamePiece.can_reach(origin_row,origin_col,1,5,gamePiece.get_color())) #move right
        self.assertFalse(gamePiece.can_reach(origin_row,origin_col,0,4,gamePiece.get_color())) #move backward
        self.assertFalse(gamePiece.can_reach(origin_row,origin_col,2,5,gamePiece.get_color())) #move diagonal (up right)
        self.assertFalse(gamePiece.can_reach(origin_row,origin_col,2,3,gamePiece.get_color())) #move diagonal (up left)
        self.assertFalse(gamePiece.can_reach(origin_row,origin_col,0,3,gamePiece.get_color())) #move diagonal (down left)
        self.assertFalse(gamePiece.can_reach(origin_row,origin_col,0,5,gamePiece.get_color())) #move diagonal (down right)

        #Black piece moveset
        origin_row = 8
        origin_col = 1
        self.assertTrue(gamePieceBlack.can_reach(origin_row,origin_col,6,2,gamePieceBlack.get_color())) #move L-shape right
        self.assertFalse(gamePieceBlack.can_reach(origin_row,origin_col,1,5,gamePieceBlack.get_color())) #unreachable
        
#Pawn.py
class TestPawn(unittest.TestCase):
    #Block1 choices 
    descriptionA1 = "Pawn"
    representationB1 = 'P'

    #Block2 choices 
    descriptionA2 = "King"
    representationB2 = 'K'

    #Block3 choices 
    descriptionA3 = "Bishop"
    representationB3 = 'B'
    
    #{A1,B1,C1}  
    def test_init1(self):
        piecePawn = Pawn(Color.WHITE)
        piecePawnBlack = Pawn(Color.BLACK)
        origin_row = 2
        origin_col = 4

        self.assertEqual(self.descriptionA1, piecePawn.description)
        self.assertEqual(self.representationB1, piecePawn.representation)
        #White Pawn moveset
        self.assertTrue(piecePawn.can_reach(origin_row,origin_col,3,4,piecePawn.get_color())) # move 1 space forward
        self.assertFalse(piecePawn.can_reach(origin_row,origin_col,1,4,piecePawn.get_color())) # move 1 space back
        #Black Pawn moveset
        self.assertTrue(piecePawnBlack.can_reach(origin_row,origin_col,1,4,piecePawnBlack.get_color())) # move 1 space forward
        self.assertFalse(piecePawnBlack.can_reach(origin_row,origin_col,3,4,piecePawnBlack.get_color())) # move 1 space back
        
    #{A2,B2,C2}  
    def test_init2(self):
        pieceKing = King(Color.WHITE)
        pieceKingBlack = King(Color.BLACK)
        origin_row = 2
        origin_col = 4
        
        self.assertEqual(self.descriptionA2, pieceKing.description)
        self.assertEqual(self.representationB2, pieceKing.representation)
        #White King moveset
        self.assertTrue(pieceKing.can_reach(origin_row,origin_col,3,4,pieceKing.get_color())) # move forward
        self.assertTrue(pieceKing.can_reach(origin_row,origin_col,1,4,pieceKing.get_color())) # move backward
        self.assertTrue(pieceKing.can_reach(origin_row,origin_col,2,5,pieceKing.get_color())) # move left
        self.assertTrue(pieceKing.can_reach(origin_row,origin_col,2,3,pieceKing.get_color())) # move right
        self.assertTrue(pieceKing.can_reach(origin_row,origin_col,3,3,pieceKing.get_color())) # move diagonal up left
        self.assertTrue(pieceKing.can_reach(origin_row,origin_col,3,5,pieceKing.get_color())) # move diagonal up right
        self.assertTrue(pieceKing.can_reach(origin_row,origin_col,1,3,pieceKing.get_color())) # move diagonal down left
        self.assertTrue(pieceKing.can_reach(origin_row,origin_col,1,5,pieceKing.get_color())) # move diagonal down right
        self.assertFalse(pieceKing.can_reach(origin_row,origin_col,4,4,pieceKing.get_color())) # move forward 2 spaces

        #Black King moveset
        self.assertTrue(pieceKing.can_reach(origin_row,origin_col,3,4,pieceKing.get_color())) # move forward
        self.assertFalse(pieceKing.can_reach(origin_row,origin_col,0,4,pieceKing.get_color())) # move forward 2 spaces
        

    #{A3,B3,C3}  
    def test_init3(self):
        pieceBishop = Bishop(Color.WHITE)
        pieceBishopBlack = Bishop(Color.BLACK)
        origin_row = 2
        origin_col = 4

        self.assertEqual(self.descriptionA3, pieceBishop.description)
        self.assertEqual(self.representationB3, pieceBishop.representation)
        #White Bishop moveset
        self.assertTrue(pieceBishop.can_reach(origin_row,origin_col,3,3,pieceBishop.get_color())) # move diagonal up left 1 space
        self.assertTrue(pieceBishop.can_reach(origin_row,origin_col,3,5,pieceBishop.get_color())) # move diagonal up right 1 space
        self.assertTrue(pieceBishop.can_reach(origin_row,origin_col,1,3,pieceBishop.get_color())) # move diagonal down left 1 space
        self.assertTrue(pieceBishop.can_reach(origin_row,origin_col,1,5,pieceBishop.get_color())) # move diagonal down right 1 space
        self.assertTrue(pieceBishop.can_reach(origin_row,origin_col,5,1,pieceBishop.get_color())) # move diagonal up left 3 spaces
        self.assertTrue(pieceBishop.can_reach(origin_row,origin_col,5,7,pieceBishop.get_color())) # move diagonal up right 3 spaces
        self.assertTrue(pieceBishop.can_reach(origin_row,origin_col,0,6,pieceBishop.get_color())) # move diagonal down left 2 spaces
        self.assertTrue(pieceBishop.can_reach(origin_row,origin_col,0,2,pieceBishop.get_color())) # move diagonal down right 2 spaces
        self.assertFalse(pieceBishop.can_reach(origin_row,origin_col,2,3,pieceBishop.get_color())) # move left
        
        #Black Bishop moveset
        self.assertTrue(pieceBishopBlack.can_reach(origin_row,origin_col,1,3,pieceBishopBlack.get_color())) # move diagonal up left 1 space
        self.assertFalse(pieceBishopBlack.can_reach(origin_row,origin_col,2,5,pieceBishopBlack.get_color())) # move right
   

#allows running all tests by running file
if __name__ == '__main__':
    unittest.main()
