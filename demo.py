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

#Task1 - (size, iterations, visualize=True)
basicHillClimbingDriver(11, iterations=6000, visualize=True)

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

