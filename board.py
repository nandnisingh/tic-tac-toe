def create_board():
    return [" " for _ in range(9)]


def display_board(board):
    print()
    print(f"{board[0]} | {board[1]} | {board[2]}")
    print("--+---+--")
    print(f"{board[3]} | {board[4]} | {board[5]}")
    print("--+---+--")
    print(f"{board[6]} | {board[7]} | {board[8]}")
    print()


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


def check_winner(board, symbol):
    win_combos = [
        [0, 1, 2], [3, 4, 5], [6, 7, 8],  
        [0, 3, 6], [1, 4, 7], [2, 5, 8],  
        [0, 4, 8], [2, 4, 6]              
    ]
    return any(all(board[i] == symbol for i in combo) for combo in win_combos)


def check_draw(board):
    return " " not in board


def define_players():
    name1 = input("Enter name for Player 1 (X): ")
    name2 = input("Enter name for Player 2 (O): ")
    return {"name": name1, "symbol": "X"}, {"name": name2, "symbol": "O"}


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


play_game()