from LLD.Chess.entities.piece.enum.piecetype import PieceType
from LLD.Chess.entities.piece.piece import Piece


class Knight(Piece):
    def __init__(self, color):
        super.__init__(PieceType.Knight, color)
    
    def valid_move(self, start_cell, end_cell):
        piece = start_cell.piece

        if piece != PieceType.Knight:
            Exception("piece on start cell not equal to knight")
            return False
        
        start_row, start_col = start_cell.row, start_cell.col
        end_row, end_col = end_cell.row, end_cell.col

        directions = [(-2,1), (-2,-1), (2,1), (2,-1), (1,-2), (1,2), (-1,2), (-1,-2)]

        for x,y in directions:
            if end_row == start_row+x and end_col == start_col+y:
                return True
        
        return False
