from puzzle import Puzzle

def main():
    myPuzzle = Puzzle("0123456789ABCDEF", "0123456789ABCDEF", 4)
    print(myPuzzle.coord_to_index(1, 3))
    myPuzzle.print_states()
    

    pass

  
    

if __name__ == '__main__':
    main()