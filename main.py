import random
import math


def initializeBoard():
    board = list(range(0, 9))
    while True:
        random.shuffle(board)
        if computeSumOfPermutationInversions(board) % 2 == 0:
            return board


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


# start of script
board = initializeBoard()
victoryState = [1, 2, 3, 4, 5, 6, 7, 8, 0]

# main game loop
displayBoard(board)
while True: 
    # input validation loop
    availableMoves = getAvailableMoves(board.index(0))
    print('Available Moves Are:', availableMoves)
    direction = input('Enter a direction: ').upper()
    # translate WASD to UP DN RT LT
    if direction in availableMoves:
        move(board, direction)
        displayBoard(board)
        if checkForVictory(board, victoryState):
            print('Congrats!!!')
            break
    else:
        print('Invalid Move')
        displayBoard(board)



