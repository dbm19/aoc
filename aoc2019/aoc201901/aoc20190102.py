from pathlib import Path
import sys
import math

def parse(inputFile):
    input = Path(inputFile).read_text().splitlines()
    return input

def solve(input):
    totalFuel = 0

    for i in range(0, len(input)):
        moduleFuel = math.floor((int(input[i])) / 3) - 2
        totalModuleFuel = moduleFuel           

        while moduleFuel > 0:
            moduleFuel = math.floor((moduleFuel) / 3) - 2
            if moduleFuel <= 0:
                break
            totalModuleFuel += moduleFuel 
        
        totalFuel += totalModuleFuel

    print("totalfuel = ",  totalFuel)

if __name__ == "__main__":
    for path in sys.argv[1:]:
        input = parse(path)
        solve(input)