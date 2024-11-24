"""
Main script to run chess.

"""

from LLD.Chess.entities.player import Player
from LLD.Chess.game.enum.gamestate import GameState
from LLD.Chess.game.game import Game


def main():
    # Player id can be auto-assigned also. Ignoring for now this can be improved.
    player_1 = Player("Shagun", 1)
    player_2 = Player("Dhruv", 2)

    # Assign colors to players.
    player_1.set_side_color("white")
    player_2.set_side_color("black")

    game = Game(player_1, player_2)
    curr_player = player_1
    
    # Input:
    # 1. 1 sr sc er ec (user wants to play a move, input will be start_row, start_col and end_row and end_col)
    # 2. 2 (user wants to abort)
    # 3. 3 (user wants to resign)

    while game.game_status == GameState.ACTIVE:
        option = input()

        if option == 1:
            sr, sc, er, ec = input().split(' ')
            status = game.player_move(curr_player, sr, sc, er, ec) 
            if status:    
                curr_player = player_1 if curr_player != player_1 else player_2
            else:
                print("Invalid move. Input again.")
                
            continue   
            
        if option == 2:
            game.abort_game()
            continue

        if option == 3:
            game.resign_game()
            continue
            
        print("Invalid input.")
        
        