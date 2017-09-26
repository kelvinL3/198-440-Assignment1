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
def doHillClimbing(board, size, iterations, p=0, name=""):
	f = open("randomWalkHillClimb" + name +".txt","a") #a is for appending, pointer is at end of file
	afterBasicHillClimbing = basicHillClimbing(board, iterations, p, f=f)
	return afterBasicHillClimbing

#HillClimbingWithRandomRestart
def doHillClimbingWithRandomRestart(size, iterations, numberOfRestarts, p=0, name=""):

	afterHillClimbingWithRestart = hillClimbingWithRandomRestart(size, iterations, numberOfRestarts, p, name)
	# i = 0
	# while i < numberOfRestarts:
	# 	print("\t\t\tBoard", i+1)
	# 	print(afterHillClimbingWithRestart.preBoards[i])
	# 	print(afterHillClimbingWithRestart.preDistanceBoards[i])
	# 	print(afterHillClimbingWithRestart.preScores[i])
	# 	print(afterHillClimbingWithRestart.boards[i])
	# 	print(afterHillClimbingWithRestart.distanceBoards[i])
	# 	print(afterHillClimbingWithRestart.scores[i])
	# 	i += 1

	print("Best Random Restart:", )
	indices = bestRandomRestart(afterHillClimbingWithRestart)
	for x in indices:
		print(afterHillClimbingWithRestart.boards[x])
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
	drawMatrix("Initial Board", board, dboard, score, timeToExecute) #basically visualize

def basicHillClimbingDriver(size, iterations, p=0, visualize = False, name=""):
	board = createAndCalcBoard(size)
	dboard = calcDistanceBoard(board)
	score = evalScore(dboard)
	board1 = doHillClimbing(board, size, iterations, p=p, name=name)
	dboard1 = calcDistanceBoard(board1)
	score1 = evalScore(dboard1)
	timeToExecute = datetime.now() - starttimme
	if visualize:
		drawMatrix("Initial Board", board, dboard, score, timeToExecute)
		drawMatrix("Final Board", board1, dboard1, score1, timeToExecute)

def randomRestartHillClimbingDriver(size, iterations, numberOfRestarts, visualize = False, name=""):
	# size, iterations, numberOfRestarts, p=0, name=""
	##print("1 level")
	board1 = doHillClimbingWithRandomRestart(size, iterations, numberOfRestarts, p=0, name=name)
	timeToExecute = datetime.now() - starttimme
	if visualize:
		drawMatrix("Initial Board", board, dboard, score, timeToExecute)
		drawMatrix("Final Board", board1, dboard1, score1, timeToExecute)

def simAnnealDriver(size, iterations, T, d, visualize = False, f=None):
	board = generateBoard(size)
	board1 = simAnnealHillClimbing(board, iterations, T, d, f)
	timeToExecute = datetime.now() - starttimme
	if visualize:
		drawMatrix("Initial Board", board, dboard, score, timeToExecute)
		drawMatrix("Final Board", board1, dboard1, score1, timeToExecute)

#doHillClimbingWithRandomRestart(size, iterations, numberOfRestarts)


# with random restart, p=0 is regular walk, p=1 is random walk
###  doHillClimbingWithRandomRestart(size, iterations, numberOfRestarts, p=.5)

#doHillClimbingWithSimulatedAnnealing(size, iterations, numberOfRestarts, T, d)
#doHillClimbingWithSimulatedAnnealing(size, iterations, numberOfRestarts, 100, .97)


starttimme = datetime.now()
#size = 5
iterations = 2000
#numberOfRestarts = 3



#simmulated Annealing
	# #for T in np.arange(200,300, 50):
	# T=25000
	# d=0.975
	# # for i in range(50):
	# # 	name = "5"#"test"+str(T)+str(d)
	# # 	f = open("simAnneal" + name + ".csv","a") 
	# # 	simAnnealDriver(5, iterations, T, d, visualize = False, f=f)

	# # for i in range(50):
	# # 	name = "7"#"test"+str(T)+str(d)
	# # 	f = open("simAnneal" + name + ".csv","a") 
	# # 	simAnnealDriver(7, iterations, T, d, visualize = False, f=f)

	# # for i in range(50):
	# # 	name = "9"#"test"+str(T)+str(d)
	# # 	f = open("simAnneal" + name + ".csv","a") 
	# # 	simAnnealDriver(9, iterations, T, d, visualize = False, f=f)

	# # for i in range(50):	
	# # 	name = "11"#"test"+str(T)+str(d)
	# # 	f = open("simAnneal" + name + ".csv","a") 
	# # 	simAnnealDriver(11, iterations, T, d, visualize = False, f=f)

#0.96-->16
#0.97-->16.2
#0.975-->16.5
#0.98-->16.1


# prob1 = 0.00
# prob2 = 0.01
# intervals = 5

# for j in range(1,intervals):
# 	alpha = j/intervals
# 	prob = (1-alpha)*prob1 + (alpha)*prob2
# 	prob = int(prob*1000)/1000
# 	print(prob)
#best p is 0.002

##good code for testing, named differently every time to get j different files
	#for i in range(0,20):
	#	basicHillClimbingDriver(5, iterations, p=prob1, visualize = False, name = "7-"+str(j))

#random Walk Data
# prob1 = 0.002
# for i in range(0,50):
# 	size=5
# 	basicHillClimbingDriver(size, iterations, p=prob1, visualize = False, name = str(size))
# 	size=7
# 	basicHillClimbingDriver(size, iterations, p=prob1, visualize = False, name = str(size))
# 	size=9
# 	basicHillClimbingDriver(size, iterations, p=prob1, visualize = False, name = str(size))
# 	size=11
# 	basicHillClimbingDriver(size, iterations, p=prob1, visualize = False, name = str(size))



#basicBoardCreation(11)
# for i in range(0,50):
# 	basicHillClimbingDriver(9, iterations, False, "9")

# for i in range(0,50):
# 	basicHillClimbingDriver(11, iterations, False, "11")



#####Graph Data 2
# for i in range(0,50):
# 	randomRestartHillClimbingDriver(5, iterations, numberOfRestarts, False, "5")
# 	randomRestartHillClimbingDriver(7, iterations, numberOfRestarts, False, "7")
# 	randomRestartHillClimbingDriver(9, iterations, numberOfRestarts, False, "9")
# 	randomRestartHillClimbingDriver(11, iterations, numberOfRestarts, False, "11")
