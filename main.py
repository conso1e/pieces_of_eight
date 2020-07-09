# TODO: solve infinite loop by adding cycle checking 

import random
import math
import time
import game_functons
import heuristic_hamming_dist as hamming


def initializeBoard():
    board = list(range(0, 9))
    while True:
        random.shuffle(board)
        if computeSumOfPermutationInversions(board) % 2 == 0:
            return board


def computeSumOfPermutationInversions(board):
    sumOfPermtationInversions = 0
    for currentNumberIndex in range(len(board)):
        for nextNumbersIndex in range(currentNumberIndex + 1, len(board)):
            if board[currentNumberIndex] > board[nextNumbersIndex]:
                sumOfPermtationInversions += 1
    return sumOfPermtationInversions


def displayBoard(board):
    print()
    count = 1
    for i in range(len(board)):
        print(board[i], end=' ')
        if count % 3 == 0:
            print()
        count += 1
    print()


def convertToString(board):
    return ''.join(map(str, board))  

# start of script
board = initializeBoard()
visitedStates = [convertToString(board)]
goalState = [1, 2, 3, 4, 5, 6, 7, 8, 0]

print('Welcome to Pieces of Eight')

displayBoard(board)


turnCounter = 0
while True:
    turnCounter += 1
    print('turn', turnCounter)

    minimalState = None
    minimalHeuristic = None
    for successor in hamming.generateSuccessorStates(board):
        if convertToString(successor) not in visitedStates:
            heuristicEvaluation = hamming.heuristic_HammingDist(successor, goalState)
            if not minimalHeuristic or heuristicEvaluation < minimalHeuristic:
                minimalState = successor
                minimalHeuristic = heuristicEvaluation

    if not minimalState:
        print('Search Failed. Deadend.')
        break
    
    elif game_functons.checkForVictory(minimalState, goalState):
        displayBoard(minimalState)
        print('Congrats! Solved in', turnCounter, 'moves.')
        break
    else:
        visitedStates.append(convertToString(minimalState))
        board = minimalState
        displayBoard(board)

    # time.sleep(0.05)


# main game loop
# displayBoard(board)
# while True: 
#     # input validation loop
#     availableMoves = getAvailableMoves(board.index(0))
#     print('Available Moves Are:', availableMoves)
#     direction = input('Enter a direction: ').upper()
#     # translate WASD to UP DN RT LT
#     if direction in availableMoves:
#         move(board, direction)
#         displayBoard(board)
#         if checkForVictory(board, victoryState):
#             print('Congrats!!!')
#             break
#     else:
#         print('Invalid Move')
#         displayBoard(board)

