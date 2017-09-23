import numpy as np

from puzzleRepresentation import *
from puzzleEvaluation import *
from Tree import *
from hillClimbing import *
#import puzzleEvaluation 

def createAndCalcBoard(size):
	board = generateBoard(size)
	#print("save as\n", board)
	name = "boardState.txt"
	writeBoard(board, name)

	board = readBoard(name)
	print("Puzzle Board Read As\n", board,"\n")

	rootNode = evaluate(board)
	NumberToReachBoard = calcNumberToReach(rootNode, size)
	print("Number of Moves to Reach Each Cell\n", NumberToReachBoard)
	print()
	print("evalFunction(board_BEFORE)=", evalScore(NumberToReachBoard), "\n")
	return board

#BasicHillClimbing
def doHillClimbing(board, size, iterations, p=0):
	#board = createAndCalcBoard(size)
	afterBasicHillClimbing = basicHillClimbing(board, iterations)
	print("After Basic Hill Climbing\n", afterBasicHillClimbing)
	distanceBoard = calcNumberToReach(evaluate(afterBasicHillClimbing), size)
	print("distanceBoard\n", distanceBoard)
	#newEval = evalScore(calcNumberToReach(evaluate(board), size))
	print("evalFunction(board_AFTER)=", evalScore(distanceBoard))
	return 

#HillClimbingWithRandomRestart
def doHillClimbingWithRandomRestart(size, iterations, numberOfRestarts, p=0):
	afterHillClimbingWithRestart = hillClimbingWithRandomRestart(size, iterations, numberOfRestarts)
	# afterHillClimbingWithRestart.preBoards.reverse()
	# afterHillClimbingWithRestart.preScores.reverse()
	# afterHillClimbingWithRestart.boards.reverse()
	# afterHillClimbingWithRestart.scores.reverse()
	i = 0
	while i < numberOfRestarts:
		print("\t\t\tBoard", i+1)
		print(afterHillClimbingWithRestart.preBoards[i])
		print(afterHillClimbingWithRestart.preDistanceBoards[i])
		print(afterHillClimbingWithRestart.preScores[i])
		print(afterHillClimbingWithRestart.boards[i])
		print(afterHillClimbingWithRestart.distanceBoards[i])
		print(afterHillClimbingWithRestart.scores[i])
		i += 1

	print("Best Random Restart:", )
	indices = bestRandomRestart(afterHillClimbingWithRestart)
	indices.reverse()
	for x in indices:
		print(x)



size = 5
iterations = 1000
numberOfRestarts = 1


board = createAndCalcBoard(size)
# doHillClimbing(board, size, iterations)
doHillClimbingWithRandomRestart(size, iterations, numberOfRestarts)


# with random restart
# doHillClimbing(board, size, iterations, p=0.5)
doHillClimbingWithRandomRestart(size, iterations, numberOfRestarts, p=0.5)
