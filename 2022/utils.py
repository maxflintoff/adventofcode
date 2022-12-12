from pathlib import Path
import re
import operator

def getInput(day: str):
    input = open(Path(__file__).with_name(day + 'input'))
    return input.read()


def GetFirstNumberFromString(string):
    return int(re.findall(r'\b\d+\b', string)[0])

def GetNumbersFromString(string):
    vals = re.findall(r'\b\d+\b', string)
    return [int(i) for i in vals]

def GetOperation(operatorText):
    if operatorText == '*':
        return operator.mul
    if operatorText == '+':
        return operator.add
    if operatorText == '-':
        return operator.sub
    if operatorText == '/':
        return operator.truediv

def returnStrorInt(test: str):
    try:
        int(test)
        return int(test)
    except ValueError:
        return test