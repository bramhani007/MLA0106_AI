board = [' '] * 9

def show():
    print(board[0], "|", board[1], "|", board[2])
    print(board[3], "|", board[4], "|", board[5])
    print(board[6], "|", board[7], "|", board[8])
    print()

def win(p):
    return (
        (board[0]==board[1]==board[2]==p) or
        (board[3]==board[4]==board[5]==p) or
        (board[6]==board[7]==board[8]==p) or
        (board[0]==board[3]==board[6]==p) or
        (board[1]==board[4]==board[7]==p) or
        (board[2]==board[5]==board[8]==p) or
        (board[0]==board[4]==board[8]==p) or
        (board[2]==board[4]==board[6]==p)
    )

for i in range(9):
    show()
    pos = int(input("Enter position (0-8): "))
    board[pos] = 'X'

    if win('X'):
        show()
        print("User Wins")
        break

    for j in range(9):
        if board[j] == ' ':
            board[j] = 'O'
            break

    if win('O'):
        show()
        print("Computer Wins")
        break




