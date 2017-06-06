#what is constantly being printed on screen.  Print the characters as cursor moves around.
class Matrix():
	def __init__(self, rows, columns, default_character = "@"):
		self.rows = rows
		self.columns = columns

		self.grid = [[default_character] * columns for x in xrange(rows)] #python3.5 doesn't like xrange not defined.
		self.grid

	def print_matrix(self):
		for row in self.grid:
			print("".join(row)) #['a','b','c'] --> "abc"

	def update_character_in_matrix(self, row_number, column_number, new_character):
		if 0 <= row_number < self.rows:
			if 0 <= column_number < self.columns: #instructor error message appears.  Mistype self statement.  Instructor says even he makes errors writing Python.
				self.grid[row_number][column_number] = new_character
				return
			raise IndexError("Index error. Indexes out of bounds")