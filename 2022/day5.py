from pathlib import Path
from collections import defaultdict

def day5():
    input = open(Path(__file__).with_name('day5input'))
    split = input.read().split('\n\n')
    crates = split[0]
    instructions = split[1]
    crates = crates.split('\n')
    crates.reverse()
    crates.pop(0)
    stacks = []
    for crateLine in crates:
        crateLine += ''
        crateList = [list(crateLine)[x:x+3] for x in range(0, len(crateLine), 4)]
        stacks.append(dict(enumerate(crateList)))
    stackProcessor = defaultdict(list)
    stackProcessorStar2 = defaultdict(list)
    for stackIndex in range(len(stacks)):
        d = stacks[stackIndex]
        for k, v in d.items():
            k = k + 1
            v = v[1]
            if v != ' ':
                stackProcessor[k].append(v)
                stackProcessorStar2[k].append(v)
            
    instructions = instructions.split('\n')
    for instruction in instructions:
        inst = instruction.replace("move ", '').replace("from ", '').replace('to ', '').split(' ')
        qty = int(inst[0])
        fromStack = int(inst[1])
        toStack = int(inst[2])
        # print('Now moving to stack ' + str(toStack) + ' from stack ' + str(fromStack) + '. Quantity: ' + str(qty))
        
        # Star 1
        stack = stackProcessor[fromStack]
        targetStack = stackProcessor[toStack]
        move = stack[len(stack) - qty:]
        move.reverse()
        for item in move:
            targetStack.append(item)
        stackProcessor[toStack] = targetStack
        del stackProcessor[fromStack][len(stack) - qty:]
        # Star 2
        stack = stackProcessorStar2[fromStack]
        targetStack = stackProcessorStar2[toStack]
        move = stack[len(stack) - qty:]
        for item in move:
            targetStack.append(item)
        stackProcessorStar2[toStack] = targetStack
        del stackProcessorStar2[fromStack][len(stack) - qty:]

    star1 = ''
    for stack in stackProcessor:
        top = stackProcessor[stack][len(stackProcessor[stack]) - 1 :]
        star1 += top[0]
    print('Star 1: ' + star1)

    star2 = ''
    for stack in stackProcessorStar2:
        top = stackProcessorStar2[stack][len(stackProcessorStar2[stack]) - 1 :]
        star2 += top[0]
    print('Star 2: ' + star2)

if __name__ == "__main__":
    day5()