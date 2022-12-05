from pathlib import Path

def day1():
    input = open(Path(__file__).with_name('day1input'))
    vals = input.read().strip().split('\n\n')

    totals = []
    for val in vals:
        parsed = val.split('\n')
        total = sum(map(int, parsed))
        totals.append(total)

    print('Star 1: ' + str(max(totals)))

    top3 = sorted(totals, reverse=True)[:3]
    print('Star 2: ' + str(sum(top3)))

if __name__ == "__main__":
    day1()