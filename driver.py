import numpy as np

from puzzleRepresentation import *
from puzzleEvaluation import *
from Tree import *
#import puzzleEvaluation 





board = generateBoard(10)
#print("save as\n", board)
name = "boardState.txt"
writeBoard(board, name)
board = readBoard(name)
print("read as\n", board,"\n")
rootNode = evaluate(board)
print(calcNumberToReach(rootNode, board[0].size))