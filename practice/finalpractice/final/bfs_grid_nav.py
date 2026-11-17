
from collections import deque

def bfs_grid_nav(width, height, obstacles, start, goal):

    queue = deque([(start, [start])])

    visited = {start}

    directions = [(0,-1),(0,1),(-1,0),(1,0)]

    while queue:

        current_pos, path = queue.popleft()
        if current_pos == goal:
            return path
        
        x,y = current_pos

        for dx, dy in directions:
            next_position = (x + dx, y + dy)
            nx, ny = next_position

            if 0<=nx<width and 0<=ny<height and next_position not in obstacles and next_position not in visited:
                
                visited.add(next_position)
                queue.append((next_position, path + [next_position]))

    return None

width = 5
height = 5
start = (0,0)
goal = (4,4)
obstacles = ((1,3),(3,3),(2,0))

path = bfs_grid_nav(width, height,obstacles, start, goal)

if path:
    print("Navigation done using path ", path)
    print("Number of steps", len(path))
else:
    print("Path not found")





        
