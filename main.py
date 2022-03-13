def main():
    
    print_puzzle("0123456789ABCDEF", 4)

    pass

def print_puzzle(puzzle: str, size: int):
    for i, tile in enumerate(puzzle):
        print(tile, end=' ')
        if (i - size + 1) % size == 0:
            print('')    
    

if __name__ == '__main__':
    main()