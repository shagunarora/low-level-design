from LLD.Chess.entities.piece.enum.piecetype import PieceType
from LLD.Chess.entities.piece.pieces.bishop import Bishop
from LLD.Chess.entities.piece.pieces.knight import Knight


class PieceFactory:
    def create_piece(self, pieceType, color):
        if pieceType == PieceType.BISHOP:
            return Bishop(color)
        
        if pieceType == PieceType.KNIGHT:
            return Knight(color)
        
        # Similarly write for other chess pieces as well.
