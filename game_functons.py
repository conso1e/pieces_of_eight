import math


def getAvailableMoves(index):
    moves = ['UP', 'DN', 'RT', 'LT']

    if math.floor(index / 3) == 0:
        moves.remove('UP')
    if math.floor(index / 3) == 2:
        moves.remove('DN')
    if index % 3 == 0:
        moves.remove('LT')
    if index % 3 == 2:
        moves.remove('RT')

    return moves


def move(board, direction):
    swapIndex = board.index(0)

    if direction == 'UP':
        targetIndex = swapIndex - 3
    elif direction == 'DN':
        targetIndex = swapIndex + 3
    elif direction == 'RT':
        targetIndex = swapIndex + 1
    else:
        targetIndex = swapIndex - 1

    board[swapIndex], board[targetIndex] = board[targetIndex], board[swapIndex]


def checkForVictory(board, victoryState):
    for i in range(len(board)):
        if board[i] != victoryState[i]:
            return False
    return True

def convertToString(board):
    return ''.join(map(str, board))    