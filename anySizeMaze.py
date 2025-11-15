import random


def generate_maze(width, height):
    """Generate a simple maze using iterative depth-first backtracker.

    Returns a 2D list where 1 indicates a visited/corridor cell and 0 is a wall.
    """
    maze = [[0] * width for _ in range(height)]
    start_cell = (random.randint(0, width - 1), random.randint(0, height - 1))
    stack = [start_cell]
    final_cell = (0,0)
    stackmax = 0
    while stack:
        x, y = stack[-1]

        # collect unvisited neighbors
        neighbors = []
        directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
        for dx, dy in directions:
            nx, ny = x + dx, y + dy
            if not (0 <= nx < width and 0 <= ny < height):
                continue
            if maze[ny][nx] != 0:
                continue
            adjacent_visited = 0
            for ddx, ddy in directions:
                ax, ay = nx + ddx, ny + ddy
                if 0 <= ax < width and 0 <= ay < height:
                    if maze[ay][ax] == 1 or (ax, ay) == start_cell:
                        adjacent_visited += 1
            if adjacent_visited <= 1:
                neighbors.append((nx, ny))
        if neighbors:
            next_cell = random.choice(neighbors)
            print(next_cell)
            stack.append(next_cell)
            maze[next_cell[1]][next_cell[0]] = 1
        else:
            if len(stack) > stackmax:
                stackmax = len(stack)
                final_cell = stack.pop()
            else:
                stack.pop()

    return maze, start_cell, final_cell


if __name__ == "__main__":
    maze, start, end = generate_maze(20, 20)
    print(maze)
    print(start)
    print(end)
    maze[end[1]][end[0]] = 2  # mark the end point
    maze[start[1]][start[0]] = 3  # mark the start point
        
    for row in maze:
        print("".join(["# " if cell == 0 else ". " if cell == 1 else "S " if cell == 3 else "E " for cell in row]))