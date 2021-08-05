import numpy as np
import time

start_time = time.time()

grid = [[0,0,0,0,0,1,2,0,0], 
	 	[0,0,0,0,0,0,3,4,0],
	 	[0,0,0,0,0,0,0,5,6],
	 	[0,0,0,0,0,0,0,0,7],
	 	[0,0,0,0,0,0,0,0,0],
	 	[1,0,0,0,0,0,0,0,0],
	 	[7,2,0,0,0,0,0,0,0],
	 	[0,4,8,0,0,0,0,0,0],
	 	[0,0,6,3,0,0,0,0,0]]

print (np.matrix(grid))

def find_empty_box(sudoku): 
	for x in range(9):
		for y in range(9):
			if sudoku[x][y] == 0:
				return x, y 
	
	return None, None

def Answer_Valid(sudoku, guess, row, col): 
	row_values = sudoku[row]    
	if guess in row_values:
		return False

	column_values = [sudoku[i][col]for i in range(9)]
	if guess in column_values:
		return False

	row_start = (row // 3) * 3
	col_start = (col // 3) * 3

	for x in range(row_start, row_start + 3):
		for y in range(col_start, col_start + 3):
			if sudoku[x][y] == guess:
				return False

		return True

def Solver(sudoku):
	row, col = find_empty_box(sudoku)

	if row is None:
		return True

	for guess in range(1,10):
		if Answer_Valid(sudoku, guess, row, col):
			sudoku[row][col] = guess

			if Solver(sudoku):
				return True

		sudoku[row][col] = 0

	return False

print(Solver(grid))

print(np.matrix(grid))

print("%s seconds " % (time.time() - start_time))