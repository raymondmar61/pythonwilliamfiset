#what is constantly being printed on screen.  Print the characters as cursor moves around.
class Matrix():
	def __init__(self, rows, columns, default_character = "@"):
		self.rows = rows
		self.columns = columns

		self.grid = [[default_character] * columns for _ in xrange(rows)]
		self.grid

	def print_matrix(self):
		for row in self.grid:
			print("".join(row)) #['a','b','c'] --> "abc"