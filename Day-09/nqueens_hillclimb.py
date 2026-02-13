# N-Queen Hill Climbing
# User gives INITIAL STATE
# Prints COMPLETE PATH until h = 0 (solution)

def h(board):
    c = 0
    n = len(board)
    for i in range(n):
        for j in range(i+1, n):
            if board[i] == board[j] or abs(board[i]-board[j]) == abs(i-j):
                c += 1
    return c

def show(board):
    n = len(board)
    for i in range(n):
        print(" ".join("Q" if board[i]==j else "." for j in range(n)))
    print()

def hill_climb(board):
    n = len(board)
    path = [board[:]]  

    while True:
        curr_h = h(board)
        print("State:", board, " h =", curr_h)
        show(board)

        if curr_h == 0:
            print("Goal reached!")
            return path

        best = board[:]
        best_h = curr_h

        for r in range(n):
            for col in range(n):
                temp = board[:]
                temp[r] = col
                temp_h = h(temp)
                if temp_h < best_h:
                    best = temp[:]
                    best_h = temp_h

        if best_h >= curr_h:
            print("Stuck at local optimum!")
            return path

        board = best
        path.append(board[:])

n = int(input("Enter N: "))
print("Enter initial state as space-separated columns (0 to N-1)")
print("Example for N=4 : 1 3 0 2")

initial = list(map(int, input("Initial state: ").split()))

hill_climb(initial)
