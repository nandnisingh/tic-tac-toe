# player.py

def define_players():
    name1 = input("Enter name for Player 1 (X): ")
    name2 = input("Enter name for Player 2 (O): ")
    return {"name": name1, "symbol": "X"}, {"name": name2, "symbol": "O"}

def player_move(board, current_player):
    while True:
        try:
            move = int(input(f"{current_player['name']} ({current_player['symbol']}), enter your move (1-9): ")) - 1
            if board[move] == " ":
                board[move] = current_player['symbol']
                break
            else:
                print("That spot is already taken. Try again.")
        except (ValueError, IndexError):
            print("Invalid input. Choose a number from 1 to 9.")
