from LLD.Chess.entities.piece.piece import Piece

"""
Update the functions with valid logic. We have created 
classes for only Knight and Bishop for this example, please
update valid_move and init methods for remaining pieces.
"""
class Pawn(Piece):
    def __init__(self, piecetype, color):
        super().__init__(piecetype, color)

    def valid_move(self, start_cell, end_cell):
        return super().valid_move(start_cell, end_cell)