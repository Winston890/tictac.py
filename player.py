from board import Board
class Player(Board):
	def __init__(self, name, sign):
		self.name = name  # player's name
		self.sign = sign  # player's sign O or X
	def get_sign(self):
		return self.sign
	def get_name(self):
		return self.name
	def choose(self, board):
		while True: 
			cell = input("Pick a Cell: ")
			cell = cell.upper()
			if board.isempty(cell) is True:
				board.update(cell, self.sign)
				break
			else:
				print("Try again.")
	    # if the user enters a valid string and the cell on the board is empty, update the board
	    # otherwise print a message that the input is wrong and rewrite the prompt
	    # use the methods board.isempty(cell), and board.set(cell, sign)
	    # you need to convert A1, B1, …, C3 cells into index values from 1 to 9
	    # you can use a tuple ("A1", "B1",...) to obtain indexes 
	    # you can do the conversion here in the player.py or in the board.py
	    # this implementation is up to you 
a = Player("Bob", "O")
print(type(a.get_sign()))
