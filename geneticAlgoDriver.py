import numpy as np
import math

from puzzleRepresentation import *
from puzzleEvaluation import *
from hillClimbing import *

def createInitialPopulation(dimension, popSize):
	population = []
	for i in range(0, popSize):
		population.append(generateBoard(dimension))
	return population

def evaluatePopulation(dimension, popSize, population):
	popScores = []
	for i in range(0, popSize):
		score = int(evalScore(calcNumberToReach(evaluate(population[i]), dimension))) 
		popScores.append(score)
	return popScores

def normalizeScores(dimension, popSize, popScores):
	total = 0
	for i in range(0, popSize):
		popScores[i] += pow(dimension, 2) 
		total += popScores[i]
	for i in range(0, popSize):
		popScores[i] = popScores[i]/total
	return popScores

def takeTopN(topN, population, popScores):
	survivors = []
	reduce = 0 
	for i in range(topN):
		randomNumber = (1-reduce)*np.random.random()
		temp = 0
		j = -1
		while temp < randomNumber:
			temp += popScores[j]
			j += 1
		#print("jth subject taken", j)
		survivors.append(population[j])
		population.pop(j)
		reduce += popScores[j]
		popScores.pop(j)
	return survivors

def mating(matrix1, matrix2):
	matrix3 = np.empty((matrix1[0].size,matrix1[0].size), dtype=np.int)
	counter = 0 
	for i in range(0, matrix3[0].size):
		for j in range(0, matrix3[0].size):
			if counter % 2 == 0:
				matrix3[i,j] = matrix1[i,j]
			elif counter % 2 == 1:
				matrix3[i,j] = matrix2[i,j]
			counter += 1
	return matrix3

def repopulation(topN, survivors, popSize):
	for i in range(topN, popSize):

		matrix1 = np.random.randint(topN)
		matrix2 = np.random.randint(topN - 1)
		if matrix2 >= matrix1:
			matrix2 += 1

		matrix1 = survivors[matrix1]
		matrix2 = survivors[matrix2]
		survivors.append(mating(matrix1, matrix2))
	return survivors

def mutateIndividual(matrix1):
	size = matrix1[0].size
	coor = chooseRandomCell(size)
	maxMoves = np.empty(4)
	maxMoves[0] = size - coor.row
	maxMoves[1] = coor.row - 1
	maxMoves[2] = size - coor.col
	maxMoves[3] = coor.col - 1
	#random integer from 1 to np.amax(maxMoves)+1, including 1, discluding np.amax(maxMoves)+1
	matrix1[coor.row-1,coor.col-1] = np.random.randint(1, np.amax(maxMoves)+1)
	return matrix1

def randomlyMutatePopulation(popSize, population, chanceToMutuateIndividual):
	for i in range(0, popSize):
		if chanceToMutuateIndividual > np.random.random():
			mutateIndividual(population[i])

# helper method
def averagePopScores(popScores, sizeOfArray):
	average = 0
	for i in range(0, sizeOfArray):
		average += popScores[i]
	average = average / sizeOfArray
	return average

# printing method
def printListOfArrays(listOfArrays):
	for x in listOfArrays:
		print(int(evalScore(calcNumberToReach(evaluate(x), x[0].size))), "\n", x, "\n")

# dimension = size from before, name change due to size and popSize being similar
# 

dimension = 7
popSize = 100
topN = 25
iterations = 200

population = createInitialPopulation(dimension, popSize)

for i in range(iterations):
	#printListOfArrays(population)
	#culling
	popScores = evaluatePopulation(dimension, popSize, population)
	print(averagePopScores(popScores, popSize))
	normalizeScores(dimension, popSize, popScores)
	survivors = takeTopN(topN, population, popScores)

	#mating
	repopulation(topN, survivors, popSize)
	population = survivors

	#mutating
	randomlyMutatePopulation(popSize, population, 0.2)
#print("FINAL POPULATION")
printListOfArrays(population)