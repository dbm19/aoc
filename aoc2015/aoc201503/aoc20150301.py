#aoc20150101

import pathlib
import sys

def parse(puzzleInput):
  return list(pathlib.Path(puzzleInput).read_text())

def solve(puzzleInput):
  numberOfHouses = 1
  visitedHouses = {'00': 'visited'}
  coordinates = [0, 0]

  for datum in puzzleInput:
    match datum:
      case '^':
        coordinates[1] += 1
      case 'v':
        coordinates[1] -= 1
      case '>':
        coordinates[0] += 1
      case '<':
        coordinates[0] -= 1
    if coordinatesToString(coordinates) not in visitedHouses:
      numberOfHouses += 1
      visitedHouses[coordinatesToString(coordinates)] = 'visited'

  return numberOfHouses

def coordinatesToString(coordinates):
  coordinatesString = ''

  for coordinate in coordinates:
    coordinatesString += str(coordinate)

  return coordinatesString

if __name__ == "__main__":
  for path in sys.argv[1:]:
    print(solve(parse(path)))

