from pathlib import Path
import sys

def parse(inputFile):
    puzzleInput =  Path(inputFile).read_text()
    return puzzleInput

def solve(puzzleInput):
    sum = 0

    for i in range(0, len(puzzleInput)):
        if i == len(puzzleInput) - 1:
            if puzzleInput[i] == puzzleInput[0]:
                sum += int(puzzleInput[i])
            return sum
        if puzzleInput[i] == puzzleInput[i + 1]:
            sum += int(puzzleInput[i])

    return sum

if __name__ == "__main__":
    for path in sys.argv[1:]:
        puzzleInput = parse(path)
        print(solve(puzzleInput))