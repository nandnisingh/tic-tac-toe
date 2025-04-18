from game_board import create_board, display_board, check_winner, check_draw
from player import define_players, player_move

def play_game():
    board = create_board()
    player1, player2 = define_players()
    current_player = player1

    while True:
        display_board(board)
        player_move(board, current_player)

        if check_winner(board, current_player['symbol']):
            display_board(board)
            print(f"{current_player['name']} wins!")
            break
        elif check_draw(board):
            display_board(board)
            print("It's a draw!")
            break

        
        current_player = player1 if current_player == player2 else player2


if __name__ == "__main__":
    play_game()
