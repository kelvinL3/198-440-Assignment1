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
	board[size-1,size-1]=0
	np.set_printoptions(precision=5, suppress=False)
	return board

def writeBoard(board, name):
		f = open(name,"w+")
		f.write(str(board[0].size))
		f.write("\n")
		for i in range(board[1].size):
			for j in range(board[1].size):
				f.write(str(board[i,j]))
				#if i != (board[1].size-1) or j != (board[1].size-1):
				f.write(", ")
			f.write("\n")

def readBoard(name):
	file = open(name, 'r')
	size = int(file.readline())
	board = np.empty((size,size), dtype=np.int)
	i = 0
	j = 0
	for line in file:
		while line != "\n":
			temp = line[:1]
			line = line[3:]
			#print("temp:", temp,";",line)
			board[j,i] = int(temp)
			i+=1
		i=0	
		j+=1
	return board