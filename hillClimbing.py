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

def bestInitialStart(pairOfBoardsEvalScores):
	maxScore = None
	indices = []
	for index, score in enumerate(pairOfBoardsEvalScores.preScores):
	    if maxScore is None or score > maxScore:
	        indices = [index]
	        maxScore = score
	    elif score == maxScore:
	        indices.append(index)
	return indices
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
def basicHillClimbing(board, iterations, p, best="", fString="", f=None):
	##print("4 level")
	hillClimbBoard = np.copy(board)
	size = hillClimbBoard[0].size
	eval = evalScore(calcNumberToReach(evaluate(hillClimbBoard),size))
	i=1
	count1 = 0
	count2 = 0

	#fString = ""
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

		#if eval > best[0]:
		#	best[0] = eval 
		
		#fString = fString + str(eval) + ","
		#print(fString)
		if newEval >= eval:
			eval = newEval
		elif np.random.random() < p:
			eval = newEval
		else:
			hillClimbBoard[coor.row-1,coor.col-1] = prevValue
		i += 1
	##fString = fString + str(best[0]) + ","
	##print("fString= " + fString)
	#f.write(fString + "\n")
	return hillClimbBoard

def hillClimbingWithRandomRestart(size, iterations, restarts):
	preStarts = []
	preDistanceBoards = []
	preEvalStarts = []
	candidates = []
	distanceBoards = []
	evalCandidates = []

	best = [-size*size]
	#f = open("randomRestartHillClimbingPlotData" + name + ".csv","a") #a is for appending, pointer is at end of file


	for i in range(0, restarts):

		board = generateBoard(size)
		preStarts.append(board)

		preDistanceBoard = calcNumberToReach(evaluate(board), board[0].size)
		preDistanceBoards.append(preDistanceBoard)

		preEvalStarts.append(evalScore(preDistanceBoard))


		tempBoard = np.copy(board)
		#print("called the function")
		##print("best: " + str(best[0]))
		p=0
		tempCandidate = basicHillClimbing(tempBoard, iterations/restarts, p, best)
		# ans = basicHillClimbing(tempBoard, iterations/restarts, p, best, fString, f)
		# tempCandidate = ans.row
		# best = ans.col

		candidates.append(tempCandidate)

		distanceBoard = calcNumberToReach(evaluate(tempCandidate), tempCandidate[0].size)
		distanceBoards.append(distanceBoard)

		evalCandidates.append(evalScore(distanceBoard))

	candidatePairBoardEvalScore = pairOfBoardsEvalScores(preStarts, preDistanceBoards, preEvalStarts, candidates, distanceBoards, evalCandidates)
	return candidatePairBoardEvalScore
############### BASICALLY A COPY OF THE ABOVE TWO FUNCTIONS #############################
def simAnnealProb(T, d, prevScore, postScore):
	#eval>newEval; #prevScore>postScore
	#print("MATH",postScore, prevScore, T, pow(math.e, (postScore - prevScore)/T))
	prob = pow(math.e, (postScore - prevScore)/T)
	return prob

def simAnnealHillClimbing(board, iterations, T, d, f=None):
	hillClimbBoard = np.copy(board)
	size = hillClimbBoard[0].size
	eval = int(evalScore(calcNumberToReach(evaluate(hillClimbBoard),size)))
	i=1
	count1 = 0
	count2 = 0

	#fString = ""
	tempT = T
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
		newEval = int(evalScore(calcNumberToReach(evaluate(hillClimbBoard), size)))

		if newEval >= eval:
			#print("SAME", newEval, eval)
			eval = newEval
			#eval>newEval
		elif np.random.random() < simAnnealProb(tempT, d, eval, newEval):
			#print("simmed", newEval, eval)
			eval = newEval
		else:
			#print("revert", newEval, eval)
			hillClimbBoard[coor.row-1,coor.col-1] = prevValue
		#print(eval, " ", newEval, " ", T, "  ", simAnnealProb(T, d, eval, newEval))
		#fString = fString + str(eval) + ","
		tempT = tempT*d
		i += 1
	#f.write(fString+"\n")
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

