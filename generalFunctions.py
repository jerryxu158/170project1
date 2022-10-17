import node
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
        for j in range(len(i)):#zero being out of place and finding how out of place shouldn't matter, but this is doing it anyways
            if puzzle[i][j] != solved[i][j]:
                locs = find(solved, solved[i][j])
                totalDist += abs(i - locs[1]) + abs(j - locs[0])
    return totalDist

def findSmallest(l:list[node.nodes]):
    smallest = l[0].cost
    smallestIndex = 0
    for i in range(len(l)):
        if l[i].cost < smallest:
            smallest = l[i].cost
            smallestIndex = i
    return smallestIndex
