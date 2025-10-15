from collections import deque

# Maze grid
maze = [
    ['S', '.', '.', '#'],
    ['.', '#', '.', '.'],
    ['.', '.', '.', 'G']
]

rows, cols = len(maze), len(maze[0])

# Directions: up, down, left, right
dirs = [(-1,0), (1,0), (0,-1), (0,1)]

def bfs(maze, start, goal):
    queue = deque([start])
    visited = set([start])
    parent = {start: None}

    while queue:
        r, c = queue.popleft()
        if (r, c) == goal:
            break
        for dr, dc in dirs:
            nr, nc = r + dr, c + dc
            if 0 <= nr < rows and 0 <= nc < cols and maze[nr][nc] != '#' and (nr, nc) not in visited:
                queue.append((nr, nc))
                visited.add((nr, nc))
                parent[(nr, nc)] = (r, c)
    
    # Reconstruct path
    path = []
    node = goal
    while node:
        path.append(node)
        node = parent.get(node)
    path.reverse()
    return path

start = (0,0)
goal = (2,3)
path = bfs(maze, start, goal)

print("Shortest Path:", path)
