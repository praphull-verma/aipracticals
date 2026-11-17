
from collections import deque


def bfs_grid_nav(width, height, obstacles, start, goal):

    queue = deque([(start, [start])])
    visited = {start}

    directions = [(0,-1),(0,1),(-1,0),(1,0)]

    while queue:

        current_pos, path = queue.popleft()
        if current_pos == goal:
            return path

        x, y = current_pos

        for dx, dy in directions:
            next_pos = (x+dx, y+dy)
            ny, nx = next_pos

            if 0<= nx < width and 0 <= ny < height and next_pos not in obstacles and next_pos not in visited:

                visited.add(next_pos)
                queue.append((next_pos, path + [next_pos]))
    return None

width = 5
height = 5
goal = (4,4)
start = (0,0)
obstacles = ((2,3),(2,2))

path = bfs_grid_nav(width,height,obstacles, goal,start)
if path:
    print("path found with path length: ", len(path))
    print("Path: ", path[-1])
else:
    print("No path found")




