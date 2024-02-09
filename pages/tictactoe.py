ticTacToe = [
    ['.', '.', '.'],
    ['.', '.', '.'],
    ['.', '.', '.']
]
playerSymbol = ' '
machineSymbol = ' '

def getCurrentStateOfTicTacToe():
    print()
    for row in ticTacToe:
        for column in row:
            print(column, end=' ')
        print()
    print()

def isTicTacToeFull():
    for row in ticTacToe:
        for column in row:
            if column == '.':
                return False
    return True

COEFFICIENT_FOR_DEPTH_CHECKING = 10

def judgeCurrentStateBasedOfCoefficients(currentDepthOfGame):
    for row in ticTacToe:
        if row[0] == row[1] and row[0] == row[2]:
            if row[0] == playerSymbol:
                return currentDepthOfGame - COEFFICIENT_FOR_DEPTH_CHECKING
            elif row[0] == machineSymbol:
                return COEFFICIENT_FOR_DEPTH_CHECKING - currentDepthOfGame
    for column in range(3):
        if ticTacToe[0][column] == ticTacToe[1][column] and ticTacToe[0][column] == ticTacToe[2][column]:
            if ticTacToe[0][column] == playerSymbol:
                return currentDepthOfGame - COEFFICIENT_FOR_DEPTH_CHECKING
            elif ticTacToe[0][column] == machineSymbol:
                return COEFFICIENT_FOR_DEPTH_CHECKING - currentDepthOfGame
    if ticTacToe[0][0] == ticTacToe[1][1] and ticTacToe[0][0] == ticTacToe[2][2]:
        if ticTacToe[0][0] == playerSymbol:
            return currentDepthOfGame - COEFFICIENT_FOR_DEPTH_CHECKING
        elif ticTacToe[0][0] == machineSymbol:
            return COEFFICIENT_FOR_DEPTH_CHECKING - currentDepthOfGame
    if ticTacToe[0][2] == ticTacToe[1][1] and ticTacToe[0][2] == ticTacToe[2][0]:
        if ticTacToe[0][2] == playerSymbol:
            return currentDepthOfGame - COEFFICIENT_FOR_DEPTH_CHECKING
        elif ticTacToe[0][2] == machineSymbol:
            return COEFFICIENT_FOR_DEPTH_CHECKING - currentDepthOfGame
    return 0

def hasNoWinner():
    if judgeCurrentStateBasedOfCoefficients(0) == 0:
        return True
    return False

def placeSymbol(row, column, isPlayersTurn):
    global ticTacToe
    if isPlayersTurn:
        ticTacToe[row][column] = playerSymbol
    else:
        ticTacToe[row][column] = machineSymbol
    print("New state of TicTacToe: ")
    getCurrentStateOfTicTacToe()
    if not hasNoWinner():
        if isPlayersTurn:
            print("You win!")
        else:
            print("You lose!")

def minValue(alpha, beta, currentDepth):
    if isTicTacToeFull():
        return 0
    currentCoefficient = judgeCurrentStateBasedOfCoefficients(currentDepth)
    if currentCoefficient != 0:
        return currentCoefficient
    bestValue = float('inf')
    for row in range(3):
        for column in range(3):
            if ticTacToe[row][column] == '.':
                ticTacToe[row][column] = playerSymbol
                bestValue = min(bestValue, maxValue(alpha, beta, currentDepth + 1))
                ticTacToe[row][column] = '.'
                if bestValue <= alpha:
                    return bestValue
                beta = min(beta, bestValue)
    return bestValue

def maxValue(alpha, beta, currentDepth):
    if isTicTacToeFull():
        return 0
    currentCoefficient = judgeCurrentStateBasedOfCoefficients(currentDepth)
    if currentCoefficient != 0:
        return currentCoefficient
    bestValue = float('-inf')
    for row in range(3):
        for column in range(3):
            if ticTacToe[row][column] == '.':
                ticTacToe[row][column] = machineSymbol
                bestValue = max(bestValue, minValue(alpha, beta, currentDepth + 1))
                ticTacToe[row][column] = '.'
                if bestValue >= beta:
                    return bestValue
                alpha = max(alpha, bestValue)
    return bestValue

def minimaxAlphaBetaDecision():
    bestValue = float('-inf')
    bestPlace = [-1, -1]
    for row in range(3):
        for column in range(3):
            if ticTacToe[row][column] == '.':
                ticTacToe[row][column] = machineSymbol
                currentValue = minValue(float('-inf'), float('inf'), 0)
                ticTacToe[row][column] = '.'
                if currentValue > bestValue:
                    bestValue = currentValue
                    bestPlace[0] = row
                    bestPlace[1] = column
    return bestPlace

isPlayersTurn = False

def treatPlayersAnswer(answer):
    answer = answer.lower()
    global playerSymbol, machineSymbol, isPlayersTurn
    if answer == "yes":
        playerSymbol = 'X'
        machineSymbol = 'O'
        isPlayersTurn = True
    else:
        playerSymbol = 'O'
        machineSymbol = 'X'
    print("You are playing with \"" + playerSymbol + "\".")

getCurrentStateOfTicTacToe()
print("Possible places to mark are signed with \".\".")
answer = input("Do you want to start the game? ")
treatPlayersAnswer(answer)
row = 0
column = 0
while not isTicTacToeFull() and hasNoWinner():
    if isPlayersTurn:
        print("Insert your wanted row and column: ")
        row, column = map(int, input().split())
        placeSymbol(row - 1, column - 1, isPlayersTurn)
        isPlayersTurn = False
    if isTicTacToeFull() or not hasNoWinner():
        break
    print("Machine plays.")
    bestMachineMove = minimaxAlphaBetaDecision()
    placeSymbol(bestMachineMove[0], bestMachineMove[1], isPlayersTurn)
    isPlayersTurn = True
if isTicTacToeFull() and hasNoWinner():
    print("It's a draw!")


