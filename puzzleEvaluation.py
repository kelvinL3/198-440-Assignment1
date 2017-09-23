import numpy as np

from puzzleRepresentation import generateBoard
#from Tree import *
import Tree as Tree
import queue

def isInBoard(size, row, col):
	if row > size or row < 1 or col > size or col < 1: 
		return False
	return True

#returns the tree
def evaluate(board):
	size = board[0].size


	visited = np.zeros((size,size), dtype=np.int)
	visited[0,0] = 1

	#children, jumpDistance, row, col
	rootNode = Tree.Node(None, None, None, None, board[0,0], 1, 1, 0);

	if size == 0:
		print("Cannot evaluate board of size zero")
		sys.exit()
	if size == 1:
		print("There is only a goal tile (with value 0)")
		board[0,0] = 0
		np.set_printoptions(precision=5, suppress=False)
		return rootNode

	t = rootNode
	q = queue.Queue()
	q.put(t)
	while not q.empty():
		t = q.get()
		jumpLength = t.jumpDistance
		if isInBoard(board[0].size, t.row+jumpLength, t.col): #if it's in the board
			if visited[t.row-1+jumpLength, t.col-1] == 0: #if it hasn't been visited yet
				visited[t.row-1+jumpLength,t.col-1] = 1
				#print("downCheck", t.row, t.col, board[t.row-1,t.col-1],t.depth)
				depth = int(t.depth) + 1
				t.downChild = Tree.Node(None, None, None, None, board[t.row-1+jumpLength,t.col-1], t.row+jumpLength, t.col, depth)
				q.put(t.downChild)
		if isInBoard(board[0].size, t.row-jumpLength, t.col):
			if visited[t.row-1-jumpLength, t.col-1] == 0:
				visited[t.row-1-jumpLength,t.col-1] = 1
				#print("upCheck", t.row, t.col, board[t.row-1,t.col-1],t.depth)
				depth = int(t.depth) + 1
				t.upChild = Tree.Node(None, None, None, None, board[t.row-1-jumpLength,t.col-1], t.row-jumpLength, t.col, depth)
				q.put(t.upChild)
		if isInBoard(board[0].size, t.row, t.col+jumpLength):
			if visited[t.row-1,t.col-1+jumpLength] == 0:
				visited[t.row-1,t.col-1+jumpLength] = 1
				#print("rightCheck", t.row, t.col, board[t.row-1,t.col-1],t.depth)
				depth = int(t.depth) + 1
				t.rightChild = Tree.Node(None, None, None, None, board[t.row-1,t.col-1+jumpLength], t.row, t.col+jumpLength, depth)
				q.put(t.rightChild)
		if isInBoard(board[0].size, t.row, t.col-jumpLength):
			if visited[t.row-1,t.col-1-jumpLength] == 0:
				visited[t.row-1,t.col-1-jumpLength] = 1
				#print("leftCheck", t.row, t.col, board[t.row-1,t.col-1],t.depth)
				depth = int(t.depth) + 1
				t.leftChild = Tree.Node(None, None, None, None, board[t.row-1,t.col-1-jumpLength], t.row, t.col-jumpLength, depth)
				q.put(t.leftChild)
	return rootNode

def bfs(root, board):
	if root != None:
		#print("bfs", root.row, root.col, root.depth)
		board[root.row-1, root.col-1] = root.depth
		bfs(root.upChild, board)
		bfs(root.downChild, board)
		bfs(root.rightChild, board)
		bfs(root.leftChild, board)
	return -1

#given the root of the tree, give the numberToReach matrix
def calcNumberToReach(root, size):
	numberToReach = np.zeros((size,size), dtype=np.int)
	bfs(root, numberToReach)
	#replace everything that was not reached with '-1'
	for i in range(size):
		for j in range(size):
			if numberToReach[i,j] == 0:
				numberToReach[i,j] = -1
	numberToReach[0,0] = 0
	return numberToReach

def evalScore(numberToReach):
	size = numberToReach[0].size
	if numberToReach[size-1,size-1] != -1: #end is reachable
		return int(numberToReach[size-1,size-1])
	else:
		score = 0 
		for i in range(size):
			for j in range(size):
				if numberToReach[i,j] == -1:
					score += -1
		return int(score)