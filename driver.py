import numpy as np

from puzzleRepresentation import *
from puzzleEvaluation import *
from Tree import *
from hillClimbing import *
#import puzzleEvaluation 
from PYQT4 import *
from datetime import datetime
import time

def createAndCalcBoard(size):
	board = generateBoard(size)
	#print("save as\n", board)
	name = "boardState.txt"
	writeBoard(board, name)

	board = readBoard(name)
	#print("Puzzle Board Read As\n", board,"\n")

	# rootNode = evaluate(board)
	# NumberToReachBoard = calcNumberToReach(rootNode, size)
	# print("Number of Moves to Reach Each Cell\n", NumberToReachBoard)
	# print()
	# print("evalFunction(board_BEFORE)=", evalScore(NumberToReachBoard), "\n")
	return board

#return distanceBoard
def calcDistanceBoard(board):
	distanceBoard = calcNumberToReach(evaluate(board), board[0].size)
	return distanceBoard

#BasicHillClimbing, for loading in a specific one
def doHillClimbing(board, size, iterations, p=0):
	f = open("BasicHillClimbingPlotData.txt","a") #a is for appending, pointer is at end of file
	# f.write()
	afterBasicHillClimbing = basicHillClimbing(board, iterations, p, f)
	return afterBasicHillClimbing

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
		print("\t\tBoard", i+1)
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


def basicBoardCreation(size):
	board = createAndCalcBoard(size)
	dboard = calcDistanceBoard(board)
	score = evalScore(dboard)
	#time.sleep(1)
	timeToExecute = datetime.now() - starttimme
	drawMatrix("Initial Board", board, dboard, score, timeToExecute)

def basicHillClimbingDriver(size, iterations, visualize = False):
	board = createAndCalcBoard(size)
	dboard = calcDistanceBoard(board)
	score = evalScore(dboard)
	board1 = doHillClimbing(board, size, iterations)
	dboard1 = calcDistanceBoard(board1)
	score1 = evalScore(dboard1)
	timeToExecute = datetime.now() - starttimme
	if visualize:
		drawMatrix("Initial Board", board, dboard, score, timeToExecute)
		drawMatrix("Final Board", board1, dboard1, score1, timeToExecute)

#doHillClimbingWithRandomRestart(size, iterations, numberOfRestarts)


# with random restart, p=0 is regular walk, p=1 is random walk
# doHillClimbing(board, size, iterations, p=0.5)
###  doHillClimbingWithRandomRestart(size, iterations, numberOfRestarts, p=.5)

#doHillClimbingWithSimulatedAnnealing(size, iterations, numberOfRestarts, T, d)
#doHillClimbingWithSimulatedAnnealing(size, iterations, numberOfRestarts, 100, .97)


starttimme = datetime.now()
size = 5
iterations = 2000
numberOfRestarts = 2


#basicBoardCreation(11)
for i in range(0,50):
	basicHillClimbingDriver(size, iterations, False)

sys.exit()