from pathlib import Path
import sys

def parse(inputFile):
    input = Path(inputFile).read_text().splitlines()
    finalInput = []

    for i in range(0, len(input)):
        inputSubArray = input[i].split("\t")
        for j in range(0, len(inputSubArray)):
            inputSubArray[j] = int(inputSubArray[j])
        finalInput.append(inputSubArray)

    return finalInput

def solve(input):
    checksum = 0

    for i in range(0, len(input)):
        input[i].sort()
        for j in reversed(range(len(input[i]))):
            for k in range(0, j - 1):
                if puzzleInput[i][j] % puzzleInput[i][k] == 0:
                    quotient = puzzleInput[i][j] // puzzleInput[i][k]
                    checksum += quotient

    print(checksum)    

if __name__ == "__main__":
    for path in sys.argv[1:]:
        puzzleInput = parse(path)
        solve(puzzleInput)