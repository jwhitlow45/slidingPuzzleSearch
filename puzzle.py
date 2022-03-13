from typing import Tuple, List

class Puzzle:
    def __init__(self, initState: str, goalState: str, size: int):
        self.initState = list(initState)
        self.goalState = list(goalState)
        self.size = size
    
        
    def index_to_coord(self, index: int) -> Tuple[int, int]:
        if index >= len(self.initState):
            print('WARNING: OUT OF PUZZLE BOUNDS!')
        return (int(index/self.size), index%self.size)
    
    def coord_to_index(self, col: int, row: int) -> int:
        if row >= self.size or col >= self.size:
            print('WARNING: OUT OF PUZZLE BOUNDS!')
        return row * self.size + col
    
    def print_states(self):  
        print('Init state:')
        Puzzle.print_puzzle(Puzzle, self.initState, self.size)
        print('Goal state:')
        Puzzle.print_puzzle(Puzzle, self.goalState, self.size)
        
    def move(cls, curState: List[str], move: str):
        pass
    
    def print_puzzle(cls, puzzle: str, size: int):
        for i, tile in enumerate(puzzle):
            print(tile, end=' ')
            if (i - size + 1) % size == 0:
                print('')
