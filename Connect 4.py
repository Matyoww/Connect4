from Board import Board
from Player import Player


myBoard = Board(6,7)
p1 = Player(1)
p2 = Player(2)


while True:

    # Player 1
    myBoard.print_board()
    p1.print_turn()
    p1.input()
    while myBoard.is_full(p1.column):
        print("Column Full!")
        p1.column = int(input("Enter the column no. again(1 - 7): ")) - 1

    print("\n")

    myBoard.stack(p1.column, p1.peg)
    if myBoard.check_win():
        myBoard.print_board()
        p1.print_win()
        break

    # Player 2
    myBoard.print_board()
    p2.print_turn()
    p2.input()
    while myBoard.is_full(p2.column):
        print("Column Full!")
        p2.column = int(input("Enter the column no. again(1 - 7): ")) - 1

    print("\n")

    myBoard.stack(p2.column, p2.peg)
    if myBoard.check_win():
        myBoard.print_board()
        p2.print_win()
        break
