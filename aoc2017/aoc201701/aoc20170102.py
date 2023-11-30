from pathlib import Path
import sys

def parse(inputFile):
    puzzleInput =  Path(inputFile).read_text()
    return puzzleInput

def solve(puzzleInput):
    sum = 0
    checkLength = len(puzzleInput) // 2

    for i in range(0, len(puzzleInput)):
        if len(puzzleInput) - i <= checkLength:
            if puzzleInput[i] == puzzleInput[checkLength - (len(puzzleInput) - i)]:
                sum += int(puzzleInput[i])
        elif puzzleInput[i] == puzzleInput[i + checkLength]:
            sum += int(puzzleInput[i])
    return sum

if __name__ == "__main__":
    for path in sys.argv[1:]:
        puzzleInput = parse(path)
        print(solve(puzzleInput))