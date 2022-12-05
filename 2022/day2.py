from pathlib import Path

def day2():
    input = open(Path(__file__).with_name('day2input'))
    vals = input.read().strip().split('\n')

    scores = []
    
    picks = { 'X': 1, 'Y': 2, 'Z': 3 }
    draw = { 'A': 'X', 'B': 'Y', 'C': 'Z' }
    win = { 'A': 'Y', 'B': 'Z', 'C': 'X' }

    for val in vals:
        opp = val[0]
        you = val[2]
        score = picks[you]
        if draw[opp] == you:
            score = score + 3
        if win[opp] == you:
            score = score + 6
        scores.append(score)

    print('Star 1: ' + str(sum(scores)))

    picks = { 'A': 1, 'B': 2, 'C': 3 }
    beats = { 'A': 'B', 'B': 'C', 'C': 'A' }
    loses = { 'A': 'C', 'B': 'A', 'C': 'B' }

    scores = []
    for val in vals:
        opp = val[0]
        result = val[2]
        if result == 'X':
            pick = loses[opp]
            score = 0
        if result == 'Y':
            pick = opp
            score = 3
        if result == 'Z':
            pick = beats[opp]
            score = 6
        score = score + picks[pick]
        scores.append(score)
        
    print('Star 2: ' + str(sum(scores)))  

if __name__ == "__main__":
    day2()