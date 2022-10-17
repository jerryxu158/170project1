import node
#for pretty much every sytnactic thing such as 2d array or enum or splitting i double checked on geek2geek or w3 schools

#use 0 to rep blank

test1 = [[8,7,6],[5,4,3],[2,1,0]]
solvedState1 = [[1,2,3],[4,5,6],[7,8,0]]

def Astar(cost, heuristic, puzzle, solved):
    print(cost)
    
def solve(puzzle, size):
    toRet = []
    temp = []
    num = 1
    for j in puzzle:
        for i in range(len(j)):
            temp.append(num)
            num+=1
        toRet.append(temp)
        temp = []
    toRet[len(toRet) - 1][len(toRet) - 1] = 0
    return toRet

print('please choose your heuristic:')
print('    0: uniform cost search')
print('    1: misplaced tile heuristic')
print('    2: manhattan distance heuristic')

choice = int(input())
if choice != 0 and choice != 1 and choice != 2:
    print('unknown choice, exiting program')
    exit

print('please input the size of your puzzle')
size = int(input())
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
solved = solve(puzzle, size)
    
if puzzle == solved:
        print('puzzle solved, input same as solved puzzle')
        exit
        
if(choice == 0):
    Astar(1, 0, puzzle, solved)
elif(choice == 1):
    Astar(1, 1, puzzle, solved)
elif(choice == 2):
    Astar(1, 2, puzzle, solved)

