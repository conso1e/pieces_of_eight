import math
import game_functions


def generateSuccessorStates(board):
    successors = []
    
    avialableMoves = game_functions.getAvailableMoves(board.index(0))
    for availableMove in avialableMoves:
        successor = list(board)
        game_functions.move(successor, availableMove)
        successors.append(successor)

    return successors


def heuristic_HammingDist(board, goalState):
    hammingDistance = 0

    for tile in board:
        if tile != 0:
            if board.index(tile) != goalState.index(tile):
                hammingDistance += 1

    return hammingDistance

def heuristic_ManhattanDist(board, goalState):
    manhattanDistance = 0

    for tile in board:
        if tile != 0:
            tileRow = math.floor(board.index(tile) / 3)
            tileCol = board.index(tile) % 3
            targetRow = math.floor(goalState.index(tile) / 3)
            targetCol = goalState.index(tile) % 3

            manhattanDistance += abs(tileRow - targetRow) + abs(tileCol - targetCol)

    return manhattanDistance

# implement more generally
# only words for ordered goal states 
def heuristic_sumOfPermutationInversions(board):
    sumOfPermtationInversions = 0

    for currentTileIndex in range(len(board)):
        for subsequentTileIndex in range(currentTileIndex, len(board)):
            if board[currentTileIndex] != 0 and board[subsequentTileIndex] != 0: 
                if board[currentTileIndex] > board[subsequentTileIndex]:
                    sumOfPermtationInversions += 1

    return sumOfPermtationInversions

    





