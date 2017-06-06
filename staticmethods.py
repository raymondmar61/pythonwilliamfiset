#williamfiset 42 Static Methods

#run on Python2.7
#static methods belong to a class, not specific to an object

class Board(object):

	_game_tiles = []

	def __init__(self, length, width):
		if not Board._game_tiles:
			for _ in xrange( length * width ):
				Board._game_tiles.append(Tile())

	@staticmethod
	def move_together(x_amount, y_amount):
		for tile in Board._game_tiles:
			tile.move(x_amount, y_amount)
			#print x_amount, y_amount

	@staticmethod
	def print_locations():
		for tile in Board._game_tiles:
			print tile.x, tile.y

class Tile(object):
	def __init__(self):
		self.x = 0
		self.y = 0

	def move(self, x, y):
		self.x += x
		self.y += y

my_board = Board(4,4)
Board.print_locations()
Board.move_together(10, 20) #syntax for calling a static method ClassName.staticmethod.  Another way object.method()
Board.print_locations()