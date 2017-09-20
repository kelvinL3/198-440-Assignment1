import numpy as np

def generateBoard (size):
	#size should be 5,7,9,11;
	board = np.empty((size,size), dtype=np.int)
	if size == 0:
		print("Cannot make board of size zero")
		return 
	if size == 1:
		print("There is only a goal tile (with value 0)")
		board[0,0] = 0
		np.set_printoptions(precision=5, suppress=False)
		print(board)
		return board
	for x in range(1, size+1): #range goes from (1) to (1 less than size+1)
		for y in range(1, size+1):
			maxMoves = np.empty(4)
			maxMoves[0] = size - x
			maxMoves[1] = x - 1
			maxMoves[2] = size - y
			maxMoves[3] = y - 1
			board[x-1,y-1] = np.random.randint(1, np.amax(maxMoves+1))
			#print(x,y,np.amax(maxMoves+1))
		#print()
	board[size-1,size-1]=0
	np.set_printoptions(precision=5, suppress=False)
	print(board)
	print(board[0].size)
	return board

#generateBoard(5)