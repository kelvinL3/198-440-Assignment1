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

#BasicHillClimbing, for loading in a specific one
def doHillClimbing(board, size, iterations, p=0):
	#board = createAndCalcBoard(size)
	afterBasicHillClimbing = basicHillClimbing(board, iterations, p)
	print("After Basic Hill Climbing\n", afterBasicHillClimbing)
	distanceBoard = calcNumberToReach(evaluate(afterBasicHillClimbing), size)
	print("distanceBoard\n", distanceBoard)
	#newEval = evalScore(calcNumberToReach(evaluate(board), size))
	print("evalFunction(board_AFTER)=", evalScore(distanceBoard))
	return 

#HillClimbingWithRandomRestart
def doHillClimbingWithRandomRestart(size, iterations, numberOfRestarts, p=0):
	afterHillClimbingWithRestart = hillClimbingWithRandomRestart(size, iterations, numberOfRestarts, p)
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
	for x in indices:
		print(x)
		#gives the index of the best outcome
#HillClimbingWithRandomRestart
def doHillClimbingWithSimulatedAnnealing(size, iterations, numberOfRestarts, T, d):
	afterHillClimbingWithSimulatedAnnealing = hillClimbingWithSimulatedAnnealing(size, iterations, numberOfRestarts, T, d)
	i = 0
	while i < numberOfRestarts:
		print("\t\t\tBoard", i+1)
		print(afterHillClimbingWithSimulatedAnnealing.preBoards[i])
		print(afterHillClimbingWithSimulatedAnnealing.preDistanceBoards[i])
		print(afterHillClimbingWithSimulatedAnnealing.preScores[i])
		print(afterHillClimbingWithSimulatedAnnealing.boards[i])
		print(afterHillClimbingWithSimulatedAnnealing.distanceBoards[i])
		print(afterHillClimbingWithSimulatedAnnealing.scores[i])
		i += 1

	print("Best Random Restart:", )
	indices = bestRandomRestart(afterHillClimbingWithSimulatedAnnealing)
	for x in indices:
		print(x)
		#gives the index of the best outcome


size = 5
iterations = 900
numberOfRestarts = 2


board = createAndCalcBoard(size)
doHillClimbing(board, size, iterations)
#doHillClimbingWithRandomRestart(size, iterations, numberOfRestarts)


# with random restart, p=0 is regular walk, p=1 is random walk
# doHillClimbing(board, size, iterations, p=0.5)
###  doHillClimbingWithRandomRestart(size, iterations, numberOfRestarts, p=.5)

#doHillClimbingWithSimulatedAnnealing(size, iterations, numberOfRestarts, T, d)
#doHillClimbingWithSimulatedAnnealing(size, iterations, numberOfRestarts, 100, .97)