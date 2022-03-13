from typing import List, Tuple
from puzzle import Puzzle
def breadth_first_search(initState: str, goalState: str, size: int) -> Tuple[str, int]:
    breadthPuzzle = Puzzle(initState, goalState, size)
    
    