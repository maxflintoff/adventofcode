from pathlib import Path
from collections import defaultdict
import re
from copy import deepcopy

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
        crateList = [list(crateLine)[x:x+3] for x in range(0, len(crateLine), 4)]
        stacks.append(dict(enumerate(crateList)))
    stackProcessor = defaultdict(list)
    for stackIndex in range(len(stacks)):
        d = stacks[stackIndex]
        for k, v in d.items():
            k = k + 1
            v = v[1]
            if v != ' ':
                stackProcessor[k].append(v)
    stackProcessorStar2 = deepcopy(stackProcessor)
            
    instructions = instructions.split('\n')
    for instruction in instructions:
        inst = re.findall(r'\b\d+\b', instruction)
        qty = int(inst[0])
        fromStack = int(inst[1])
        toStack = int(inst[2])
        
        # Star 1
        stack = stackProcessor[fromStack]
        targetStack = stackProcessor[toStack]
        for _ in range(qty):
            val = stackProcessor[fromStack].pop()
            stackProcessor[toStack].append(val)

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
        star1 += stackProcessor[stack][-1]
    print('Star 1: ' + star1)

    star2 = ''
    for stack in stackProcessorStar2:
        star2 += stackProcessorStar2[stack][-1]
    print('Star 2: ' + star2)

if __name__ == "__main__":
    day5()