import string
from pathlib import Path


def day3():
    input = open(Path(__file__).with_name("day3input"))
    vals = input.read().strip().split("\n")
    alphabet = list(string.ascii_letters)

    star1 = []
    for val in vals:
        half = round(len(val) / 2)
        common = list(set(val[:half]).intersection(val[half:]))
        priority = alphabet.index(common[0]) + 1
        star1.append(priority)
    print("Star 1: " + str(sum(star1)))

    star2 = []
    for i in range(0, len(vals), 3):
        group = vals[i : i + 3]
        pack0 = list(group[0])
        pack1 = list(group[1])
        pack2 = list(group[2])
        common = list(set(pack0).intersection(pack1).intersection(pack2))
        priority = alphabet.index(common[0]) + 1
        star2.append(priority)
    print("Star 2: " + str(sum(star2)))


if __name__ == "__main__":
    day3()
