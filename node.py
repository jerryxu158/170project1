import copy
import generalFunctions
class nodes:
    def init(self, puzzle, solved, cost, choice):
        self.puzzle = puzzle
        self.cost = cost
        self.solved = solved
        self.choice = choice

    def findChildren(self):
        toRet=[]
        puzzle = copy.deepcopy(self.puzzle)
        
        loc = generalFunctions.find(puzzle, 0)
        zero = loc[0]
        zeroRow = loc[1]

        toRet = []

        if(zero != 0):#checks if the empty tile is on the very left, if yes, then we can't move it further left
            temp = puzzle[zeroRow][zero-1]
            puzzle[zeroRow][zero-1] = puzzle[zeroRow][zero]
            puzzle[zeroRow][zero] = temp
            if self.choice == 0:
                toRet.append(nodes(puzzle, self.solved, self.cost + 1, 0))
            elif(self.choice == 1):
                toRet.append(nodes(puzzle, self.solved, self.cost + 1, generalFunctions.misplacedTile(puzzle)))
            else:
                toRet.append(nodes(puzzle, self.solved, self.cost + 1, generalFunctions.manhattanSearch(puzzle, self.solved)))
            puzzle = copy.deepcopy(self.puzzle)

        if zero != len(puzzle[0]) - 1:#checks if the empty tile is on the very right, if so we cannot move any further to the right
            temp = puzzle[zeroRow][zero+1]
            puzzle[zeroRow][zero+1] = puzzle[zeroRow][zero]
            puzzle[zeroRow][zero] = temp
            if self.choice == 0:
                toRet.append(nodes(puzzle, self.solved, self.cost + 1, 0))
            elif(self.choice == 1):
                toRet.append(nodes(puzzle, self.solved, self.cost + 1, generalFunctions.misplacedTile(puzzle)))
            else:
                toRet.append(nodes(puzzle, self.solved, self.cost + 1, generalFunctions.manhattanSearch(puzzle, self.solved)))
            puzzle = copy.deepcopy(self.puzzle)

        if zeroRow != 0:
            temp = puzzle[zeroRow-1][zero]
            puzzle[zeroRow-1][zero] = puzzle[zeroRow][zero]
            puzzle[zeroRow][zero] = temp
            if self.choice == 0:
                toRet.append(nodes(puzzle, self.solved, self.cost + 1, 0))
            elif(self.choice == 1):
                toRet.append(nodes(puzzle, self.solved, self.cost + 1, generalFunctions.misplacedTile(puzzle)))
            else:
                toRet.append(nodes(puzzle, self.solved, self.cost + 1, generalFunctions.manhattanSearch(puzzle, self.solved)))
            puzzle = copy.deepcopy(self.puzzle)

        if zeroRow != len(puzzle) - 1:
            temp = puzzle[zeroRow+1][zero]
            puzzle[zeroRow+1][zero] = puzzle[zeroRow][zero]
            puzzle[zeroRow][zero] = temp
            if self.choice == 0:
                toRet.append(nodes(puzzle, self.solved, self.cost + 1, 0))
            elif(self.choice == 1):
                toRet.append(nodes(puzzle, self.solved, self.cost + 1, generalFunctions.misplacedTile(puzzle)))
            else:
                toRet.append(nodes(puzzle, self.solved, self.cost + 1, generalFunctions.manhattanSearch(puzzle, self.solved)))
        return toRet