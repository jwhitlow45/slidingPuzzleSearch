from puzzle import Puzzle
import algorithms

def main():
    initState = "462301587"
    goalState = "012345678"
    size = 3
    puz = Puzzle()
    
    print("Initial state")
    puz.print_puzzle(initState, size)
    solution, expands = algorithms.breadth_first_search(initState, goalState, size)
    print("Solution:", solution)
    print("Expands", expands)
    print("Solution tested:")
    state = puz.move(initState, solution, size)[0]
    puz.print_puzzle(state, size)

    pass

  
    

if __name__ == '__main__':
    main()