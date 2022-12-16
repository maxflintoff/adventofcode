from utils import getInput


def day14():
    input = getInput("day14").split("\n")
    input = [i.split("->") for i in input]
    xs = set()
    ys = set()
    for i in range(len(input)):
        for c in range(len(input[i])):
            res = tuple(map(int, input[i][c].split(",")))
            input[i][c] = res
            xs.add(res[0])
            ys.add(res[1])
    xstart, xend = min(xs), max(xs)
    yend = max(ys)
    grid = []
    for i in range(0, yend + 1):
        grid.append(["." for _ in range((xend - xstart) + 1)])
    mapping = dict()
    for i in range((xend - xstart) + 1):
        mapping[xstart + i] = i

    for line in input:
        for i in range(len(line)):
            if i + 1 >= len(line):
                break
            startx, starty = line[i]
            endx, endy = line[i + 1]
            grid[starty][mapping[startx]] = "#"
            diffx, diffy = endx - startx, endy - starty
            for i in range(0, abs(diffx)):
                if diffx > 0:
                    it = 1
                else:
                    it = -1
                    i = -i
                grid[starty][mapping[startx + i + it]] = "#"
            for i in range(0, abs(diffy)):
                if diffy > 0:
                    it = 1
                else:
                    it = -1
                    i = -i
                grid[starty + i + it][mapping[startx]] = "#"

    def moveSand(sand: tuple, grid: list, part1: bool = True):
        moves = [
            (sand[0], sand[1] + 1),
            (sand[0] - 1, sand[1] + 1),
            (sand[0] + 1, sand[1] + 1),
        ]

        for move in moves:
            if part1:
                if (move[0] not in mapping.keys()) or (
                    move[1] not in range(0, len(grid))
                ):
                    return sand, True
            dest = grid[move[1]][mapping[move[0]]]
            if dest == ".":
                sand = move
                break

        return sand, False

    abyss = False
    count = 0
    sandStart = (500, 0)

    while not abyss:
        sand = sandStart
        while True:
            update, abyss = moveSand(sand, grid)
            if abyss:
                part1 = count
            if update == sand:
                grid[update[1]][mapping[update[0]]] = "o"
                break
            sand = update
        count += 1

    print("Star 1:", part1)

    grid.append(["." for _ in range((xend - xstart) + 1)])
    grid.append(["#" for _ in range((xend - xstart) + 1)])

    blocked = False
    while not blocked:
        sand = sandStart
        stopped = False
        while not stopped:

            update, _ = moveSand(sand, grid, False)

            if update[0] + 1 not in mapping.keys():
                for i in range(len(grid)):
                    if i + 1 == len(grid):
                        grid[i].append("#")
                    else:
                        grid[i].append(".")
                mapping[update[0] + 1] = len(grid[0]) - 1

            if update[0] - 1 not in mapping.keys():
                for i in range(len(grid)):
                    if i + 1 == len(grid):
                        grid[i].insert(0, "#")
                    else:
                        grid[i].insert(0, ".")
                for i in mapping:
                    mapping[i] += 1
                mapping[update[0] - 1] = 0

            if update == sand:
                grid[update[1]][mapping[update[0]]] = "o"
                stopped = True
            sand = update

            if grid[0][mapping[500]] == "o":
                blocked = True
                stopped = True

        count += 1

    print("Star 2:", count)


if __name__ == "__main__":
    day14()
