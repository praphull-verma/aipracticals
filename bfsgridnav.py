
from collections import deque


def bfsgridnav(width, height, obstacles, start, goal):
    
    queue = deque([(start, [start])])
    visited = {start}

    directions = [(0, -1), (0, 1), (-1, 0), (1, 0)]
    step = 0
    while queue:
        step += 1
        print("Step count: ",step)
#        print(f"Queue: {list(queue)}")

        current_pos, path = queue.popleft()

        if current_pos == goal:
            return path
        x,y = current_pos

        for dx, dy in directions:
            next_pos = (x+dx, y+dy)
            nx, ny = next_pos

            if 0 <= nx < width and 0 <= ny < height and next_pos not in obstacles and next_pos not in visited:
                visited.add(next_pos)
                queue.append((next_pos, path + [next_pos]))
    return None

if __name__ == "__main__":
    width, height = 5,5
    obstacles = {(1, 1), (1, 2), (3, 1), (3, 2), (3, 3)}
    start = (0,0)
    goal = (4,4)

    print(f"Finding shortest path from {start} to {goal}...")
    path = bfsgridnav(width,height,obstacles,start,goal)

    if path:
        print(f"Success! Shortest path found ({len(path)} steps")
        print(path)
    else:
        print("No path found")

