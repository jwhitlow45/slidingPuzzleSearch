from puzzle import Puzzle
import algorithms
from datetime import datetime

def main():
    goalState: str
    puzzles = []
    puz = Puzzle()
    
    # puzzles3.txt (3x3), puzzles4e.txt (4x4 easy), puzzles4h.txt (4x4 hard)
    fileName = "puzzles4e.txt"
    
    with open(fileName, 'r') as FILE:
        goalState = FILE.readline()[:-1]
        line = None
        while line := FILE.readline():
            puzzles.append(line.strip().split(','))
            
    for i in range(len(puzzles)):
        initState = puzzles[i][0]
        size = int(puzzles[i][1])
    
        print("Initial state:", ''.join(initState))
        start = datetime.now()
        solution, expands = algorithms.a_star_search(initState, goalState, size)
        print("Solution:", solution)
        print("Expands:", expands)
        state = puz.move(initState, solution, size)[0]
        print("Solution tested:", ''.join(state))
        print("Time:", datetime.now() - start, end='\n\n')
    
    pass

  
    

if __name__ == '__main__':
    main()