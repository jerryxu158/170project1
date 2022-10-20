import copy
import generalFunctions
class nodes:
    def __init__(self, puzzle, depth, hCost, choice, movesMade): # hCost is wrong, i should have depth and heurstic seperate
        self.puzzle = puzzle
        self.depth = depth
        self.hCost = hCost
        self.choice = choice
        self.movesMade = copy.deepcopy(movesMade)

    def findChildren(self, solved):
        toRet=[]
        puzzle = copy.deepcopy(self.puzzle)
        
        loc = generalFunctions.find(puzzle, 0)
        zero = loc[0]
        zeroRow = loc[1]
        toRet = []
        if(zero != 0):#checks if the empty tile is on the very left, if yes, then we can't move it further left
            temp = copy.deepcopy(puzzle[zeroRow][zero-1])
            puzzle[zeroRow][zero-1] = copy.deepcopy(puzzle[zeroRow][zero])
            puzzle[zeroRow][zero] = temp
            moves = copy.deepcopy(self.movesMade)
            moves.append('left')
            #print('moves made ' + str(moves))
            toRet.append(nodes(puzzle, 
                        self.depth + 1, 
                        generalFunctions.getCost(self.choice, puzzle, solved), 
                        self.choice, 
                        moves))
            #for i in puzzle:
            #    print(i)
            puzzle = copy.deepcopy(self.puzzle)

        if zero != len(puzzle[0]) - 1:#checks if the empty tile is on the very right, if so we cannot move any further to the right
            moves = copy.deepcopy(self.movesMade)
            moves.append('right')
            #print('moves made ' + str(moves))
            temp = copy.deepcopy(puzzle[zeroRow][zero+1])
            puzzle[zeroRow][zero+1] = copy.deepcopy(puzzle[zeroRow][zero])
            puzzle[zeroRow][zero] = temp
            toRet.append(nodes(puzzle, 
                        self.depth + 1, 
                        generalFunctions.getCost(self.choice, puzzle, solved), 
                        self.choice, 
                        moves))
            #for i in puzzle:
            #    print(i)
            puzzle = copy.deepcopy(self.puzzle)

        if zeroRow != 0:#if its not the top, move up 1
            moves = copy.deepcopy(self.movesMade)
            moves.append('up')
            #print('moves made ' + str(moves))
            temp = copy.deepcopy(puzzle[zeroRow-1][zero])
            puzzle[zeroRow-1][zero] = copy.deepcopy(puzzle[zeroRow][zero])
            puzzle[zeroRow][zero] = temp
            toRet.append(nodes(puzzle, 
                        self.depth + 1, 
                        generalFunctions.getCost(self.choice, puzzle, solved), 
                        self.choice, 
                        moves))
            #for i in puzzle:
            #    print(i)
            puzzle = copy.deepcopy(self.puzzle)

        if zeroRow != len(puzzle) - 1:#if its not the bottom row, we move 0 down one
            moves = copy.deepcopy(self.movesMade)
            moves.append('down')
            #print('moves made ' + str(moves))
            temp = copy.deepcopy(puzzle[zeroRow+1][zero])
            puzzle[zeroRow+1][zero] = copy.deepcopy(puzzle[zeroRow][zero])
            puzzle[zeroRow][zero] = copy.deepcopy(temp)
            toRet.append(nodes(puzzle, 
                        self.depth + 1, 
                        generalFunctions.getCost(self.choice, puzzle, solved), 
                        self.choice, 
                        moves))
            #for i in puzzle:
            #   print(i)
        return toRet