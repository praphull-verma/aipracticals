
import heapq 

GOAL_STATE = (

        1,2,3,
        4,5,6,
        7,8,0

        )

def manhattan(state):
    distance = 0
    for i, val in enumerate(state):
        if val!=0:

            target_index = GOAL_STATE.index(val)

            curr_row, curr_col = i // 3, i % 3

            target_row, target_col = target_index // 3, target_index % 3

            distance += (abs(target_row - curr_row) + abs(target_col - curr_col))

    return distance

def get_neighbour(state):
    neighbour = []
    zero_index = state.index(0)
    row, col = zero_index // 3, zero_index % 3

    moves = [(-1,0,"Up"),(1,0,"Down"),(0,-1,"Left"),(0,1,"Right")]

    for dr, dc, directions in moves:

        new_row, new_col = row + dr, col + dc

        if 0 <= new_row < 3 and 0 <= new_col < 3:

            new_zero_index = new_row * 3 + new_col

            state_list = list(state)

            state_list[zero_index], state_list[new_zero_index] = state_list[new_zero_index], state_list[zero_index]

            neighbour.append(tuple(state_list),directions))
    return neighbour

def a_star(start):

    pq = [(manhattan(start), 0 , start , [start])]

    visited = set()

    while pq:

        f, g, state, path = heapq.heappop(pq)

        if state == GOAL_STATE:
            return state

        if state in visited:
            continue

        visited.add(state)

        for nxt, directions in get_neighbour(state):

            if nxt not in visited:

                g_new = g + 1
                f_new = g_new + manhattan(nxt)
                heapq.heappush(pq, (f_new, g_new, nxt, path + [nxt]))


    return None


def print_board(state):
    for i in range(0,9,3):
        print(state[i:i+3])
    print("-" * 9)

if __name__ == "__main__":
    start_state = (1,2,3,
                   4,0,5,
                   6,7,8)
    print("Starting 8-puzzle board: ")
    print_board(start_state)

    path = a_star_puzzle(start_state)
    if path:
        print(f"Solved in {len(path)-1} steps!\n")
        for i, board in enumerate(path):
            print(f"step {i}: ")
            print_board(board)
    else:
        print("No solution found")








