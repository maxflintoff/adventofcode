from utils import (
    getInput,
    GetNumbersFromString,
    GetOperation,
    GetFirstNumberFromString,
    returnStrorInt,
)
from math import lcm
import operator
import copy


class Monkey:
    def __init__(
        self,
        items: list,
        operation,
        operationValue,
        test: int,
        trueTarget: int,
        falseTarget: int,
    ):
        self.items = items
        self.operation = operation
        self.operationValue = operationValue
        self.test = test
        self.trueTarget = trueTarget
        self.falseTarget = falseTarget
        self.inspections = 0

    def print(self):
        print(
            self.items,
            self.operation,
            self.operationValue,
            self.test,
            self.trueTarget,
            self.falseTarget,
            self.inspections,
        )


def getMonkeys():
    input = getInput("day11").split("\n\n")
    MONKEYS = []
    for monkey in input:
        lines = monkey.split("\n")
        operation = lines[2].replace("Operation:", "").strip().split()
        MONKEY = Monkey(
            items=GetNumbersFromString(lines[1]),
            operation=GetOperation(operation[3]),
            operationValue=returnStrorInt(operation[4]),
            test=GetFirstNumberFromString(lines[3]),
            trueTarget=GetFirstNumberFromString(lines[4]),
            falseTarget=GetFirstNumberFromString(lines[5]),
        )
        MONKEYS.append(MONKEY)

    return MONKEYS


def play(ROUNDS: int, MONKEYS: list, STAR: int, LCM: int = 0):
    for _ in range(ROUNDS):
        for MONKEY in MONKEYS:
            while MONKEY.items:
                MONKEY.inspections += 1
                item = MONKEY.items.pop(0)
                if MONKEY.operationValue == "old":
                    item = MONKEY.operation(item, item)
                else:
                    item = MONKEY.operation(item, MONKEY.operationValue)
                if STAR == 1:
                    item //= 3
                else:
                    item %= LCM
                if item % MONKEY.test == 0:
                    MONKEYS[MONKEY.trueTarget].items.append(item)
                else:
                    MONKEYS[MONKEY.falseTarget].items.append(item)
    inspections = sorted([m.inspections for m in MONKEYS], reverse=True)
    return operator.mul(inspections[0], inspections[1])


def day11():
    MONKEYS = getMonkeys()
    MONKEY_BUSINESS = play(ROUNDS=20, MONKEYS=copy.deepcopy(MONKEYS), STAR=1)

    print("Star 1:", MONKEY_BUSINESS)

    LCM = lcm(*[m.test for m in MONKEYS])
    MONKEY_BUSINESS = play(ROUNDS=10000, MONKEYS=MONKEYS, STAR=2, LCM=LCM)

    print("Star 2:", MONKEY_BUSINESS)


if __name__ == "__main__":
    day11()
