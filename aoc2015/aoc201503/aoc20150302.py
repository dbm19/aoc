#aoc20150101

import pathlib
import sys

def parse(puzzleInput):
  return list(pathlib.Path(puzzleInput).read_text())

def solve(puzzleInput):
  numberOfHouses = 1
  visitedHouses = {'00': ['visited', numberOfHouses]}
  santaCoordinates = [0, 0]
  roboSantaCoordinates = [0, 0]

  for i in range(0, len(puzzleInput)):
    if i % 2 == 0:
      match puzzleInput[i]:
        case '^':
          santaCoordinates[1] += 1
        case 'v':
          santaCoordinates[1] -= 1
        case '>':
          santaCoordinates[0] += 1
        case '<':
          santaCoordinates[0] -= 1
      if coordinatesToString(santaCoordinates) not in visitedHouses:
        numberOfHouses += 1
        visitedHouses[coordinatesToString(santaCoordinates)] = ['visited', numberOfHouses]
    else:
      match puzzleInput[i]:
        case '^':
          roboSantaCoordinates[1] += 1
        case 'v':
          roboSantaCoordinates[1] -= 1
        case '>':
          roboSantaCoordinates[0] += 1
        case '<':
          roboSantaCoordinates[0] -= 1
      if coordinatesToString(roboSantaCoordinates) not in visitedHouses:
        numberOfHouses += 1
        visitedHouses[coordinatesToString(roboSantaCoordinates)] = ['visited', numberOfHouses]
  print(visitedHouses)
  return numberOfHouses

def coordinatesToString(coordinates):
  coordinatesString = ''

  for coordinate in coordinates:
    coordinatesString += str(coordinate)

  return coordinatesString

if __name__ == "__main__":
  for path in sys.argv[1:]:
    print(solve(parse(path)))

