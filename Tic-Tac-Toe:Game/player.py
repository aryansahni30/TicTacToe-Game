import random
from random import choice


class Player:
    def __init__(self, name, sign):
        self.name = name  # player's name
        self.sign = sign  # player's sign X or O

    def get_sign(self):
        # return an instance sign
        return self.sign

    def get_name(self):
        # return an instance name
        return self.name

    def choose(self, board):
        count = 0
        valid_input = False
        while (valid_input == False):
            if count != 0:
                print("You did not choose correctly.")
            print(self.name + ", " + self.sign + ": Enter a cell [A-C][1-3]:")  # ask user to choose cell
            cell_choice = input()
            if type(cell_choice) == str:  # check if input is right type
                if len(cell_choice) == 2:
                    if cell_choice[0] in ["A", "a", "B", "b", "C", "c"] and cell_choice[1] in ["1", "2", "3"]:
                        cell = cell_choice[0].upper() + cell_choice[1]  # make input uppercase
                        if board.isempty(cell) == True:  # check if cell is empty
                            valid_input = True
                            board.set(cell, self.sign)
            count += 1


class AI(Player):
    def __init__(self, name, sign, board):
        self.name = name  # AI's name
        self.sign = sign  # AI's sign
        if self.sign == "X":  # set opponent's sign
            self.opponent_sign = "O"
        else:
            self.opponent_sign = "X"
        self.board = board
        self.possible_choices = ["A1", "A2", "A3", "B1", "B2", "B3", "C1", "C2", "C3"] # list of possible choices

    def choose(self, board):
        print(self.name + ", " + self.sign + ": Enter a cell [A-C][1-3]:")  # ask user to choose cell
        for x in self.possible_choices:  
            if board.isempty(x) != True:
                self.possible_choices.remove(x)
        move = random.choice(self.possible_choices)  # choose random element from choices list
        self.possible_choices.remove(move) 
        board.set(move, self.sign)  
        print(move)  # print the chosen move


class MiniMax(AI):
    def choose(self, board):
        print(f"\n{self.name}, {self.sign}: Enter a cell [A-C][1-3]: ")  # ask user to choose cell
        for x in self.possible_choices: # traverse through possible choices list
            if board.isempty(x) != True:
                self.possible_choices.remove(x)
        cell = MiniMax.minimax(self, board, True,
                               True) # call minimax() to get the best move for MiniMax and store it in cell
        print(cell)  # print the chosen move
        self.possible_choices.remove(cell)  
        board.set(cell, self.sign) # set cell to self sign

    def minimax(self, board, self_player, start):
        if board.isdone():
            # self = winner
            if board.get_winner() == self.sign:
                return 1
            # tie
            elif board.get_winner() == "":
                return 0
            # self = loser
            else:
                return -1

        # set max score to -infinity and min score to infinity
        max_score = float('-inf')
        min_score = float('inf')
        move = ""
        for cell in ["A1", "A2", "A3", "B1", "B2", "B3", "C1", "C2", "C3"]:  # traverse through board cells
            if self.board.isempty(cell):  
                if self_player:
                    board.set(cell, self.sign)
                    score = MiniMax.minimax(self, board, False,
                                            False)
                    if score > max_score:
                        max_score = score
                        move = cell

                else:  # opponent's turn
                    board.set(cell, self.opponent_sign)
                    score = MiniMax.minimax(self, board, True, False)
                    if score < min_score:
                        min_score = score
                        move = cell

                board.set(cell, " ") # reset cell to empty
        if start:  
            return move
        elif self_player:  
            return max_score
        else:
            return min_score 

