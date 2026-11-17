
def dfs(state, goal, visited):

    if state == goal:
        print("Goal Reached:", state)
        return True

    visited.append(state)

    for i in range(len(state)):
        new_state = list(state)
        block = new_state.pop(i)

        new_state.append(block)
        new_state = tuple(new_state)

        if new_state not in visited:
            print(new_state)
            if dfs(new_state, goal, visited):
                return True

    return False


start = ('B', 'C', 'D', 'A')
goal = ('A', 'B', 'C', 'D')

dfs(start, goal, [])


