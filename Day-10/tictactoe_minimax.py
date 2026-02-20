# Tic Tac Toe using Minimax Algorithml
# User = X
# Computer = O

import math

board = [" " for _ in range(9)]

def print_board():
    print()
    print(board[0] + " | " + board[1] + " | " + board[2])
    print("--+---+--")
    print(board[3] + " | " + board[4] + " | " + board[5])
    print("--+---+--")
    print(board[6] + " | " + board[7] + " | " + board[8])
    print()

def check_winner(b, player):
    win_pos = [
        [0,1,2],[3,4,5],[6,7,8],
        [0,3,6],[1,4,7],[2,5,8],
        [0,4,8],[2,4,6]
    ]
    for pos in win_pos:
        if b[pos[0]] == b[pos[1]] == b[pos[2]] == player:
            return True
    return False

def is_draw():
    return " " not in board

def minimax(b, depth, is_max):
    if check_winner(b, "O"):
        return 1
    if check_winner(b, "X"):
        return -1
    if " " not in b:
        return 0

    if is_max:
        best = -math.inf
        for i in range(9):
            if b[i] == " ":
                b[i] = "O"
                score = minimax(b, depth+1, False)
                b[i] = " "
                best = max(best, score)
        return best
    else:
        best = math.inf
        for i in range(9):
            if b[i] == " ":
                b[i] = "X"
                score = minimax(b, depth+1, True)
                b[i] = " "
                best = min(best, score)
        return best

def computer_move():
    best_score = -math.inf
    move = -1
    for i in range(9):
        if board[i] == " ":
            board[i] = "O"
            score = minimax(board, 0, False)
            board[i] = " "
            if score > best_score:
                best_score = score
                move = i
    board[move] = "O"
    print("Computer chose position:", move+1)

def user_move():
    while True:
        try:
            pos = int(input("Enter position (1-9): ")) - 1
            if pos >= 0 and pos < 9 and board[pos] == " ":
                board[pos] = "X"
                break
            else:
                print("Invalid move, try again.")
        except:
            print("Enter a valid number.")

print("Positions are numbered 1 to 9")
print("You are X, Computer is O")

while True:
    print_board()
    user_move()

    if check_winner(board, "X"):
        print_board()
        print("You win!")
        break
    if is_draw():
        print_board()
        print("Draw!")
        break

    computer_move()

    if check_winner(board, "O"):
        print_board()
        print("Computer wins!")
        break
    if is_draw():
        print_board()
        print("Draw!")
        break
