import node
import generalFunctions
import time
#for pretty much every sytnactic thing such as 2d array or enum or splitting i double checked on geek2geek or w3 schools
#total 9! nodes?
#use 0 to rep blank
test1 = [[1,3,6],[5,0,2],[4,7,8]]

def findSmallest(l:list[node.nodes]):
    smallest = l[0].hCost + l[0].depth
    smallestIndex = 0
    for i in range(len(l)):
        if l[i].hCost + l[i].depth < smallest:
            smallest = l[i].hCost + l[i].depth
            smallestIndex = i
    return smallestIndex

def Astar(heuristic, puzzle, solved):
    start = time.time()
    theQ = []
    cost = generalFunctions.getCost(heuristic, puzzle, solved)
    theQ.append(node.nodes(puzzle, 0, cost ,heuristic, ['start']))
    currNode = theQ[0]
    smallestCost = cost #this is same as getting from node since depth 0
    childIsSmaller = False
    largestQ = 0
    loc = -1
    iterations = 0
    while len(theQ) > 0:
        if(len(theQ) > largestQ):
            largestQ = len(theQ)

        if(childIsSmaller == False): #if one of the children is not smaller, find best move
            loc = findSmallest(theQ)
            smallestCost = theQ[loc].hCost + theQ[loc].depth
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
            print('largest qeueu size was: ' + str(largestQ))
            for i in currNode.movesMade:
                print('move ' + str(iterations) + ': ')
                puzzle = generalFunctions.move(puzzle, i)
                for j in puzzle:
                    print(j)
                iterations += 1
            break
        else:
            #print('making new nodes')
            newNodes = currNode.findChildren(solved)
            for i in newNodes:
                theQ.append(i)
                if(i.hCost + i.depth < smallestCost):
                    loc = len(theQ) - 1
                    smallestCost = i.hCost + i.depth
                    childIsSmaller = True
    end = time.time()
    print('run time: ' + str(end - start))
    
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
if(choice == "yes"):
    puzzle = test1
    size = 3
    choice = 2
else:
    choice = generalFunctions.getHeuristic()

    size = generalFunctions.getSize()
    
    puzzle = generalFunctions.getPuzzle(size)

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

