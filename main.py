import node
import generalFunctions
import time
#for pretty much every sytnactic thing such as 2d array or enum or splitting i double checked on geek2geek or w3 schools
#total 9! nodes?
#use 0 to rep blank

test1 = [[1,2,3],[4,5,6],[7,0,8]] #depth 1
#test1 = [[1,2,3],[5,0,6],[4,7,8]] #depth 4
#test1 = [[1,3,6],[5,0,2],[4,7,8]] #depth 8
#test1 = [[1,3,6],[5,0,7],[4,8,2]] #depth 12
#test1 = [[1,6,7],[5,0,3],[4,8,2]] #depth 16
#test1 = [[7,1,2],[4,8,5],[6,3,0]] #depth 20
#test1 = [[0,7,2],[4,6,1],[3,5,8]] #depth 24

def findSmallest(l:list[node.nodes]):
    smallest = l[0].hCost + l[0].depth
    smallestIndex = 0
    secondSmallestIndex = 0
    toRet = []
    for i in range(len(l)):
        if (l[i].hCost + l[i].depth) < smallest:
            secondSmallestIndex = smallestIndex
            smallest = l[i].hCost + l[i].depth
            smallestIndex = i
    toRet.append(smallestIndex)
    toRet.append(secondSmallestIndex)
    return toRet

def Astar(heuristic, puzzle, solved):
    start = time.time()
    theQ = []

    cost = generalFunctions.getCost(heuristic, puzzle, solved)
    theQ.append(node.nodes(puzzle, 0, cost ,heuristic, ['start']))

    currNode = theQ[0]
    secondSmallestCost = cost #this is same as getting from node since depth 0
    childIsSmaller = False
    largestQ = 0
    loc = -1

    visitedNodes = 0

    while len(theQ) > 0:
        if(len(theQ) > largestQ):
            largestQ = len(theQ)

        if(childIsSmaller == False): #if one of the children is not smaller, find best move
            loc = findSmallest(theQ)
            secondSmallestCost = loc[1]
            loc = loc[0]
        else:#if one of the children is smaller, we don't need to find again
            childIsSmaller = False #reset this flag

        if(visitedNodes % 10000 == 0):
           print('nodes visited so far: ' + str(visitedNodes))    

        visitedNodes +=1

        currNode = theQ.pop(loc)
        #input()
        if(currNode.puzzle == solved):
            print('total nodes visited: ' + str(visitedNodes))
            moveNum = 0
            print('largest queue size was: ' + str(largestQ))

            for i in currNode.movesMade: #for each move made, create that puzzle and print out the move made
                print('move ' + str(moveNum) + ': ')
                puzzle = generalFunctions.move(puzzle, i)
                for j in puzzle:
                    print(j)
                moveNum += 1
            break
        else:
            newNodes = currNode.findChildren(solved)
            for i in newNodes:
                theQ.append(i)
                if(i.hCost + i.depth < secondSmallestCost):#this saves a little bit of time hopefully
                    loc = len(theQ) - 1
                    secondSmallestCost = i.hCost + i.depth
                    childIsSmaller = True
                
    end = time.time()
    end = end - start
    generalFunctions.printTime(end)


print('use test cases?')
testCase = input()

puzzle =[]
size = 0

choice = generalFunctions.getHeuristic()

if(testCase == "yes"):
    puzzle = test1
    size = 3
else:
    size = generalFunctions.getSize()
    
    puzzle = generalFunctions.getPuzzle(size)

solved = generalFunctions.solve(puzzle, size)

if puzzle == solved:
    print('puzzle solved, input same as solved puzzle')
    exit
        
if(choice == 0):
    Astar(0, puzzle, solved)
elif(choice == 1):
    Astar(1, puzzle, solved)
elif(choice == 2):
    Astar(2, puzzle, solved)