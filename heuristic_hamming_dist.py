import game_functions

def heuristic_HammingDist(board, goalState):
    hammingDistance = 0

    for tileIndex in range(len(board)):
        if board[tileIndex] != goalState[tileIndex]:
            hammingDistance += 1

    return hammingDistance


def generateSuccessorStates(board):
    successors = []
    
    avialableMoves = game_functions.getAvailableMoves(board.index(0))
    for availableMove in avialableMoves:
        successor = list(board)
        game_functions.move(successor, availableMove)
        successors.append(successor)

    return successors



