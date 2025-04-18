def define_players():
    name1 = input("Enter name for Player 1 (X): ")
    name2 = input("Enter name for Player 2 (O): ")
    return {"name": name1, "symbol": "X"}, {"name": name2, "symbol": "O"}
