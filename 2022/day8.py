from utils import getInput


def day8():

    input = getInput("day8")
    lines = input.split()
    visibleTotal = 0
    scenicScores = []

    for row in range(len(lines)):
        line = lines[row]
        if row == 0 or row == len(lines) - 1:
            visibleTotal += len(line)
        else:
            for tree in range(len(line)):
                if tree == 0 or tree == len(line) - 1:
                    visibleTotal += 1
                else:
                    left, right = tree - 1, tree + 1

                    visibleLeft = visibleRight = True
                    viewLeft = viewRight = 0

                    def calculate_properties(
                        check: int, test: int, tree: int, distance: int
                    ):
                        visible = True
                        view = 0
                        if test == 0:
                            while check >= test:
                                if lines[check][tree] >= line[tree]:
                                    visible = False
                                    if view == 0:
                                        view = distance - check
                                if check == 0 and view == 0:
                                    view = row - check
                                check -= 1
                        else:
                            while check <= test:
                                if lines[check][tree] >= line[tree]:
                                    visible = False
                                    if view == 0:
                                        view = check - distance
                                if check == 0 and view == 0:
                                    view = check - distance
                                check += 1

                        return visible, view

                    visibleAbove, viewAbove = calculate_properties(
                        row - 1, 0, tree, row
                    )
                    visibleBelow, viewBelow = calculate_properties(
                        row + 1, len(lines) - 1, tree, row
                    )

                    while left >= 0:
                        if line[left] >= line[tree]:
                            visibleLeft = False
                            if viewLeft == 0:
                                viewLeft = tree - left
                        if left == 0 and viewLeft == 0:
                            viewLeft = tree - left
                        left -= 1
                    while right <= len(line) - 1:
                        if line[right] >= line[tree]:
                            visibleRight = False
                            if viewRight == 0:
                                viewRight = right - tree
                        if right == len(line) - 1 and viewRight == 0:
                            viewRight = right - tree
                        right += 1
                    if visibleRight or visibleLeft or visibleAbove or visibleBelow:
                        visibleTotal += 1

                    scenicScores.append(viewAbove * viewLeft * viewRight * viewBelow)

    print("Star 1:", visibleTotal)
    print("Star 2:", max(scenicScores))


if __name__ == "__main__":
    day8()
