class Board:
    def __init__(self):
        # board is a list of cells that are represented 
        # by strings (" ", "O", and "X")
        # initially it is made of empty cells represented 
        # by " " strings
        self.sign = " "
        self.size = 3
        self.board = list(self.sign * self.size**2)
        self.valid = ['A1', 'A2', 'A3', 'B1', 'B2','B3', 'C1', 'C2','C3']
        # the winner's sign O or X
        self.winner = ""
    def get_size(self): 
        pass
        # optional, return the board size (an instance size)
    def get_winner(self):
        solutions = [[0, 1, 2], [3, 4, 5], [6, 7, 8], [0, 3, 6], [1, 4, 7], [2, 5, 8], [0, 4, 8], [2, 4, 6]]
        for item in solutions:
            if self.board[item[0]] == self.board[item[1]] == self.board[item[2]]:
                return self.board[item[0]]
        #This should return a string 'X' or 'O'
        # return the winner's sign O or X (an instance winner)     
    def update(self, cell, sign):
        position = self.valid.index(cell)
        self.board[position] = sign
        self.valid[position] = ''
    def isempty(self, cell):
        if cell in self.valid:
            return True
        else:
            return False
        # return True if the cell is empty (not marked with X or O)
    def isdone(self):
        done = False
        solutions = [[0, 1, 2], [3, 4, 5], [6, 7, 8], [0, 3, 6], [1, 4, 7], [2, 5, 8], [0, 4, 8], [2, 4, 6]]
        for item in solutions:
            if self.board[item[0]] == self.board[item[1]] == self.board[item[2]] == 'X':
                done = True
            elif self.board[item[0]] == self.board[item[1]] == self.board[item[2]] == 'O':
                done = True
            elif ' ' not in self.board:
                done = True
        # check all game terminating conditions, if one of them is present, assign the var done to True
        # depending on conditions assign the instance var winner to O or X
        return done
    def show(self):
        # draw the board
        return  print("   A   B   C \n"\
                " +---+---+---+\n"\
                f"1| {self.board[0]} | {self.board[3]} | {self.board[6]} |\n"\
                " +---+---+---+\n"\
                f"2| {self.board[1]} | {self.board[4]} | {self.board[7]} |\n"\
                " +---+---+---+\n"\
                f"3| {self.board[2]} | {self.board[5]} | {self.board[8]} |\n"\
                " +---+---+---+ ")

