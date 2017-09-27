import numpy as np
import math

from puzzleRepresentation import *
from puzzleEvaluation import *
from hillClimbing import *
import time
from datetime import datetime, date, time, timedelta

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
		#popScores[i] += pow(dimension, 2) 
		if popScores[i] > 0:
			total += pow(popScores[i],2)
		elif popScores[i] < 0:
			total += 1
		else:
			total += 1
	for i in range(0, popSize):
		if popScores[i] > 0:
			popScores[i] = pow(popScores[i],2)/total#round(pow(popScores[i],2)/total,6)
		elif popScores[i] < 0:
			popScores[i] = 1/total
		else:
			popScores[i] = 1/total

		#print(str(popScores[i])+" ", end='')
	return popScores

def takeTopN(topN, population, popScores):
	survivors = []
	reduce = 0 
	import sys
	# x=0
	# for i in range(200):
	# 	x = x + popScores[i]
	# print(x)
	# sys.exit()
	for i in range(topN):
		randomNumber = (1-reduce)*np.random.random()
		temp = 0
		j = -1
		#print()
		#print(popScores)
		while temp < randomNumber:
			j += 1
			try:
				temp += popScores[j]
				#print(temp)
			except:
				#print("j, 1-reduce, temp, randomNumber\n", j, 1-reduce, temp, randomNumber)
				sys.exit()
		#print("jth subject taken", j)
		survivors.append(population[j])
		population.pop(j)
		reduce += popScores[j]
		#print(round(reduce,3), round(popScores[j],3))
		popScores.pop(j)
	return survivors

def mating(matrix1, matrix2):
	matrix3 = np.empty((matrix1[0].size,matrix1[0].size), dtype=np.int)
	counter = 0
	if np.random.randint(2)==1:
		tempM = matrix1
		matrix1 = matrix2
		matrix2 = tempM

	matrix3=matrix1
	# for i in range(0, matrix3[0].size):
	# 	for j in range(0, matrix3[0].size):
	# 		if i < matrix3[0].size/2:
	# 			matrix3[i,j] = matrix1[i,j]
	# 		elif i>=matrix3[0].size/2:
	# 			matrix3[i,j] = matrix2[i,j]
	# print(matrix1)
	# print(matrix2)
	# print(matrix3)
	# print()
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

def maxPopScores(popScores, sizeOfArray):
	max = 0
	for i in range(0, sizeOfArray):
		if popScores[i] > max:
			max = popScores[i]
	return max



# printing method
def printListOfArrays(listOfArrays):
	for x in listOfArrays:
		print(int(evalScore(calcNumberToReach(evaluate(x), x[0].size))), "\n", x, "\n")

# dimension = size from before, name change due to size and popSize being similar
# 

dimension = 11
popSize = 200
topN =  30
iterations = 15000

#print("starttime",starttimme)
population = createInitialPopulation(dimension, popSize)

#for i in range(iterations):
f = open("GATEST.csv","a")
#g = open("genAlgo9Avg.csv","a") 



starttimme = datetime.now()
for i in range(1):
	sF=""
	#sG=""
	check = True
	best = -dimension*dimension
	while iterations!=0: #check: #and iterations != 0:
		#printListOfArrays(population)
		#culling
		popScores = evaluatePopulation(dimension, popSize, population)
		a = maxPopScores(popScores, popSize)
		#print(best)
		if a > best:
			best = a
		sF = sF + str(best) + ","
		#sG = sG + str(averagePopScores(popScores, popSize)) + ","
		
		normalizeScores(dimension, popSize, popScores)
		survivors = takeTopN(topN, population, popScores)

		#mating
		repopulation(topN, survivors, popSize)
		population = survivors

		#mutating
		randomlyMutatePopulation(popSize, population, 0.13)

		# if datetime.now()-starttimme > timedelta(seconds=83):
		# 	check = False
		iterations += -1
	iterations = 2750
	print(iterations)
	#print(sF + "\n:\n" + sG)
	f.write(sF+"\n")
	#g.write(sG+"\n")



#print("FINAL POPULATION")
#printListOfArrays(population)