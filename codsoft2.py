import math

board = [" "] * 9


def print_board():
    print()
    for i in range(0, 9, 3):
        print(" " + " | ".join(board[i:i+3]))
        if i < 6:
            print("---+---+---")
    print()


def check_winner(player):
    combinations = [
        (0, 1, 2), (3, 4, 5), (6, 7, 8),
        (0, 3, 6), (1, 4, 7), (2, 5, 8),
        (0, 4, 8), (2, 4, 6)
    ]

    return any(
        board[a] == board[b] == board[c] == player
        for a, b, c in combinations
    )


def is_draw():
    return " " not in board


def minimax(is_maximizing):
    if check_winner("O"):
        return 1

    if check_winner("X"):
        return -1

    if is_draw():
        return 0

    if is_maximizing:
        best_score = -math.inf

        for i in range(9):
            if board[i] == " ":
                board[i] = "O"
                score = minimax(False)
                board[i] = " "
                best_score = max(best_score, score)

        return best_score

    else:
        best_score = math.inf

        for i in range(9):
            if board[i] == " ":
                board[i] = "X"
                score = minimax(True)
                board[i] = " "
                best_score = min(best_score, score)

        return best_score


def best_move():
    best_score = -math.inf
    move = None

    for i in range(9):
        if board[i] == " ":
            board[i] = "O"
            score = minimax(False)
            board[i] = " "

            if score > best_score:
                best_score = score
                move = i

    return move


print("TIC-TAC-TOE AI")
print("You = X")
print("AI = O")

while True:
    print_board()

    try:
        position = int(input("Enter position (1-9): ")) - 1

        if position < 0 or position > 8 or board[position] != " ":
            print("Invalid position!")
            continue

        board[position] = "X"

    except ValueError:
        print("Please enter a number from 1 to 9.")
        continue

    if check_winner("X"):
        print_board()
        print("🎉 You win!")
        break

    if is_draw():
        print_board()
        print("Game Draw!")
        break

    ai_move = best_move()
    board[ai_move] = "O"

    if check_winner("O"):
        print_board()
        print("🤖 AI wins!")
        break

    if is_draw():
        print_board()
        print("Game Draw!")
        break