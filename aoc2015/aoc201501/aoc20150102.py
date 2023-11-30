#aoc20150102

import pathlib
import sys

def parse(path):
  return list(pathlib.Path(path).read_text())


def solve(puzzleInput):
  currentFloor = 0

  for index, datum in enumerate(puzzleInput):
    if datum == '(':
      currentFloor += 1
    else:
      currentFloor -= 1

    if currentFloor == -1:
      return index + 1

if __name__ == "__main__":
  for path in sys.argv[1:]:
    puzzleInput = parse(path)
    print(solve(puzzleInput))


