from LLD.Chess.entities.piece.enum.piecetype import PieceType
from LLD.Chess.entities.piece.piece import Piece


class Bishop(Piece):
    def __init__(self, color):
        super().__init__(PieceType.BISHOP, color)
    
    def valid_move(self, start_cell, end_cell):
        curr_piece = start_cell.piece

        if curr_piece != PieceType.BISHOP:
            KeyError(f"Piece passed in move is not bishop. Piece provided = {curr_piece}")
            return False

        start_row, start_col = start_cell.row, start_cell.col
        end_row, end_col = end_cell.row, end_cell.col
    
        # Check if the cells lie on diagnol. For diagnol we can check absolute difference
        # between cell A and cell B rows and cols. For a diagnol distance travelled in rows
        # should be same as distance travelled in cols direction.
        if abs(end_row - start_row) == abs(end_col - start_col):
            return True
    
        return False
