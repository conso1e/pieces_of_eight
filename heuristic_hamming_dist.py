import game_functons

def heuristic_HammingDist(board, goalState):
    hammingDistance = 0

    for tileIndex in range(len(board)):
        if board[tileIndex] != goalState[tileIndex]:
            hammingDistance += 1

    return hammingDistance


def generateSuccessorStates(board):
    successors = []
    
    avialableMoves = game_functons.getAvailableMoves(board.index(0))
    for availableMove in avialableMoves:
        successor = list(board)
        game_functons.move(successor, availableMove)
        successors.append(successor)

    return successors
