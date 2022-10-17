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
def misplacedTile(puzzle):
        misplaced = 0
        temp = []
        for i in puzzle:
            temp.append(i)
        puzzle = temp
        for i in range(len(puzzle)):
            if puzzle[i] != i+1 and puzzle[i] != 0:
                misplaced+=1
        return misplaced
        
def manhattanSearch(puzzle, solved):
    totalDist = 0
    for i in range(len(puzzle)):
        for j in range(len(puzzle[i])): #zero being out of place and finding how out of place shouldn't matter, but this is doing it anyways
            if puzzle[i][j] != solved[i][j]:
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