from utils import getInput

directions = {"U": (0, 1), "D": (0, -1), "L": (-1, 0), "R": (1, 0)}


def calcMove(a, b):
    if a > b:
        return 1
    elif a < b:
        return -1
    else:
        return 0


def Move(HEAD: tuple, TAIL: tuple):
    diff = (abs(HEAD[0] - TAIL[0]), abs(HEAD[1] - TAIL[1]))
    if diff[0] + diff[1] > 2:
        TAIL = (
            TAIL[0] + calcMove(HEAD[0], TAIL[0]),
            TAIL[1] + calcMove(HEAD[1], TAIL[1]),
        )
    elif diff[0] >= 2 or diff[1] >= 2:
        TAIL = (
            TAIL[0] + calcMove(HEAD[0], TAIL[0]),
            TAIL[1] + calcMove(HEAD[1], TAIL[1]),
        )
    return TAIL


def day9():

    input = getInput("day9").split("\n")
    # '0,0' is the starting x,y
    HEAD = (0, 0)
    TAIL = (0, 0)
    POSITIONS = {TAIL}
    LONG = []
    for _ in range(10):
        LONG.append((0, 0))
    LONGPOSITIONS = {LONG[-1]}

    for line in input:
        direction, moves = line.split()

        move = directions[direction]

        for _ in range(int(moves)):
            HEAD = (HEAD[0] + move[0], HEAD[1] + move[1])
            TAIL = Move(HEAD, TAIL)
            POSITIONS.add(TAIL)

            LONG[0] = (LONG[0][0] + move[0], LONG[0][1] + move[1])
            for i in range(1, len(LONG)):
                LONG[i] = Move(LONG[i - 1], LONG[i])
            LONGPOSITIONS.add(LONG[-1])

    print("Star 1:", len(POSITIONS))
    print("Star 2:", len(LONGPOSITIONS))


if __name__ == "__main__":
    day9()
