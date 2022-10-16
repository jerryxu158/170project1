def find(puzzle, toFind):
        toRet = []
        for i in range(len(puzzle)):
            if(toFind in puzzle[i]):
                toRet.append(i.index(0))
                toRet.append(i)
                break
        return toRet
def misplacedTile(puzzle):
        misplaced = 0
        for i in puzzle:
            puzzle.append(i)
        for i in range(len(puzzle)):
            if puzzle[i] != i+1 and puzzle[i] != 0:
                misplaced+=1
        return misplaced
        
def manhattanSearch(puzzle, solved):
    totalDist = 0
    for i in range(len(puzzle)):
        for j in range(len(i)):#zero being out of place and finding how out of place shouldn't matter, but this is doing it anyways
            if puzzle[i][j] != solved[i][j]:
                locs = find(solved, solved[i][j])
                totalDist += abs(i - locs[1]) + abs(j - locs[0])
    return totalDist
class nodes:
    def init(self, puzzle, solved, cost, choice):
        self.puzzle = puzzle
        self.cost = cost
        self.solved = solved
        self.choice = choice

    def findChildren(self):
        toRet=[]
        puzzle = self.puzzle
        zero = -1
        zeroRow = -1
        for i in range(len(puzzle)):
            if(0 in puzzle[i]):
                zero = i.index(0)
                zerRow = i
                break
        toRet = []
        if(zero != 0):
            temp = puzzle[zeroRow][zero-1]
            puzzle[zeroRow][zero-1] = puzzle[zeroRow][zero]
            puzzle[zeroRow][zero] = temp
            toRet.append(nodes(puzzle, ))
            puzzle = self.puzzle
        if zero != len(puzzle[0]):
            temp = puzzle[zeroRow][zero+1]
            puzzle[zeroRow][zero+1] = puzzle[zeroRow][zero]
            puzzle[zeroRow][zero] = temp
            if self.choice == 0:
                toRet.append(nodes(puzzle, self.solved, self.cost + 1, 0))
            elif(self.choice == 1):
                toRet.append(nodes(puzzle, self.solved, self.cost + 1, misplacedTile(puzzle)))
            else:
                toRet.append(nodes(puzzle, self.solved, self.cost + 1, manhattanSearch(puzzle, self.solved)))