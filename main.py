# TODO: generalize som of pi heuristic
# TODO: avoid deadends 

import time
import game_functions
import heuristics


board = game_functions.initializeBoard()
visitedStates = [game_functions.convertToString(board)]
goalState = [1, 2, 3, 4, 5, 6, 7, 8, 0]

print('Welcome to Pieces of Eight!')
while True:
    mode = input('Select Mode: Interactive (i) or Demonstration (d): ').upper()
    if mode == 'I' or mode == 'D':
        break
    print('Please enter a valid mode.')

if mode == 'I':
    game_functions.displayBoard(board)
    while True: 
        availableMoves = game_functions.getAvailableMoves(board.index(0))
        print('Available Moves Are:', availableMoves)
        direction = input('Enter a direction: ').upper()
        # TODO: translate WASD to UP DN RT LT
        if direction in availableMoves:
            game_functions.move(board, direction)
            game_functions.displayBoard(board)
            if game_functions.checkForVictory(board, goalState):
                print('Congrats!!!')
                break
        else:
            print('Invalid Move')
            game_functions.displayBoard(board)
else:
    game_functions.displayBoard(board)
    turnCounter = 0
    while True:
        turnCounter += 1

        minimalState = None
        minimalHeuristic = None
        for successor in heuristics.generateSuccessorStates(board):
            if game_functions.convertToString(successor) not in visitedStates:
                heuristicEvaluation = heuristics.heuristic_sumOfPermutationInversions(successor)
                if not minimalHeuristic or heuristicEvaluation < minimalHeuristic:
                    minimalState = successor
                    minimalHeuristic = heuristicEvaluation

        if not minimalState:
            print('Search failed in', turnCounter, 'moves. Deadend.')
            break
        elif game_functions.checkForVictory(minimalState, goalState):
            game_functions.displayBoard(minimalState)
            print('Congrats! Solved in', turnCounter, 'moves.')
            break
        else:
            visitedStates.append(game_functions.convertToString(minimalState))
            board = minimalState
            
        # time.sleep(0.1)
