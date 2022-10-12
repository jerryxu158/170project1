
#for pretty much every sytnactic thing such as 2d array or enum or splitting i double checked on geek2geek or w3 schools

#use 0 to rep blank

test = [8,7,6,5,4,3,2,1,0]#for misplaced tile
test1 = [[8,7,6],[5,4,3],[2,1,0]]#for manhattan
solvedState = [1,2,3,4,5,6,7,8,0]
solvedState1 = [[1,2,3],[4,5,6],[7,8,0]]

uniformSearch = 0
def misplacedTile(puzzle):
    misplaced = 0
    for i in range(len(puzzle)):
        if puzzle[i] != i+1 and puzzle[i] != 0:
            misplaced+=1
    return misplaced
        

def manhattanSearch(puzzle):
    totalDist = 0
    for i in puzzle:
        for j in range(len(i)):
            print(j)

def Astar(cost, heuristic, puzzle, solved):
    if puzzle == solved:
        print('already solved puzzle inputted')
        return 0

def solve(puzzle, choice, size = 0):
    toRet = []
    temp = []
    if choice == 0 or choice == 1:
        for i in range(len(puzzle)):
            toRet.append(i+1)
    else:
        for i in range(len(puzzle)):
            temp.append(i+1)
            if len(temp) == size:
                toRet.appen(temp)
                temp = []

print('please choose your heuristic:')
print('    0: uniform cost search')
print('    1: misplaced tile heuristic')
print('    2: manhattan distance heuristic')
choice = input()
print('plese input a puzzle')
print('   please use the format of:')
print('   1,2,3')
print('   3,5,6')
print('   7,8,0')
puzzle = input()
puzzle += input()
puzzle += input()
if(choice == 0):
    puzzle = solve(puzzle)
elif(choice == 1):
    print(choice)
elif(choice == 2):
    print(choice)
else:
    print('unknown choice, exiting program')

