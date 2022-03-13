from typing import Tuple, List

class Puzzle:
    def __init__(self, initState: str, goalState: str, size: int):
        self.initState = list(initState)
        self.goalState = list(goalState)
        self.size = size
    
    def swap_tiles(cls, state: List[str], pos0: int, pos1: int):
        temp = state[pos0]
        state[pos0] = state[pos1]
        state[pos1] = temp
        return state
    
    def __moveLeft(cls, state: List[str], zeroIndex: int, size: int) -> Tuple[List[str], int]:
        """move 0 tile (empty tile) left one space

        Args:
            curState (List[str]): current puzzle state
            zeroIndex (int): index of 0 tile (empty space)
            size (int): size of puzzle

        Returns:
            Tuple[List[str], int]: new puzzle state and index of zero tile
        """
        # check if valid move
        if zeroIndex % size == 0:
            print('WARNING: INVALID MOVE!')
            return (state, zeroIndex)
        # make move
        state = cls.swap_tiles(state, zeroIndex, zeroIndex - 1)
        zeroIndex -= 1
        return (state, zeroIndex)

    def __moveRight(cls, state: List[str], zeroIndex: int, size: int) -> Tuple[List[str], int]:
        """move 0 tile (empty tile) right one space

        Args:
            curState (List[str]): current puzzle state
            zeroIndex (int): index of 0 tile (empty space)
            size (int): size of puzzle

        Returns:
            Tuple[List[str], int]: new puzzle state and index of zero tile
        """
        # check if valid move
        if zeroIndex % size == size - 1:
            print('WARNING: INVALID MOVE!')
            return (state, zeroIndex)
        # make move
        state = cls.swap_tiles(state, zeroIndex, zeroIndex + 1)
        zeroIndex += 1
        return (state, zeroIndex)

    def __moveUp(cls, state: List[str], zeroIndex: int, size: int) -> Tuple[List[str], int]:
        """move 0 tile (empty tile) up one space

        Args:
            curState (List[str]): current puzzle state
            zeroIndex (int): index of 0 tile (empty space)
            size (int): size of puzzle

        Returns:
            Tuple[List[str], int]: new puzzle state and index of zero tile
        """
        # check if valid move
        if zeroIndex < size:
            print('WARNING: INVALID MOVE!')
            return (state, zeroIndex)
        # make move
        state = cls.swap_tiles(state, zeroIndex, zeroIndex - size)
        zeroIndex -= size
        return (state, zeroIndex)
    
    def __moveDown(cls, state: List[str], zeroIndex: int, size: int) -> Tuple[List[str], int]:
        """move 0 tile (empty tile) down one space

        Args:
            curState (List[str]): current puzzle state
            zeroIndex (int): index of 0 tile (empty space)
            size (int): size of puzzle

        Returns:
            Tuple[List[str], int]: new puzzle state and index of zero tile
        """
        # check if valid move
        if zeroIndex >= size * (size - 1):
            print('WARNING: INVALID MOVE!')
            return (state, zeroIndex)
        # make move
        state = cls.swap_tiles(state, zeroIndex, zeroIndex + size)
        zeroIndex += size
        return (state, zeroIndex)
         
    def move(cls, state: str, moveset: str, size: int) -> List[str]:
        """given a puzzle state, performs moves left, right, up, or down from
        moveset on puzzle and puzzle state after performed moves

        Args:
            state (str): puzzle state to manipulate
            moveset (str): moves to perform on puzzle state, l, r, u, or d
            size (int): size of puzzle

        Returns:
            List[str]: state after moveset has been performed
        """
        state = list(state)
        zeroIndex = state.index('0')
        for move in moveset:
            # cls.print_puzzle(state, size)
            # print()
            # print(move)
            
            match move:
                case 'l':
                    state, zeroIndex = cls.__moveLeft(state, zeroIndex, size)
                    continue
                case 'r':
                    state, zeroIndex = cls.__moveRight(state, zeroIndex, size)
                    continue
                case 'u':
                    state, zeroIndex = cls.__moveUp(state, zeroIndex, size)
                    continue
                case 'd':
                    state, zeroIndex = cls.__moveDown(state, zeroIndex, size)
                    continue
        # cls.print_puzzle(state, size)
            
        return state
    
    def print_puzzle(cls, puzzle: List[str], size: int):
        for i, tile in enumerate(puzzle):
            print(tile, end=' ')
            if (i - size + 1) % size == 0:
                print('')
                
    def print_states(self):  
        print('Init state:')
        Puzzle.print_puzzle(Puzzle, self.initState, self.size)
        print('Goal state:')
        Puzzle.print_puzzle(Puzzle, self.goalState, self.size)
