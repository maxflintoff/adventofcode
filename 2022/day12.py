from utils import getInput
import string
from functools import reduce
import collections


def getLocation(search: int, list: list):
    for sublist in list:
        for i in range(len(sublist)):
            if sublist[i] == search:
                return (i, list.index(sublist))


def getNextPos(coordinates: list):
    return (
        [coordinates[0], coordinates[1] - 1],
        [coordinates[0], coordinates[1] + 1],
        [coordinates[0] - 1, coordinates[1]],
        [coordinates[0] + 1, coordinates[1]],
    )


def compvecs(a, b):
    return reduce(lambda b1, b2: b1 and b2, map(lambda e1, e2: e1 == e2, a, b), True)


def bfs(grid: list[list], start: tuple, end: tuple):
    queue = collections.deque(((start, 0),))
    seen = {}
    shortest = float("inf")
    while queue:
        loc, moves = queue.popleft()
        x, y = loc
        seen[(x, y)] = moves
        next_move = moves + 1
        if (x, y) == end:
            shortest = min(shortest, moves)
        for nx, ny in ((x + 1, y), (x - 1, y), (x, y + 1), (x, y - 1)):
            if 0 <= ny < len(grid) and 0 <= nx < len(grid[0]):
                if grid[ny][nx] <= grid[y][x] + 1:
                    if (nx, ny) not in seen or seen[(nx, ny)] > next_move:
                        seen[(nx, ny)] = next_move
                        queue.append(((nx, ny), next_move))
    return shortest


def day12():
    input = getInput("day12")

    grid = []
    alphabet = list(string.ascii_letters)

    for line in input.split():
        row = []
        for i in list(line):
            row.append(alphabet.index(i))
        grid.append(row)

    start = getLocation(alphabet.index("S"), grid)
    grid[start[1]][start[0]] = 0
    end = getLocation(alphabet.index("E"), grid)
    grid[end[1]][end[0]] = 25

    shortest_path = bfs(grid, start, end)
    print("Star 1:", shortest_path)

    starts = []
    for y in range(len(grid)):
        for x in range(len(grid[y])):
            if grid[y][x] == 0:
                starts.append((x, y))

    shortest_paths = []
    for start in starts:
        result = bfs(grid, start, end)
        shortest_paths.append(result)

    print("Star 2:", min(shortest_paths))
    return None


if __name__ == "__main__":
    day12()
