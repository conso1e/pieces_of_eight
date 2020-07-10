# TODO: generalize som of pi heuristic
# TODO: avoid deadends 
# TODO: fix wonky board initialization logic. verify goal and board?

import time
import game_functions
import heuristics
import a_star

goalState = [1, 2, 3, 4, 5, 6, 7, 8, 0]
board = game_functions.initializeBoard(goalState)
visitedStates = [game_functions.convertToString(board)]

board = [5, 0, 8, 4, 2, 1, 7, 3, 6]

game_functions.displayBoard(board)

# path = a_star.A_Star(board, goalState)

# if path:
#     for node in path:
#         # print('move', count)
#         game_functions.displayBoard(node)

#     print('Congrats! solved in', len(path), 'moves.')
# else:
#     print('zer is a bug is ze program :(')

# print('Welcome to Pieces of Eight!')
# while True:
#     mode = input('Select Mode: Interactive (i) or Demonstration (d): ').upper()
#     if mode == 'I' or mode == 'D':
#         break
#     print('Please enter a valid mode.')

# if mode == 'I':
#     game_functions.displayBoard(board)
#     while True: 
#         availableMoves = game_functions.getAvailableMoves(board.index(0))
#         print('Available Moves Are:', availableMoves)
#         direction = input('Enter a direction: ').upper()
#         # TODO: translate WASD to UP DN RT LT
#         if direction in availableMoves:
#             game_functions.move(board, direction)
#             game_functions.displayBoard(board)
#             if game_functions.checkForVictory(board, goalState):
#                 print('Congrats!!!')
#                 break
#         else:
#             print('Invalid Move')
#             game_functions.displayBoard(board)
# else:
#     game_functions.displayBoard(board)
#     turnCounter = 0
#     while True:
#         turnCounter += 1

#         minimalState = None
#         minimalHeuristic = None
#         for successor in heuristics.generateSuccessorStates(board):
#             if game_functions.convertToString(successor) not in visitedStates:
#                 heuristicEvaluation = heuristics.heuristic_sumOfPermutationInversions(successor)
#                 if not minimalHeuristic or heuristicEvaluation < minimalHeuristic:
#                     minimalState = successor
#                     minimalHeuristic = heuristicEvaluation

#         if not minimalState:
#             print('Search failed in', turnCounter, 'moves. Deadend.')
#             break
#         elif game_functions.checkForVictory(minimalState, goalState):
#             game_functions.displayBoard(minimalState)
#             print('Congrats! Solved in', turnCounter, 'moves.')
#             break
#         else:
#             visitedStates.append(game_functions.convertToString(minimalState))
#             board = minimalState
            
#         # time.sleep(0.1)
