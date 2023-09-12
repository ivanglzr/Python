WINNER_COMBOS = [
  [0, 1, 2],
  [3, 4, 5],
  [6, 7, 8],
  [0, 3, 6],
  [1, 4, 7],
  [2, 5, 8],
  [0, 4, 8],
  [6, 4, 2]
]

board = [" ", " ", " ", " ", " ", " ", " ", " ", " "]

turn = "x"

def print_board():
    print(f"\n{board[0]} | {board[1]} | {board[2]}\n"
          f"= = = = =\n"
          f"{board[3]} | {board[4]} | {board[5]}\n"
          f"= = = = =\n"
          f"{board[6]} | {board[7]} | {board[8]}")

def check_winner():
    for WINNER_COMBO in WINNER_COMBOS:
        if board[WINNER_COMBO[0]] == board[WINNER_COMBO[1]] == board[WINNER_COMBO[2]] != " ":
            return True
    return False

print_board()

while True:
    win = False

    pos = int(input(f"\n{turn}. Escoge una casilla 1 - 9: ")) - 1

    if board[pos] != " ":
        print("\nEsa casilla ya está escogida")
    elif pos < 0 or pos > 8:
        print("\nLa casilla no existe")
    else:
        board[pos] = turn
        print_board()

        if check_winner():
            print(f"\n{turn} ha ganado")
            win = True

    if win:
        break

    turn = "x" if turn == "o" else "o"
