def find(puzzle, toFind):
        toRet = []
        #print('looking for: '+ str(toFind))
        for i in range(len(puzzle)):
            #print(puzzle[i])
            #print(toFind in puzzle[i] )
            if(toFind in puzzle[i]):# if the num to find is in this level of the matrix, find its location, break and return the positions
                toRet.append(puzzle[i].index(toFind))
                toRet.append(i)
                
                break
        return toRet
def misplacedTile(puzzle, solved):
        misplaced = 0
        for i in range(len(puzzle)):
            for j in range(i):
                if(puzzle[i][j] != solved [i][j]):
                    misplaced += 1
        return misplaced
        
def manhattanSearch(puzzle, solved):
    totalDist = 0
    for i in range(len(puzzle)):
        for j in range(len(puzzle[i])): #zero being out of place and finding how out of place shouldn't matter, but this is doing it anyways
            if (puzzle[i][j] != solved[i][j]):
                locs = find(solved, solved[i][j])
                totalDist += abs(i - locs[1]) + abs(j - locs[0])
    return totalDist

def move(puzzle, move):
    loc = find(puzzle, 0)
    zeroCol = loc[0]
    zeroRow = loc[1]
    if(move == 'start'):
        return puzzle
    elif(move == 'up'):
        puzzle[zeroRow][zeroCol] = puzzle[zeroRow - 1][zeroCol]
        puzzle[zeroRow - 1][zeroCol] = 0
    elif (move == 'down'):
        puzzle[zeroRow][zeroCol] = puzzle[zeroRow + 1][zeroCol]
        puzzle[zeroRow + 1][zeroCol] = 0
    elif (move == 'left'):
        puzzle[zeroRow][zeroCol] = puzzle[zeroRow][zeroCol - 1]
        puzzle[zeroRow][zeroCol - 1] = 0
    else:
        puzzle[zeroRow][zeroCol] = puzzle[zeroRow][zeroCol+1]
        puzzle[zeroRow][zeroCol+1] = 0
    return puzzle

def getHeuristic():
    print('please choose your heuristic:')
    print('    0: uniform cost search')
    print('    1: misplaced tile heuristic')
    print('    2: manhattan distance heuristic')

    choice = int(input())
    if choice != 0 and choice != 1 and choice != 2:
        print('unknown choice, exiting program')
        exit
def getSize():
    print('please input the size of your puzzle')
    size = input()
    if type(size) != int:
        print('non integer input, exiting')
        exit
    size = int(size)
    return size

def getPuzzle(size):
    print('plese input a puzzle')
    puzzle =[]
    for i in range(size):
        puzzle += input()

    temp = []
    for i in puzzle:
        if i.isnumeric() == False and i !=',':
            print('invalid input')
            exit
        elif i != ',':
            temp.append(int(i))
    puzzle = []
    temp1 = []
    for i in temp:
        temp1.append(i)
        if(len(temp1) == size):
            puzzle.append(temp1)
            temp1 = []
def getCost(heuristic, puzzle, solved):
    cost = 0
    if(heuristic == 0):
        cost = 0
    elif heuristic == 1:
        cost = misplacedTile(puzzle, solved)
    else:
        cost = manhattanSearch(puzzle, solved)
    return cost