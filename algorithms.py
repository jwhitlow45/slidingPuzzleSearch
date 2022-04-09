from typing import List, Tuple
from puzzle import Puzzle
from queue import PriorityQueue

EXPANSION_LIMIT = 2000000


def breadth_first_search(initState: str, goalState: str, size: int) -> Tuple[str, int]:
    numExpansions = 0
    zeroIndex = initState.index('0')
    initState = list(initState)
    goalState = list(goalState)

    queue = [(initState, zeroIndex, "")]
    visited = {}

    while len(queue) > 0:
        if numExpansions > EXPANSION_LIMIT:
            return (f'exceeded limit of {EXPANSION_LIMIT} expansions', numExpansions)

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
        if numExpansions > EXPANSION_LIMIT:
            return (f'exceeded limit of {EXPANSION_LIMIT} expansions', numExpansions)

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
    depthLimit = 2

    stack = [[0, initState, zeroIndex, ""]]
    visited = {}

    while len(stack) > 0:
        if numExpansions > EXPANSION_LIMIT:
            return (f'exceeded limit of {EXPANSION_LIMIT} expansions', numExpansions)

        depth, state, z, moves = stack.pop()

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


def a_star_search(initState: str, goalState: str, size: int) -> Tuple[str, int]:
    numExpansions = 0
    zeroIndex = initState.index('0')
    initState = list(initState)
    goalState = list(goalState)

    # dictionary representing goal state, provides O(1) lookup time for computing manhattan distance
    # this is not strictly necessary but it does save a lot of time iterating over indicies
    goalStateDict = {}
    for i, tile in enumerate(goalState):
        goalStateDict[tile] = i

    # priority queue contains following tuple structure
    # (estimated cost [g(n)+h(n)], path cost, state, 0 index, moves)
    pq = PriorityQueue()
    pq.put((0, 0, initState, zeroIndex, ""))
    visited = {}

    while pq.qsize() > 0:
        if numExpansions > EXPANSION_LIMIT:
            return (f'Exceeded limit of {EXPANSION_LIMIT} expansions', numExpansions)

        # in this implementation of a*, depth = path cost because has a cost of
        # 1 since it is adding one step (l,r,u,d) to the final solution
        _, pathCost, state, z, moves = pq.get()

        if ''.join(state) in visited:
            continue
        visited[''.join(state)] = 1

        # check if we have found solution
        if state == goalState:
            return (moves, numExpansions)

        # expand and add possible solutions to pq
        for newStateTuple in expand((state, z, moves), size):
            newState, newZ, newMoves = newStateTuple
            # heuristic = manhattan_distance(newState, goalStateDict, size)
            heuristic = out_of_place(newState, goalState)
            pq.put((pathCost + 1 + heuristic, pathCost +
                   1, newState, newZ, newMoves))
        numExpansions += 1


def a_star_search_iterative(initState: str, goalState: str, size: int) -> Tuple[str, int]:
    numExpansions = 0
    zeroIndex = initState.index('0')
    initState = list(initState)
    goalState = list(goalState)
    depthLimit = 6

    # dictionary representing goal state, provides O(1) lookup time for computing manhattan distance
    # this is not strictly necessary but it does save a lot of time iterating over indicies
    goalStateDict = {}
    for i, tile in enumerate(goalState):
        goalStateDict[tile] = i

    # priority queue contains following tuple structure
    # (estimated cost [g(n)+h(n)], path cost, depth, state, 0 index, moves)
    pq = PriorityQueue()
    tempPQ = PriorityQueue()
    pq.put((0, 0, 0, initState, zeroIndex, ""))
    visited = {}

    while pq.qsize() > 0:
        if numExpansions > EXPANSION_LIMIT:
            return (f'Exceeded limit of {EXPANSION_LIMIT} expansions', numExpansions)

        # in this implementation of a*, depth = path cost because has a cost of
        # 1 since it is adding one step (l,r,u,d) to the final solution
        _, pathCost, depth, state, z, moves = pq.get()

        if ''.join(state) in visited and depth + 1 < depthLimit:
            continue
        visited[''.join(state)] = 1

        # check if we have found solution
        if state == goalState:
            return (moves, numExpansions)

        # expand and add possible solutions to pq
        for newStateTuple in expand((state, z, moves), size):
            newState, newZ, newMoves = newStateTuple
            # heuristic = manhattan_distance(newState, goalStateDict, size)
            heuristic = out_of_place(newState, goalState)

            # if we are within our depth limit then put state into priority queue
            # as normal, otherwise we have exceeded our depth limit and the new
            # state must be stored in a temp priority queue containing all nodes
            # just past the set depth limit. this temp pq is accessed when all
            # nodes within the current depth limit have been explored (pq is empty)
            if depth + 1 < depthLimit:
                pq.put((pathCost + 1 + heuristic, pathCost +
                       1, depth + 1, newState, newZ, newMoves))
            else:
                tempPQ.put((pathCost + 1 + heuristic, pathCost +
                           1, 0, newState, newZ, newMoves))

        if pq.empty():
            pq = tempPQ  # move past current depth limit
            tempPQ = PriorityQueue()  # create new queue for next depth limit

        numExpansions += 1


def expand(stateTuple: Tuple[str, int, str], size: int) -> List[Tuple[str, int, str]]:
    # unpack for legibility
    state, zeroIndex, moves = stateTuple

    possibleMoves = ['l', 'u', 'r', 'd']

    oppMoves = {
        'l': 'r',
        'r': 'l',
        'u': 'd',
        'd': 'u'
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


def out_of_place(state: str, goalState: str) -> int:
    outOfPlaceCount = 0
    for i, j in zip(state, goalState):
        if i != j:
            outOfPlaceCount += 1

    return outOfPlaceCount


def manhattan_distance(state: str, goalStateDict: dict, size: int) -> int:
    totalManhattanDist = 0
    for i, tile in enumerate(state):
        goalIndex = goalStateDict[tile]
        totalManhattanDist += abs(i % size - goalIndex % size)
        totalManhattanDist += abs(int(i / size) - int(goalIndex / size))
    return totalManhattanDist
