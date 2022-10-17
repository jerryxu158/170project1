import node
import generalFunctions
#for pretty much every sytnactic thing such as 2d array or enum or splitting i double checked on geek2geek or w3 schools
#total 9! nodes?
#use 0 to rep blank
test1 = [[1,3,6],[5,0,2],[4,7,8]]

def findSmallest(l:list[node.nodes]):
    toRet = []
    smallest = l[0].cost
    smallestIndex = 0
    secondSmall = -1
    secondIndex = 0
    for i in range(len(l)):
        if l[i].cost < smallest:
            secondSmall = smallest
            secondIndex = smallestIndex
            smallest = l[i].cost
            smallestIndex = i
    toRet.append(smallestIndex)
    toRet.append(secondSmall)
    return toRet

def Astar(heuristic, puzzle, solved):
    theQ = []
    theQ.append(node.nodes(puzzle, solved, 1, heuristic, ['start']))
    currNode = theQ[0]
    smallestCost = theQ[0].cost
    childIsSmaller = False
    loc = -1
    iterations = 0
    while len(theQ) > 0:
        if(childIsSmaller == False): #if one of the children is not smaller, find best move
            i = findSmallest(theQ)
            loc = i[0]
            smallestCost =i[1]
        else:#if one of the children is smaller, we don't need to find again
            childIsSmaller = False #reset this flag
            #the location is set when we add nodes to the Q
        if(iterations % 10 == 0):
            print('nodes expanded: ' + str(iterations)) 
        iterations +=1
        currNode = theQ.pop(loc)
        #input()
        if(currNode.puzzle == solved):
            iterations = 0
            for i in currNode.movesMade:
                print('move ' + str(iterations) + ': ')
                puzzle = generalFunctions.move(puzzle, i)
                for j in puzzle:
                    print(j)
                iterations += 1
            return
        else:
            #print('making new nodes')
            newNodes = currNode.findChildren()
            for i in newNodes:
                theQ.append(i)
                if(i.cost < smallestCost):
                    loc = len(theQ) - 1
                    smallestCost = i.cost
                    childIsSmaller = True
                    
    
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
print('use test cases?')
choice = input()
puzzle =[]
size = 0
if(choice != "yes"):

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
else:
    puzzle = test1
    size = 3
    choice = 2
solved = solve(puzzle, size)
    
if puzzle == solved:
        print('puzzle solved, input same as solved puzzle')
        exit
        
if(choice == 0):
    Astar(0, puzzle, solved)
elif(choice == 1):
    Astar(1, puzzle, solved)
elif(choice == 2):
    Astar(2, puzzle, solved)

