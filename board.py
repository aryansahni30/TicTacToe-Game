class Board:
    def __init__(self):
        #board is a list of cells that are represented
        # by strings (" ", "O", and "X")
        # initially it is made of empty cells represented
        # by " " strings
        self.sign = " "
        self.size = 3
        self.board = list(self.sign * self.size ** 2)
        # the winner's sign X or O
        self.winner = ""

    def get_size(self):
        # return the size of the board
        return self.size

    def get_winner(self):
        # return the winner's sign X or O
        return self.winner

    def set(self, cell, sign):
        # mark the cell on the board with the sign X or O
        indexes = {"A1": 1, "B1": 2, "C1": 3, "A2": 4, "B2": 5, "C2": 6, "A3": 7, "B3": 8, "C3": 9}
        cell_index = indexes[cell] - 1
        self.board[cell_index] = sign

    def isempty(self, cell):
# return True if the cell is empty (not marked with X or O)
        indexes = {"A1": 1, "B1": 2, "C1": 3, "A2": 4, "B2": 5, "C2": 6, "A3": 7, "B3": 8, "C3": 9}
        cell_index = indexes[cell] - 1
        if self.board[cell_index] == " ":
            return True

    def isdone(self):
        done = False
        self.winner = ''

       # check all game terminating conditions, if one of them is present, assign the var done to True
       # depending on conditions assign the instance var winner to O or X
       #check rows in board       
        if self.board[0] == self.board[1] == self.board[2] == "X" or self.board[0] == self.board[1] == self.board[
            2] == "O":  # row 1
            done = True
            self.winner = self.board[0]
        elif self.board[3] == self.board[4] == self.board[5] == "X" or self.board[3] == self.board[4] == self.board[
            5] == "O":  # row 2
            done = True
            self.winner = self.board[3]
        elif self.board[6] == self.board[7] == self.board[8] == "X" or self.board[6] == self.board[7] == self.board[
            8] == "O":  # row 3
            done = True
            self.winner = self.board[6]

        # check columns in board
        elif self.board[0] == self.board[3] == self.board[6] == "X" or self.board[0] == self.board[3] == self.board[
            6] == "O":  # column 1
            done = True
            self.winner = self.board[0]
        elif self.board[1] == self.board[4] == self.board[7] == "X" or self.board[1] == self.board[4] == self.board[
            7] == "O":  # column 2
            done = True
            self.winner = self.board[1]
        elif self.board[2] == self.board[5] == self.board[8] == "X" or self.board[2] == self.board[5] == self.board[
            8] == "O":  # column 3
            done = True
            self.winner = self.board[2]

        # check diagonals in board
        elif self.board[0] == self.board[4] == self.board[8] == "X" or self.board[0] == self.board[4] == self.board[
            8] == "O":  # diagonal 1
            done = True
            self.winner = self.board[0]
        elif self.board[2] == self.board[4] == self.board[6] == "X" or self.board[2] == self.board[4] == self.board[
            6] == "O":  # diagonal 2
            done = True
            self.winner = self.board[2]

        # condition for a tie
        
        count = 0
        for x in ["A1", "A2", "A3", "B1", "B2", "B3", "C1", "C2", "C3"]:
            if self.isempty(x) != True:
                count += 1
        if count == 9:
            done = True

        return done

    def show(self):
        # print the board on the screen
        
        print("\n   A   B   C ")
        print(" +---+---+---+")
        for i in range(self.size):
            print(f"{i + 1}| {self.board[i * self.size]} | {self.board[i * self.size + 1]} | {self.board[i * self.size + 2]} |")
            print(" +---+---+---+")
        print("")
    


