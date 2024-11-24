from LLD.Chess.entities.chessboard.cell import Cell
from LLD.Chess.entities.piece.enum.piecetype import PieceType
from LLD.Chess.entities.piece.piecefactory import PieceFactory


class ChessBoard:
    _CHESSBOARD_SIZE = 8

    def __init__(self):
        self.board = self.initialize_board()
    
    def initialize_board(self):
        # Create an empty 8x8 board
        board = [[None]*self._CHESSBOARD_SIZE for _ in range(self._CHESSBOARD_SIZE)]

        # Initialize all the pieces on the empty board as per
        # standard rules.
        # 1. Assign pawn to entire 1 and 7 row.
        for i in range(self._CHESSBOARD_SIZE):
            # Create a white pawn for 1st row and assign it to the cell of the board
            white_pawn = PieceFactory.create_piece(PieceType.PAWN, "white")
            cell = Cell(1, i, white_pawn)
            board[1][i] = cell
        
            # Create a black pawn for 6th index row.
            black_pawn = PieceFactory.create_piece(PieceType.PAWN, "black")
            cell = Cell(6, i, black_pawn)
            board[6][i] = black_pawn

        # Place white and black rooks at correct position.
        white_rook = PieceFactory.create_piece(PieceType.ROOK, "white")
        black_rook = PieceFactory.create_piece(PieceType.ROOK, "black") 

        board[0][0] = Cell(0, 0, white_rook)
        board[0][7] = Cell(0, 7, white_rook)

        board[7][0] = Cell(7, 0, black_rook)
        board[7][7] = Cell(7, 7, black_rook)

        # Place Knight at correct position.
        white_knight = PieceFactory.create_piece(PieceType.KNIGHT, "white")
        black_knight = PieceFactory.create_piece(PieceType.KNIGHT, "black")

        board[0][1] = Cell(0, 1, white_knight)
        board[0][6] = Cell(0, 1, white_knight)

        board[7][1] = Cell(7, 1, black_knight)
        board[7][6] = Cell(7, 6, black_knight)

        # Place other pieces as well similar to above.