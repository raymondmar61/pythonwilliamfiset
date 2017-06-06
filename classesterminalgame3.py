# -*- coding: utf-8 -*-
import matrix #import matrix.py file
#import character #import character.py file
#from character import Direction #from statement avoids character.Direction.NORTH.  We can type Direction.NORTH
from character import * #import character.py and all its classes

rows = 23
columns = 40

game_matrix = matrix.Matrix(rows, columns, default_character = ' ')  #filename.classname(parameters)
main_symbol = MainSymbol("∏", velocityx = 2) #from character import * allows us to avoid character.MainSymbol.  Just type MainSymbol.

game_matrix.update_character_in_matrix(main_symbol.x, main_symbol.y, main_symbol.symbol)

while True:
	game_matrix.print_matrix()

	direction = raw_input("Where to next (WASD)? ")

	if direction == "q": break
	elif direction not in (Direction.NORTH, Direction.SOUTH, Direction.EAST, Direction.WEST): continue #user didn't enter value input, skip the loop, forget about it

	game_matrix.update_character_in_matrix(main_symbol.y, main_symbol.x, main_symbol.trace)

	main_symbol.move(direction)

	game_matrix.update_character_in_matrix(main_symbol.y, main_symbol.x, main_symbol.symbol)