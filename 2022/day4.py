from pathlib import Path

def day4():
    input = open(Path(__file__).with_name('day4input'))
    vals = input.read().strip().split('\n')

    fullycontains = 0
    overlaps = 0
    for val in vals:
        pairs = val.split(',')
        elf0 = pairs[0].split('-')
        elf1 = pairs[1].split('-')
        assignment0 =  list(range(int(elf0[0]), int(elf0[1]) + 1))
        assignment1 =  list(range(int(elf1[0]), int(elf1[1]) + 1))
        overlap = list(set(assignment0).intersection(assignment1))
        if len(overlap) == len(assignment0) or len(overlap) == len(assignment1):
            fullycontains += 1
        if len(overlap) > 0:
            overlaps += 1
    print('Star 1: ' + str(fullycontains))
    print('Star 2: ' + str(overlaps))

if __name__ == "__main__":
    day4()