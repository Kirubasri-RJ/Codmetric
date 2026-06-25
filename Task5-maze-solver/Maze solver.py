from collections import deque


def bfs(maze, start, end):
    rows, cols = len(maze), len(maze[0])

    # 4 possible moves: up, down, left, right
    moves = [(-1, 0), (1, 0), (0, -1), (0, 1)]

    queue = deque([start])
    visited = {start}
    parent = {start: None}

    while queue:
        current = queue.popleft()

        if current == end:
            break  # reached the end, stop searching

        for dr, dc in moves:
            r, c = current[0] + dr, current[1] + dc
            neighbor = (r, c)

            # Check bounds
            if not (0 <= r < rows and 0 <= c < cols):
                continue
            # Check wall
            if maze[r][c] == 1:
                continue
            # Check visited
            if neighbor in visited:
                continue

            visited.add(neighbor)
            parent[neighbor] = current
            queue.append(neighbor)

    # If end was never reached, no path exists
    if end not in parent:
        return None

    # Reconstruct path by walking backward from end to start
    path = []
    node = end
    while node is not None:
        path.append(node)
        node = parent[node]
    path.reverse()

    return path


def print_maze(maze, path, start, end):
    path_set = set(path) if path else set()
    display = []

    for r, row in enumerate(maze):
        line = ""
        for c, cell in enumerate(row):
            pos = (r, c)
            if pos == start:
                line += "S "
            elif pos == end:
                line += "E "
            elif pos in path_set:
                line += "* "
            elif cell == 1:
                line += "# "
            else:
                line += ". "
        display.append(line)

    print("\n".join(display))


def solve_and_display(maze, start, end, label=""):
    """Runs BFS on a maze and prints the result."""
    print(f"\n--- {label} ---")
    path = bfs(maze, start, end)

    if path is None:
        print("No path found from start to end.")
    else:
        print(f"Shortest path length: {len(path) - 1} steps")
        print(f"Path: {path}\n")
        print_maze(maze, path, start, end)


if __name__ == "__main__":
    # ---------- Test Case 1: Simple solvable maze ----------
    maze1 = [
        [0, 0, 1, 0, 0],
        [1, 0, 1, 0, 1],
        [0, 0, 0, 0, 0],
        [0, 1, 1, 1, 0],
        [0, 0, 0, 0, 0],
    ]
    start1, end1 = (0, 0), (4, 4)
    solve_and_display(maze1, start1, end1, "Test 1: Solvable Maze")

    # ---------- Test Case 2: Larger maze ----------
    maze2 = [
        [0, 1, 0, 0, 0, 0],
        [0, 1, 0, 1, 1, 0],
        [0, 0, 0, 0, 1, 0],
        [1, 1, 1, 0, 1, 0],
        [0, 0, 0, 0, 0, 0],
        [0, 1, 1, 1, 1, 0],
    ]
    start2, end2 = (0, 0), (5, 5)
    solve_and_display(maze2, start2, end2, "Test 2: Larger Maze")

    # ---------- Test Case 3: No possible path ----------
    maze3 = [
        [0, 1, 0],
        [1, 1, 0],
        [0, 1, 0],
    ]
    start3, end3 = (0, 0), (2, 0)
    solve_and_display(maze3, start3, end3, "Test 3: No Path Exists")