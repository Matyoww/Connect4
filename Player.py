# Player OOP
class Player:
    def __init__(self, peg):
        self.peg = peg

    def print_turn(self):
        print("Player " + str(self.peg) + "'s Turn")

    def input(self):
        self.column = int(input("Enter the column no. (1 - 7): ")) - 1

    def print_win(self):
        print("Player " + str(self.peg) + " Wins!")