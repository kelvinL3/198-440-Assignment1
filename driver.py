import numpy as np

from puzzleRepresentation import *
from puzzleEvaluation import *
from Tree import *
#import puzzleEvaluation 





board = generateBoard(5)
#print("save as\n", board)
name = "boardState.txt"
writeBoard(board, name)
board = readBoard(name)
print("Puzzle Board Read As\n", board,"\n")
rootNode = evaluate(board)
NumberToReachBoard = calcNumberToReach(rootNode, board[0].size)
print("Number of Moves to Reach Each Cell\n", NumberToReachBoard)
print()
print("evalFunction(board)=", evalScore(NumberToReachBoard))