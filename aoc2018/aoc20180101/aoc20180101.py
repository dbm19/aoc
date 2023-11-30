from pathlib import Path
import sys

def parse(inputFile):
    input = Path(inputFile).read_text().splitlines()
    return input

def solve(input):
    frequency = 0
    
    for i in range(0, len(input)):
        if input[i][0] == "+":
            frequency += int(input[i][1:])
        else:
            frequency -= int(input[i][1:])
        
    print(frequency)

if __name__ == "__main__":
    for path in sys.argv[1:]:
        input = parse(path)
        solve(input)