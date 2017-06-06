class Direction():
	SOUTH = 's' #likes single quotes, not double quotes
	WEST = 'w'
	EAST = 'e'
	NORTH = 'n'

class MainSymbol():
	def __init__(self, symbol, startX = 0, startY = 0, velocityx = 1, velocityy = 1, trace = '*'): #assign default values
		self.symbol = symbol
		self.x = startX
		self.y = startY
		self.velocityx = velocityx
		self.velocityy = velocityy

	def move(self, direction):

		#Y
		if direction == Direction.SOUTH:
			self.y += self.velocityy
		elif direction == Direction.NORTH:
			self.y -= self.velocityy
		#X
		elif direction == Direction.EAST:
			self.x += self.velocityx
		elif direction == Direction.WEST:
			self.x -= self.velocityX

