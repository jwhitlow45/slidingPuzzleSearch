from typing import List, Tuple
from puzzle import Puzzle

def breadth_first_search(initState: str, goalState: str, size: int) -> Tuple[str, int]:
    numExpansions = 0
    zeroIndex = initState.index('0')
    initState = list(initState)
    goalState = list(goalState)
    
    queue = [(initState, zeroIndex, "")]
    
    while len(queue) > 0:
        stateTuple = queue.pop(0)
        state, zeroIndex, moves = stateTuple
        # check if we have found solution
        if state == goalState:
            return (moves, numExpansions)
        
        # expand and add possible solutions to back of queue
        queue += expand(stateTuple, size)
        numExpansions += 1
        
        
    
def expand(stateTuple: Tuple[str, int, str], size: int) -> List[Tuple[str, int, str]]:
    # unpack for legibility
    state, zeroIndex, moves = stateTuple
    
    possibleMoves = ['l','r','u','d']
    
    oppMoves = {'l':'r',
                'r':'l',
                'u':'d',
                'd':'u'}
    
    if moves:
        possibleMoves.remove(oppMoves[moves[-1]])
    
    newStateTuples = []
    expPuzzle = Puzzle()
    
    # print('expansion')
    # expPuzzle.print_puzzle(state, size)
    # print()
    
    
    for move in possibleMoves:
        newState, newZeroIndex = expPuzzle.move(state=state,
                                                moveset=move, 
                                                zeroIndex=zeroIndex,
                                                size=size)
        if newState != state:
            newStateTuples.append((newState, newZeroIndex, moves + move))
        
    return newStateTuples
        
    
    