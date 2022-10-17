import node
#for pretty much every sytnactic thing such as 2d array or enum or splitting i double checked on geek2geek or w3 schools

#use 0 to rep blank

test1 = [[8,7,6],[5,4,3],[2,1,0]]
solvedState1 = [[1,2,3],[4,5,6],[7,8,0]]

def Astar(cost, heuristic, puzzle, solved):
    if puzzle == solved:
        print('puzzle solved, input same as solved puzzle')
        
        return 0
    
def solve(puzzle, size):
    toRet = []
    temp = []
    for i in range(len(puzzle)):
        temp.append(i+1)
        if len(temp) == size:
            toRet.append(temp)
            temp = []
    return toRet

print('please choose your heuristic:')
print('    0: uniform cost search')
print('    1: misplaced tile heuristic')
print('    2: manhattan distance heuristic')

choice = int(input())
if choice != 0 and choice != 1 and choice != 2:
    print('unknown choice, exiting program')
    exit

print('plese input a puzzle')
print('   please use the format of:')
print('   1,2,3')
print('   4,5,6')
print('   7,8,0')
puzzle = input()
size = len(puzzle)/2 + 1
puzzle += input()
puzzle += input()
temp =[]
for i in puzzle:
    if i.isnumeric() == False and i !=',':
        print('invalid input')
        exit
    elif i != ',':
        temp.append(i)
puzzle = temp
        
solved = solve(puzzle, size)
if(choice == 0):
    Astar(1, 0, puzzle, solved)
elif(choice == 1):
    Astar(1, 1, puzzle, solved)
elif(choice == 2):
    Astar(1, 2, puzzle, solved)

