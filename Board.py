# Board OOP
class Board:
    def __init__(self, rows, cols):
        self.rows = rows
        self.cols = cols
        self.board = []
        for i in range(self.rows):
            row = []
            for j in range(self.cols):
                row.append(None)
            self.board.append(row)

    def print_board(self):
        for row in self.board:
            print(row)

    def is_full(self, p_col):
        return self.board[0][p_col] != None

    def stack(self, p_col, player):
        i = self.rows - 1
        while self.board[i][p_col] != None:
            i -= 1
        self.board[i][p_col] = player

    def check_win(self):
        # vertical
        for i in range(7):
            for j in range(3):
                if self.board[j][i] and \
                        self.board[j][i] == self.board[j + 1][i] and \
                        self.board[j][i] == self.board[j + 2][i] and \
                        self.board[j][i] == self.board[j + 3][i]:
                    return True

        # horizontal
        for i in range(6):
            for j in range(4):
                if self.board[i][j] and \
                        self.board[i][j] == self.board[i][j + 1] and \
                        self.board[i][j] == self.board[i][j + 2] and \
                        self.board[i][j] == self.board[i][j + 3]:
                    return True

        # diagonal (slash)
        for i in range(3):
            for j in range(4):
                if self.board[i][j + 3] and \
                        self.board[i][j + 3] == self.board[i + 1][j + 2] and \
                        self.board[i][j + 3] == self.board[i + 2][j + 1] and \
                        self.board[i][j + 3] == self.board[i + 3][j]:
                    return True

        # diagonal (backslash)
        for i in range(3):
            for j in range(4):
                if self.board[i][j] and \
                        self.board[i][j] == self.board[i + 1][j + 1] and \
                        self.board[i][j] == self.board[i + 2][j + 2] and \
                        self.board[i][j] == self.board[i + 3][j + 3]:
                    return True
        # otherwise
        return False