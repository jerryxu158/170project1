import node
import generalFunctions
import time
#for pretty much every sytnactic thing such as 2d array or enum or splitting i double checked on geek2geek or w3 schools
#total 9! nodes?
#use 0 to rep blank

#test1 = [[1,2,3], [4,5,6],[7,0,8]] #depth 1
#test1 =[[1,2,3],[5,0,6],[4,7,8]] #depth 4
#test1 = [[1,3,6],[5,0,2],[4,7,8]]  #depth 8
#test1 = [[1,3,6],[5,0,7],[4,8,2]] #depth 12
test1 = [[1,6,7],[5,0,3],[4,8,2]] #depth 16
#test1 =[[0,7,2],[4,6,1],[3,5,8]] #depth 24

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

    iterations = 0

    while len(theQ) > 0:
        if(len(theQ) > largestQ):
            largestQ = len(theQ)

        if(childIsSmaller == False): #if one of the children is not smaller, find best move
            loc = findSmallest(theQ)
            secondSmallestCost = loc[1]
            loc = loc[0]
        else:#if one of the children is smaller, we don't need to find again
            childIsSmaller = False #reset this flag
            #the location is set when we add nodes to the Q

        if(iterations % 10000 == 0):
           print('nodes expanded: ' + str(iterations))    

        iterations +=1

        currNode = theQ.pop(loc)
        #input()
        if(currNode.puzzle == solved):
            print('nodes expanded: ' + str(iterations))
            iterations = 0
            print('largest queue size was: ' + str(largestQ))
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
                if(i.hCost + i.depth < secondSmallestCost):
                    loc = len(theQ) - 1
                    secondSmallestCost = i.hCost + i.depth
                    childIsSmaller = True
                
    end = time.time()
    end = end - start
    timeArr = [0,0,0]
    print('run time was: ' + str(end) + ' seconds')
    if (end > 100):
        inSeconds = end
        timeArr[2] = end%60
        end -= end%60
        end = end / 60
        timeArr[1] = end
        if(end > 60):
            end = end / 60
            timeArr[0] = end
        print('the total run time was ' + str(timeArr[2]) + ' hours, ' + str(timeArr[1]) + ' minutes, ' + str(timeArr[0]) + ' seconds')

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
    choice = 1
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

