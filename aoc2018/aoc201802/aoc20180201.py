from pathlib import Path
import sys

def parse(inputFile):
    input = Path(inputFile).read_text().splitlines()
    return input

def solve(input):
    twoLetterIDs = 0
    threeLetterIDs = 0

    for i in range(0, len(input)):
        for j in range(0, len(sorted(input[i]))):
            

if __name__ == "__main__":
    for path in sys.argv[1:]:
        input = parse(path)
        solve(input)