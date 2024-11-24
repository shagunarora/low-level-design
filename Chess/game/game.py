from logging import info
from LLD.Chess.entities.chessboard.cell import Cell
from LLD.Chess.entities.chessboard.chessboard import ChessBoard
from LLD.Chess.entities.piece.enum.piecetype import PieceType
from LLD.Chess.entities.piece.piece import Piece
from LLD.Chess.entities.player import Player
from LLD.Chess.game.enum.gamestate import GameState


class Game:
    def __init__(self, player1: Player, player2: Player):
        self.player1 = player1
        self.player2 = player2

        self.chessboard = ChessBoard().board
        self.player_turn = self.player1
        self.game_status = GameState.ACTIVE
        self.killed_pieces = []
    
    def player_move(self, player, start_row, start_col, end_row, end_col):
        if player != self.player_turn:
            Exception(f"Wrong player. Its {self.player_turn} player turn.")
            return False
    
        start_cell = self.chessboard[start_row][start_col]
        end_cell = self.chessboard[end_row][end_col]
    
        piece: Piece = start_cell.piece
        if piece.valid_move(start_cell, end_cell):
            # Check if end cell doesn't have same side piece already sitting.
            if end_cell.piece and end_cell.piece.color == player.side_assigned:
                Exception("Invalid move")
                return False
            
            # If current move killing king then change status of game 
            # as current player win.
            if end_cell.piece == PieceType.KING:
                info(f"{player.side_assigned} wins.")
                self.game_status = GameState.WHITE_WIN if player.side_assigned == "white" else GameState.BALCK_WIN
                # Remove piece from start cell and place it to end cell.
                start_cell.piece = None
                end_cell.piece = piece

                return True

            # If some piece at end cell, then that should be added to killed pieces.
            if end_cell.piece:
                self.killed_pieces.append(end_cell.piece)
                info(f"Player {player} killed {end_cell.piece.color} {end_cell.piece.piecetype}")    
            
            # Remove piece from start cell and place it to end cell.
            start_cell.piece = None
            end_cell.piece = piece
            self.player_turn = self.player_1 if player != self.player_1 else self.player_2
            return True

        return False 
    
    def set_status(self, status):
        self.game_status = status
    
    def abort_game(self): 
        self.game_status = GameState.ABORT
    
    def resign_game(self):
        self.game_status = GameState.RESIGNED
    