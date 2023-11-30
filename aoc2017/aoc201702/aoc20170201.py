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
        puzzleInput[i].sort()
        difference = puzzleInput[i][-1] - puzzleInput[i][0]
        checksum += difference

    print(checksum)    

if __name__ == "__main__":
    for path in sys.argv[1:]:
        puzzleInput = parse(path)
        solve(puzzleInput)