from pathlib import Path
import sys
import math

def parse(inputFile):
    input = Path(inputFile).read_text().splitlines()
    return input

def solve(input):
    totalFuel = 0
    
    for i in range(0, len(input)):
        totalFuel += math.floor(int(input[i]) / 3) - 2
    print(totalFuel)

if __name__ == "__main__":
    for path in sys.argv[1:]:
        input = parse(path)
        solve(input)