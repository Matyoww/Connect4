rows, cols = (6, 7)
board = []
p1 = 1
p2 = -1

# Create and initialize the Board
def init():
    for i in range(rows):
        row = []
        for j in range(cols):
            row.append(0)
        board.append(row)

def printBoard():
    for row in board:
        print(row)

# Checks who is the winner, 1 for p1, -1 for p2
# If no one won, returns 0
def checkWin():
    return 0

# After picking the column, stack it
def stack(p_col, player):
    i = rows - 1
    while board[i][p_col] != 0:
        i -= 1
    board[i][p_col] = player

# Check column height and limit it
def isFull(p_col):
    if board[0][p_col] != 0:
        return True
    else:
        return False

# Main game
init()
while checkWin() == 0:
    # Player 1
    printBoard()
    print("Player 1's Turn")
    p1_col = int(input("Enter the column no. (1 - 7): ")) - 1
    while isFull(p1_col):
        print("Column Full!")
        p1_col = int(input("Enter the column no. again(1 - 7): ")) - 1
    print("\n")
    stack(p1_col, p1)

    # Player 2
    printBoard()
    print("Player 2's Turn")
    p2_col = int(input("Enter the column no. (1 - 7): ")) - 1
    while isFull(p2_col):
        print("Column Full!")
        p2_col = int(input("Enter the column no. again(1 - 7): ")) - 1
    print("\n")
    stack(p2_col, p2)