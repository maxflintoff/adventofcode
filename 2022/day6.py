import sys
sys.path.append('../.')
from utils import getInput

def findFirstUnique(datastream: str, marker: int):
    for index in range(len(datastream)):
        substring = datastream[index:index + marker]
        if len(substring) == len(set(substring)):
            return str(index + marker)

def day6():

    datastream = getInput('day6')
    print('Star 1: ' + findFirstUnique(datastream, 4))
    print('Star 2: ' + findFirstUnique(datastream, 14))

if __name__ == "__main__":
    day6()