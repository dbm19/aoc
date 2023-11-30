from pathlib import Path
import sys

def parse(inputFile):
    input = Path(inputFile).read_text().splitlines()
    return input

def solve(input):
    frequency = 0
    frequencyHistory = [0]
    i = 0

    while i <= len(input):
        print(i)
        if i == len(input):
            i = 0

        if input[i][0] == "+":
            frequency += int(input[i][1:])
        else:
            frequency -= int(input[i][1:])

        print(frequency)
        for j in range (0, len(frequencyHistory)):
            if frequency == frequencyHistory[j]:
                return frequency 
        
        i += 1
        frequencyHistory.append(frequency)

if __name__ == "__main__":
    for path in sys.argv[1:]:
        input = parse(path)
        dank = solve(input)