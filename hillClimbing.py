#do the hill climbing process
#visualize with an interation by evaluation function graph
#maybe integrate with GUI as to be able to do a step-by-step summary of what happened
import numpy as np
import math

from puzzleRepresentation import *
from puzzleEvaluation import *

class coordinate(object):
	def __init__(self, row, col):
		self.row = row
		self.col = col

class pairOfBoardsEvalScores(object):
	def __init__(self, preBoards, preDistanceBoards, preScores, boards, distanceBoards, scores):
		self.preBoards = preBoards
		self.preDistanceBoards = preDistanceBoards
		self.preScores = preScores
		self.boards = boards
		self.distanceBoards = distanceBoards
		self.scores = scores

def bestRandomRestart(pairOfBoardsEvalScores):
	maxScore = None
	indices = []
	for index, score in enumerate(pairOfBoardsEvalScores.scores):
	    if maxScore is None or score > maxScore:
	        indices = [index]
	        maxScore = score
	    elif score == maxScore:
	        indices.append(index)
	return indices


def chooseRandomCell(size):
	chooseCell = np.random.randint(1, pow(size,2)) #choose random integer from 1 to size^2 - 1
	col = ((chooseCell-1) % size)+1 #returns 
	row = int((chooseCell-1) / size) + 1
	coor = coordinate(row, col)
	return coor

#input the standard board
def basicHillClimbing(board, iterations, p):
	hillClimbBoard = np.copy(board)
	size = hillClimbBoard[0].size
	eval = evalScore(calcNumberToReach(evaluate(hillClimbBoard),size))
	i=1
	count1 = 0
	count2 = 0
	while i <= iterations:
		coor = chooseRandomCell(hillClimbBoard[0].size)
		maxMoves = np.empty(4)
		maxMoves[0] = size - coor.row
		maxMoves[1] = coor.row - 1
		maxMoves[2] = size - coor.col
		maxMoves[3] = coor.col - 1
		#random integer from 1 to np.amax(maxMoves)+1, including 1, discluding np.amax(maxMoves)+1
		prevValue = hillClimbBoard[coor.row-1,coor.col-1]
		hillClimbBoard[coor.row-1,coor.col-1] = np.random.randint(1, np.amax(maxMoves)+1)
		newEval = evalScore(calcNumberToReach(evaluate(hillClimbBoard), size))

		if newEval >= eval:
			eval = newEval
		elif np.random.random() < p:
			eval = newEval
			count1 += 1
		else:
			hillClimbBoard[coor.row-1,coor.col-1] = prevValue
			count2 += 1
		i += 1
	print(count1, ":::", count2)
	return hillClimbBoard

def hillClimbingWithRandomRestart(size, iterations, restarts, p):
	preStarts = []
	preDistanceBoards = []
	preEvalStarts = []
	candidates = []
	distanceBoards = []
	evalCandidates = []
	for i in range(0, restarts):

		board = generateBoard(size)
		preStarts.append(board)

		preDistanceBoard = calcNumberToReach(evaluate(board), board[0].size)
		preDistanceBoards.append(preDistanceBoard)

		preEvalStarts.append(evalScore(preDistanceBoard))


		tempBoard = np.copy(board)
		print("called the function")
		tempCandidate = basicHillClimbing(tempBoard, iterations/restarts, p)
		candidates.append(tempCandidate)

		distanceBoard = calcNumberToReach(evaluate(tempCandidate), tempCandidate[0].size)
		distanceBoards.append(distanceBoard)

		evalCandidates.append(evalScore(distanceBoard))

	candidatePairBoardEvalScore = pairOfBoardsEvalScores(preStarts, preDistanceBoards, preEvalStarts, candidates, distanceBoards, evalCandidates)
	return candidatePairBoardEvalScore
############### BASICALLY A COPY OF THE ABOVE TWO FUNCTIONS #############################
def simAnnealProb(T, d, prevScore, postScore):
	prob = pow(math.e, (postScore - prevScore)/T)
	return prob

def simAnnealHillClimbing(board, iterations, T, d):
	hillClimbBoard = np.copy(board)
	size = hillClimbBoard[0].size
	eval = evalScore(calcNumberToReach(evaluate(hillClimbBoard),size))
	i=1
	count1 = 0
	count2 = 0
	while i <= iterations:
		coor = chooseRandomCell(hillClimbBoard[0].size)
		maxMoves = np.empty(4)
		maxMoves[0] = size - coor.row
		maxMoves[1] = coor.row - 1
		maxMoves[2] = size - coor.col
		maxMoves[3] = coor.col - 1
		#random integer from 1 to np.amax(maxMoves)+1, including 1, discluding np.amax(maxMoves)+1
		prevValue = hillClimbBoard[coor.row-1,coor.col-1]
		hillClimbBoard[coor.row-1,coor.col-1] = np.random.randint(1, np.amax(maxMoves)+1)
		newEval = evalScore(calcNumberToReach(evaluate(hillClimbBoard), size))

		if newEval >= eval:
			eval = newEval
		elif np.random.random() < simAnnealProb(T, d, eval, newEval):
			print("simm")
			eval = newEval
			count1 += 1
		else:
			hillClimbBoard[coor.row-1,coor.col-1] = prevValue
			count2 += 1
		print(eval, " ", newEval, " ", T, "  ", simAnnealProb(T, d, eval, newEval))
		T = T*d
		i += 1
	print(count1, ":::", count2)
	return hillClimbBoard

def hillClimbingWithSimulatedAnnealing(size, iterations, restarts, T, d):
	preStarts = []
	preDistanceBoards = []
	preEvalStarts = []
	candidates = []
	distanceBoards = []
	evalCandidates = []
	for i in range(0, restarts):

		board = generateBoard(size)
		preStarts.append(board)

		preDistanceBoard = calcNumberToReach(evaluate(board), board[0].size)
		preDistanceBoards.append(preDistanceBoard)

		preEvalStarts.append(evalScore(preDistanceBoard))


		tempBoard = np.copy(board)
		print("called the function")
		tempCandidate = simAnnealHillClimbing(tempBoard, iterations/restarts, T, d)
		candidates.append(tempCandidate)

		distanceBoard = calcNumberToReach(evaluate(tempCandidate), tempCandidate[0].size)
		distanceBoards.append(distanceBoard)

		evalCandidates.append(evalScore(distanceBoard))

	candidatePairBoardEvalScore = pairOfBoardsEvalScores(preStarts, preDistanceBoards, preEvalStarts, candidates, distanceBoards, evalCandidates)
	return candidatePairBoardEvalScore

