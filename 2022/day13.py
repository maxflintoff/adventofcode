from utils import getInput
import ast


def checkMatch(left, right):

    if type(left) != type(right):
        if type(left) == int:
            left = [left]
        if type(right) == int:
            right = [right]
    if type(left) == list and type(right) == list:
        for i in range(max(len(left), len(right))):
            if i + 1 > len(left):
                return True, True
            if i + 1 > len(right):
                return False, True
            correct, force = checkMatch(left[i], right[i])
            if correct:
                return True, True
            elif force:
                return False, True

    if left < right:
        return True, True
    elif right < left:
        return False, True

    return False, False


def day13():
    input = getInput("day13").split("\n\n")

    results = []
    lowerthan2 = 0
    lowerthan6 = 0
    for pair in input:

        one, two = pair.split("\n")
        one, two = ast.literal_eval(one), ast.literal_eval(two)
        rightOrder = False

        for i in range(max(len(one), len(two))):

            if len(one) == 0 and len(two) > 0:
                rightOrder = True
            elif len(two) == 0 and len(one) > 0:
                break
            if i + 1 > len(one):
                rightOrder = True
            if i + 1 > len(two):
                break

            if not rightOrder:
                left, right = one[i], two[i]
                rightOrder, force = checkMatch(left, right)

            if rightOrder:
                results.append(input.index(pair) + 1)
                break
            if force:
                break

        for val in (one, two):
            lower, _ = checkMatch(val, [[2]])
            if lower:
                lowerthan2 += 1
            lower, _ = checkMatch(val, [[6]])
            if lower:
                lowerthan6 += 1

    print("Star 1:", sum(results))

    firstDivider = lowerthan2 + 1
    secondDivider = lowerthan6 + 2
    print("Star 2:", firstDivider * secondDivider)


if __name__ == "__main__":
    day13()
