 
from collections import deque

def navigation(width, height, obstacles, start, goal):

    queue = deque([(start, [start])])
    

    visited = {start}

    directions = [(0,-1),(0,1),(-1,0),(1,0)]

    while queue:

        current_position, path = queue.popleft()

        if current_position == goal:
            return path

        x,y = current_position

        for dx, dy in directions:
            next_pos = (x + dx, y + dy)
            nx, ny = next_pos

            if 0<= nx <width and 0 <= ny < height and next_pos not in visited and next_pos not in obstacles:
                visited.add(next_pos)
                queue.append((next_pos, path + [next_pos]))

    return None


if __name__ == "__main__":

    width, height = 5,5
    obstacles = {(1, 1), (1, 2), (3, 1), (3, 2), (3, 3)}
    start = (0,0)
    goal = (4,4)

    print(f"Finding shortest path from {start} to {goal}...")
    path = navigation(width,height,obstacles,start,goal)

    if path:
        print(f"Success! Shortest path found ({len(path)} steps")
        print(path)
    else:
        print("No path found")






