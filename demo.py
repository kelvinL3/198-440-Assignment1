import numpy as np

from puzzleRepresentation import *
from puzzleEvaluation import *
from Tree import *
from hillClimbing import *
#import puzzleEvaluation 
from PYQT4 import *
from datetime import datetime
import time
from driver import *
from geneticAlgoDriver import *

#Task1 - (size, iterations, visualize=True)
#basicHillClimbingDriver(11, iterations=6000, visualize=True)

#Task2
	# 1. put txt file in the same directory
	# 2. run this segment of the program
	#FOR-TESTING#writeBoard(generateBoard(7),"boardState.txt")
#readInBoardAndSolve("boardState.txt")

#Task3 - (size, iterations, p=0, visualize=True)
#basicHillClimbingDriver(5, 1000, p=0, visualize=True)

#Task4 - (size, iterations, numberOfRestarts, visualize = False, name="")
#doHillClimbingWithRandomRestart(5, 10000, 5, visualize = True)

#Task5 - (size, iterations, p=0.002, visualize = True)
#basicHillClimbingDriver(5, 1000, p=0.002, visualize = True)

#Task6 - (size, iterations, T, d, visualize = True)
# T=25000
# d=0.975
# simAnnealDriver(5, 40000, 25000, 0.975, visualize = True)

#Task7

# dimension = 5
# popSize = 50
# topN =  10
# iterations = 150

# population = createInitialPopulation(dimension, popSize)

# initial = np.copy(population[0])
# best = -dimension*dimension
# while iterations!=0: #check: #and iterations != 0:
# 	#culling
# 	popScores = evaluatePopulation(dimension, popSize, population)
# 	a = maxPopScores(popScores, popSize)
	
# 	normalizeScores(dimension, popSize, popScores)
# 	survivors = takeTopN(topN, population, popScores)

# 	#mating
# 	repopulation(topN, survivors, popSize)
# 	population = survivors

# 	#mutating
# 	randomlyMutatePopulation(popSize, population, 0.13)

# 	# 	check = False
# 	iterations += -1


# dboard = calcDistanceBoard(initial)
# score = evalScore(dboard)



# popScores = evaluatePopulation(dimension, popSize, population)
# x = maxPopScores(popScores, popSize)
# print(x)

# board1 = population[x]
# dboard1 = calcDistanceBoard(board1)
# score1 = evalScore(dboard1)
# drawMatrix("Initial Board", initial, dboard, score)
# drawMatrix("Final Board", board1, dboard1, score1)