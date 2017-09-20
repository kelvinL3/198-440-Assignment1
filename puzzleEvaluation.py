import numpy as np

from puzzleRepresentation import generateBoard
from Tree import Tree
import Queue

class coor(x,y):
	def __init__(self, row, col):
        self.row = x
        self.col = y

def isInBoard(size, row, col):
	if row > size or row < 1 or col > size or col < 1: 
		return False
	return True

def evaluate(board):
	board = np.empty((size,size), dtype=np.int)
	size = board[0].size
	if size == 0:
		print("Cannot evaluate board of size zero")
		return 
	if size == 1:
		print("There is only a goal tile (with value 0)")
		board[0,0] = 0
		np.set_printoptions(precision=5, suppress=False)
		print(board)
		return board

	visited = np.zeros((size,size), dtype=np.int)
	visited[0,0] = 1
	q = Queue.Queue()

	#children, jumpDistance, row, col
	t = Tree(None, coor(1+board[0,0],1), coor(1, 1+board[0,0]), None, board[0,0], 1, 1);
	q.put(t)

	while !q.empty():
		t = q.get()
		if isInBoard(board[1].size, t.row+board[t.row-1,t.col-1], t.col): #if it's in the board
			if visited[t.row-1+board[t.row-1,t.col-1],t.col-1] = 0: #if it hasn't been visited yet

		if isInBoard(board[1].size, t.row-board[t.row-1,t.col-1], t.col):
			if visited[t.row-1-board[t.row-1,t.col-1],t.col-1] = 0:

		if isInBoard(board[1].size, t.row, t.col+board[t.row-1,t.col-1]):
			if visited[t.row-1,t.col-1+board[t.row-1,t.col-1]] = 0::

		if isInBoard(board[1].size, t.row, t.col-board[t.row-1,t.col-1]):
			if visited[t.row-1,t.col-1-board[t.row-1,t.col-1]] = 0:

