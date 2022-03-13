def main():
    
    print_puzzle("0123456789ABCDEF", 4)

    pass

def print_puzzle(puzzle: str, size: int):
    for i in range(len(puzzle)):
        print(puzzle[i], end=' ')
        if (i - size + 1) % size == 0:
            print('')    
    

if __name__ == '__main__':
    main()