from typing import Tuple, List


class Puzzle:
    def swap_tiles(cls, state: List[str], pos0: int, pos1: int) -> List[int]:
        """swaps two tiles in a puzzle

        Args:
            state (List[str]): given puzzle state
            pos0 (int): pos of tile0 to swap
            pos1 (int): pos of tile1 to swap

        Returns:
            List[int]: resultant puzzle state from swapping of tiles at pos0 and pos1
        """
        temp = state[pos0]
        state[pos0] = state[pos1]
        state[pos1] = temp
        return state

    def moveLeft(cls, state: List[str], zeroIndex: int, size: int) -> Tuple[List[str], int]:
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
            return (state, zeroIndex)
        # make move
        state = cls.swap_tiles(state, zeroIndex, zeroIndex - 1)
        zeroIndex -= 1
        return (state, zeroIndex)

    def moveRight(cls, state: List[str], zeroIndex: int, size: int) -> Tuple[List[str], int]:
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
            return (state, zeroIndex)
        # make move
        state = cls.swap_tiles(state, zeroIndex, zeroIndex + 1)
        zeroIndex += 1
        return (state, zeroIndex)

    def moveUp(cls, state: List[str], zeroIndex: int, size: int) -> Tuple[List[str], int]:
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
            return (state, zeroIndex)
        # make move
        state = cls.swap_tiles(state, zeroIndex, zeroIndex - size)
        zeroIndex -= size
        return (state, zeroIndex)

    def moveDown(cls, state: List[str], zeroIndex: int, size: int) -> Tuple[List[str], int]:
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
            return (state, zeroIndex)
        # make move
        state = cls.swap_tiles(state, zeroIndex, zeroIndex + size)
        zeroIndex += size
        return (state, zeroIndex)

    def move(cls, state: str, moveset: str, size: int, zeroIndex: int = -1) -> Tuple[List[str], int]:
        """given a puzzle state, performs moves left, right, up, or down from
        moveset on puzzle and puzzle state after performed moves

        Args:
            state (str): puzzle state to manipulate
            moveset (str): moves to perform on puzzle state, l, r, u, or d
            size (int): size of puzzle
            zeroIndex (int): index of zero tile, automatically found if not given

        Returns:
            Tuple[List[str], int]: state after moveset has been performed, index of zero tile
        """
        state = list(state)
        if zeroIndex < 0:
            zeroIndex = state.index('0')
        for move in moveset:
            # cls.print_puzzle(state, size)
            # print()
            # print(move)

            match move:
                case 'l':
                    state, zeroIndex = cls.moveLeft(state, zeroIndex, size)
                    continue
                case 'r':
                    state, zeroIndex = cls.moveRight(state, zeroIndex, size)
                    continue
                case 'u':
                    state, zeroIndex = cls.moveUp(state, zeroIndex, size)
                    continue
                case 'd':
                    state, zeroIndex = cls.moveDown(state, zeroIndex, size)
                    continue
        # cls.print_puzzle(state, size)

        return (state, zeroIndex)

    def print_puzzle(cls, puzzle: List[str], size: int):
        for i, tile in enumerate(puzzle):
            print(tile, end=' ')
            if (i - size + 1) % size == 0:
                print('')
