class Puzzle:
    def __init__(self, initState: str, goalState: str):
        self.initState = list(initState)
        self.goalState = list(goalState)
        
    def index_to_coord(index: int, size: int):
        return (index/size, index%size)
    
    def print_states(self):
        print('Init state:', ''.join(self.initState))
        print('Goal state:', ''.join(self.goalState))