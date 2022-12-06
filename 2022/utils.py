from pathlib import Path

def getInput(day: str):
    input = open(Path(__file__).with_name(day +'input'))
    return input.read()