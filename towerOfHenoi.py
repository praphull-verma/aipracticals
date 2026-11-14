from collections import deque

def solve_hanoi(num_disks=3):
    start_state = (tuple(range(num_disks, 0, -1)), (), ())
    goal_state = ((), (), tuple(range(num_disks, 0, -1)))
    
    queue = deque([(start_state, [start_state])])
    visited = {start_state}
    
    while queue:
        current_state, path = queue.popleft()
        print(current_state)
        print(path)
        
        if current_state == goal_state:
            return path
            
        for next_state in get_neighbours(current_state):
            if next_state not in visited:
                visited.add(next_state)
                queue.append((next_state, path + [next_state]))
                
    return None

def get_neighbours(state):
    neighbours = []
    
    for i in range(3):
        for j in range(3):
            if i == j:
                continue
            
            peg_i = state[i]
            peg_j = state[j]
            
            if len(peg_i) > 0:
                top_disk = peg_i[-1]
                
                if len(peg_j) == 0 or peg_j[-1] > top_disk:
                    new_pegs = [list(peg) for peg in state]
                    disk = new_pegs[i].pop()
                    new_pegs[j].append(disk)
                    
                    new_state = tuple(tuple(peg) for peg in new_pegs)
                    neighbours.append(new_state)
                    
    return neighbours

if __name__ == "__main__":
    disks = 3
    print(f"Solving Tower of Hanoi with {disks} disks using State Space Search...\n")
    
    solution_path = solve_hanoi(disks)
    
    if solution_path:
        print(f"Solved in {len(solution_path) - 1} steps!\n")
        for step, board in enumerate(solution_path):
            print(f"Step {step}: Peg 0: {board[0]} | Peg 1: {board[1]} | Peg 2: {board[2]}")
    else:
        print("No solution found.")
