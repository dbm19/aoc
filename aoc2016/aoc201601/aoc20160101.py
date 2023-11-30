#aoc201601

from pathlib import Path
import sys

def parse(inputFile):
    puzzleInput = Path(inputFile).read_text().split(", ")
    return puzzleInput    

def rotate(orientation, direction):
    if direction == "R":
        match orientation:
            case "N":
                return "E"    
            case "E":
                return "S"
            case "S":
                return "W"
            case "W":
                return "N"
    else:
        match orientation:
            case "N":
                return "W"    
            case "E":
                return "N"
            case "S":
                return "E"
            case "W":
                return "S"

def solve(puzzleInput):
    x_coordinate = 0
    y_coordinate = 0
    orientation = "N"

    for i in range(0, len(puzzleInput)):
        orientation = rotate(orientation, puzzleInput[i][0]) 
        match orientation:
            case "N":
                y_coordinate += int(puzzleInput[i][1:])
            case "E":
                x_coordinate += int(puzzleInput[i][1:])
            case "S":
                y_coordinate -= int(puzzleInput[i][1:])
            case "W":
                x_coordinate -= int(puzzleInput[i][1:]) 
        
    print (x_coordinate, y_coordinate, x_coordinate+y_coordinate)

if __name__ == "__main__":
    for path in sys.argv[1:]:
        puzzleInput = parse(path)
        solve(puzzleInput)

