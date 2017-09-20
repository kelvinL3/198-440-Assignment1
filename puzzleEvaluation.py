import numpy as np

from puzzleRepresentation import generateBoard
from Tree import Tree
import Queue

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
	q = Queue.Queue()
	t = Tree();
	q.put()

	while !q.empty():
		q.get()