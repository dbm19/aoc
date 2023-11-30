#aoc201601

#TODO
#it's not a intermiediate location you visit twice; it's anywhere along the path you've vistited twice

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
    location_history = {
        "0": [0]
    }

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
        print(location_history)
        if str(x_coordinate) in location_history:
            values = location_history[str(x_coordinate)]
            print(values)
            for j in range (0, len(values)):
                if values[j] == y_coordinate:
                    location = [x_coordinate, y_coordinate]
                    print(location)
                    print(location[0] + location[1])
                    return location
            location_history[str(x_coordinate)].append(y_coordinate)
        else:
            location_history[str(x_coordinate)] = []
            location_history[str(x_coordinate)].append(y_coordinate)
       # print(puzzleInput[i])
       # print(location_history)

if __name__ == "__main__":
    for path in sys.argv[1:]:
        puzzleInput = parse(path)
        solve(puzzleInput)

