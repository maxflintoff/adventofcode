from utils import getInput


def day10():
    instructions = getInput("day10").split("\n")

    registerX = 1
    cycles = 0
    displayCycle = 0
    signals = []
    display = ""
    spritePos = [0, 1, 2]
    value = 0
    for instruction in instructions:
        if instruction == "noop":
            cycle = 1
        else:
            cycle = 2
            value = int(instruction.split()[1])
        for i in range(cycle):
            cycles += 1
            if cycles == 20 or (cycles % 40) - 20 == 0:
                signals.append(cycles * registerX)
            if i == 1:
                registerX += value

            # Star 2
            if displayCycle in spritePos:
                display += "#"
            else:
                display += "."

            displayCycle += 1

            if cycles % 40 == 0:
                display += "\n"
                displayCycle = 0
            spritePos = [registerX - 1, registerX, registerX + 1]

    print("Star 1:", sum(signals))
    print("Star2:")
    print(display)


if __name__ == "__main__":
    day10()
