from typing import List, Tuple
from puzzle import Puzzle

def breadth_first_search(initState: str, goalState: str, size: int) -> Tuple[str, int]:
    numExpansions = 0
    zeroIndex = initState.index('0')
    initState = list(initState)
    goalState = list(goalState)
    
    queue = [(initState, zeroIndex, "")]
    visited = {}
    
    while len(queue) > 0:
        stateTuple = queue.pop(0)
        state, zeroIndex, moves = stateTuple
        
        if ''.join(state) in visited:
            continue
        visited[''.join(state)] = 1
        
        # check if we have found solution
        if state == goalState:
            return (moves, numExpansions)
        
        # expand and add possible solutions to back of queue
        queue += expand(stateTuple, size)
        numExpansions += 1
        
def depth_first_search(initState: str, goalState: str, size: int) -> Tuple[str, int]:
    numExpansions = 0
    zeroIndex = initState.index('0')
    initState = list(initState)
    goalState = list(goalState)
    
    stack = [(initState, zeroIndex, "")]
    visited = {}
    
    while len(stack) > 0:
        stateTuple = stack.pop(-1)
        state, zeroIndex, moves = stateTuple
        
        if ''.join(state) in visited:
            continue
        visited[''.join(state)] = 1
        
        # check if we have found solution
        if state == goalState:
            return (moves, numExpansions)
        
        # expand and add possible solutions to top of stack
        stack += expand(stateTuple, size)
        numExpansions += 1
        
def iterative_deepening_search(initState: str, goalState: str, size: int) -> Tuple[str, int]:
    numExpansions = 0
    zeroIndex = initState.index('0')
    initState = list(initState)
    goalState = list(goalState)
    depthLimit = 10
    
    stack = [[0, initState, zeroIndex, ""]]
    visited = {}
    
    while len(stack) > 0:
        depth, state, z, moves = stack.pop()
        # print(depth, state, z, moves)
        # if len(stack) > 100:
        #     break
        
        # check if solution has already been explored
        if ''.join(state) in visited:
            continue
        visited[''.join(state)] = 1
        
        # check if we have found solution
        if state == goalState:
            return (moves, numExpansions)
        
        # expand and add possible solutions to top of stack if less than depth limit
        # add to bottom of stack if greater than depth limit so that all states
        # which have not hit depth limit are evaluated first
        for newState in expand((state, z, moves), size):
            if depth + 1 < depthLimit:
                newState = [depth + 1] + list(newState)
                stack += [newState]
            else:
                newState = [0] + list(newState)
                stack = [newState] + stack
                
        # track number of expansions
        numExpansions += 1   
    
def expand(stateTuple: Tuple[str, int, str], size: int) -> List[Tuple[str, int, str]]:
    # unpack for legibility
    state, zeroIndex, moves = stateTuple
    
    possibleMoves = ['l','u','r','d']
    
    oppMoves = {
        'l':'r',
        'r':'l',
        'u':'d',
        'd':'u'
    }
    
    # don't expand on opposite of last move as it is a waste of space and will
    # immediately be rejected as a prior state
    if moves:
        possibleMoves.remove(oppMoves[moves[-1]])
    
    newStateTuples = []
    expPuzzle = Puzzle()
    
    for move in possibleMoves:
        newState, newZeroIndex = expPuzzle.move(state=state,
                                                moveset=move, 
                                                zeroIndex=zeroIndex,
                                                size=size)
        if newState != state:
            newStateTuples.append((newState, newZeroIndex, moves + move))
        
    return newStateTuples
        
    
    