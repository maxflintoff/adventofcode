from pathlib import Path
from collections import Counter

def day6():
    input = open(Path(__file__).with_name('day6input'))
    datastream = input.read()

    # Star 1
    for index in range(len(datastream)):
        substring = datastream[index:index + 4]
        freq = Counter(substring)
        repeats = False
        for char in substring:
            if freq[char] > 1:
                repeats = True
                break
        if not repeats:
            packetMarker = index + 4
            break
    print('Star 1: ' + str(packetMarker))

    # Star 2
    for index in range(len(datastream)):
        substring = datastream[index:index + 14]
        freq = Counter(substring)
        repeats = 0
        for char in substring:
            if freq[char] > 1:
                repeats = True
                break
        if not repeats:
            messageMarker = index + 14
            break
    print('Star 2: ' + str(messageMarker))

if __name__ == "__main__":
    day6()