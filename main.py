from puzzle import Puzzle
import algorithms
from datetime import datetime

def main():
    initState: str
    goalState = "012345678"
    size: int
    puzzles = []
    puz = Puzzle()
    
    with open('puzzles.txt', 'r') as FILE:
        line = None
        while line := FILE.readline():
            puzzles.append(line.strip().split(','))
            
    for i in range(len(puzzles)):
        initState = puzzles[i][0]
        size = int(puzzles[i][1])
    
        print("Initial state:", ''.join(initState))
        start = datetime.now()
        solution, expands = algorithms.iterative_deepening_search(initState, goalState, size)
        print("Solution:", solution)
        print("Expands", expands)
        state = puz.move(initState, solution, size)[0]
        print("Solution tested:", ''.join(state))
        print("Time:", datetime.now() - start)
        print()

    pass

  
    

if __name__ == '__main__':
    main()