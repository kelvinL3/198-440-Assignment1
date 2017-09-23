#do the hill climbing process
#visualize with an interation by evaluation function graph
#maybe integrate with GUI as to be able to do a step-by-step summary of what happened

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
def basicHillClimbing(board, iterations):
	hillClimbBoard = np.copy(board)
	size = hillClimbBoard[0].size
	eval = evalScore(calcNumberToReach(evaluate(hillClimbBoard),size))
	i=1
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
		else:
			hillClimbBoard[coor.row-1,coor.col-1] = prevValue
		i+=1
	return hillClimbBoard

def hillClimbingWithRandomRestart(size, iterations, restarts):
	preStarts = []
	preDistanceBoards = []
	preEvalStarts = []
	candidates = []
	distanceBoards = []
	evalCandidates = []
	for i in range(0, restarts):
		#print("RETRY", i+1)

		board = generateBoard(size)
		preStarts.append(board)
		#print(board)

		######

		preDistanceBoard = calcNumberToReach(evaluate(board), board[0].size)
		preDistanceBoards.append(preDistanceBoard)
		#print(preDistanceBoard)

		preEvalStarts.append(evalScore(preDistanceBoard))
		#print(evalScore(preDistanceBoard))

		# print("COMPARE FOR EQUALITY")
		# print(preStarts[i])


		tempBoard = np.copy(board)
		tempCandidate = basicHillClimbing(tempBoard, iterations/restarts)
		candidates.append(tempCandidate)
		#print(tempCandidate)

		distanceBoard = calcNumberToReach(evaluate(tempCandidate), tempCandidate[0].size)
		distanceBoards.append(distanceBoard)
		#print(distanceBoard)

		evalCandidates.append(evalScore(distanceBoard))
		#print(evalScore(distanceBoard))




	candidatePairBoardEvalScore = pairOfBoardsEvalScores(preStarts, preDistanceBoards, preEvalStarts, candidates, distanceBoards, evalCandidates)
	return candidatePairBoardEvalScore