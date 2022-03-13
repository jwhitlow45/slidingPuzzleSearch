from puzzle import Puzzle

def main():
    myPuzzle = Puzzle("0123456789ABCDEF", "0123456789ABCDEF", 4)
    curPuzzle = myPuzzle.move(myPuzzle.initState, "rdrdrdlluuuu", myPuzzle.size)
    Puzzle.print_puzzle(Puzzle, curPuzzle, 4)

    pass

  
    

if __name__ == '__main__':
    main()