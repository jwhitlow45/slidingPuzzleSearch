from puzzle import Puzzle
import algorithms
from datetime import datetime

ALGO_NAME = {
    algorithms.breadth_first_search: 'bfs',
    algorithms.depth_first_search: 'dfs',
    algorithms.iterative_deepening_search: 'itdeep',
    algorithms.a_star_search: 'astar',
    algorithms.a_star_search_iterative: 'astarit'
}

ALGOS = [
    algorithms.breadth_first_search,
    algorithms.depth_first_search,
    algorithms.iterative_deepening_search,
    algorithms.a_star_search,
    algorithms.a_star_search_iterative
]

PUZ_FILES = [
    'puzzles3.txt',
    'puzzles4e.txt',
    'puzzles4h.txt'
]

RESULT_FOLDER = 'results/'


def main():
    for puzzleAlgo in ALGOS:
        for fileName in PUZ_FILES:
        
            goalState: str
            puzzles = []
            puz = Puzzle()
            
            with open(fileName, 'r') as FILE:
                goalState = FILE.readline()[:-1]
                while line := FILE.readline():
                    if line[0] == '#':
                        continue
                    puzzles.append(line.strip().split(','))

            outFile = f"{RESULT_FOLDER}{ALGO_NAME[puzzleAlgo]}_{fileName.removesuffix('.txt')}.csv"
            with open(outFile, 'w') as FILE:
                headers = 'state,solution,num expands,time\n'
                lines = [headers]
                for i in range(len(puzzles)):
                    initState = puzzles[i][0]
                    size = int(puzzles[i][1])

                    start = datetime.now()
                    print("Initial state:", ''.join(initState))
                    solution, expands = puzzleAlgo(initState, goalState, size)
                    print("Solution:", solution)
                    print("Expands:", expands)
                    state = puz.move(initState, solution, size)[0]
                    print("Solution tested:", ''.join(state))
                    totalTime = datetime.now() - start
                    print("Time:", totalTime, end='\n\n')
                    newLine = f'{"".join(initState)},{solution},{expands},{totalTime}\n'
                    lines.append(newLine)

                FILE.writelines(lines)

    pass


if __name__ == '__main__':
    main()
