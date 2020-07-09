import random
import math
import time
import game_functions
import heuristics


def initializeBoard():
    board = list(range(0, 9))
    while True:
        random.shuffle(board)
        if heuristics.heuristic_sumOfPermutationInversions(board) % 2 == 0:
            return board


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


board = initializeBoard()
visitedStates = [convertToString(board)]
goalState = [1, 2, 3, 4, 5, 6, 7, 8, 0]

print('Welcome to Pieces of Eight!')
while True:
    mode = input('Select Mode: Interactive (i) or Demonstration (d): ').upper()
    if mode == 'I' or mode == 'D':
        break
    print('Please enter a valid mode.')

if mode == 'I':
    displayBoard(board)
    while True: 
        availableMoves = game_functions.getAvailableMoves(board.index(0))
        print('Available Moves Are:', availableMoves)
        direction = input('Enter a direction: ').upper()
        # TODO: translate WASD to UP DN RT LT
        if direction in availableMoves:
            game_functions.move(board, direction)
            displayBoard(board)
            if game_functions.checkForVictory(board, goalState):
                print('Congrats!!!')
                break
        else:
            print('Invalid Move')
            displayBoard(board)
else:
    displayBoard(board)
    turnCounter = 0
    while True:
        turnCounter += 1
        # print('turn', turnCounter)

        minimalState = None
        minimalHeuristic = None
        for successor in heuristics.generateSuccessorStates(board):
            if convertToString(successor) not in visitedStates:
                heuristicEvaluation = heuristics.heuristic_sumOfPermutationInversions(successor)
                if not minimalHeuristic or heuristicEvaluation < minimalHeuristic:
                    minimalState = successor
                    minimalHeuristic = heuristicEvaluation

        if not minimalState:
            print('Search failed in', turnCounter, 'moves. Deadend.')
            break
        
        elif game_functions.checkForVictory(minimalState, goalState):
            displayBoard(minimalState)
            print('Congrats! Solved in', turnCounter, 'moves.')
            break
        else:
            visitedStates.append(convertToString(minimalState))
            board = minimalState
            
        # time.sleep(0.1)
