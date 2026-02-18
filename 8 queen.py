N = 8
board = [-1] * N

def safe(row, col):
    for i in range(row):
        if board[i] == col or abs(board[i] - col) == abs(i - row):
            return False
    return True

def solve(row):
    if row == N:
        print_board()
        return True

    for col in range(N):
        if safe(row, col):
            board[row] = col
            if solve(row + 1):
                return True
    return False

def print_board():
    for i in range(N):
        for j in range(N):
            if board[i] == j:
                print("Q", end=" ")
            else:
                print(".", end=" ")
        print()

solve(0)
