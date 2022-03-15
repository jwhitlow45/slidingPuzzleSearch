from puzzle import Puzzle
import algorithms
from datetime import datetime

def main():
    goalState = "123456789ABCDEF0"
    puzzles = []
    puz = Puzzle()
    
    # puzzles3.txt, puzzles4e.txt (easy), puzzles4h.txt (hard)
    fileName = "puzzles4e.txt"
    
    with open(fileName, 'r') as FILE:
        line = None
        while line := FILE.readline():
            puzzles.append(line.strip().split(','))
            
    for i in range(len(puzzles)):
        initState = puzzles[i][0]
        size = int(puzzles[i][1])
        print(initState, size)
    
        print("Initial state:", ''.join(initState))
        start = datetime.now()
        solution, expands = algorithms.breadth_first_search(initState, goalState, size)
        print("Solution:", solution)
        print("Expands:", expands)
        state = puz.move(initState, solution, size)[0]
        print("Solution tested:", ''.join(state))
        print("Time:", datetime.now() - start)
        print()
    
    pass

  
    

if __name__ == '__main__':
    main()