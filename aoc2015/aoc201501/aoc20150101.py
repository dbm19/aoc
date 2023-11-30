#aoc20150101

import pathlib
import sys

def parse(path):
  return list(pathlib.Path(path).read_text())


def solve(puzzleInput):
  finalFloor = 0

  for datum in puzzleInput:
    if datum == '(':
      finalFloor += 1
    else:
      finalFloor -= 1

  return finalFloor

if __name__ == "__main__":
  for path in sys.argv[1:]:
    puzzleInput = parse(path)
    print(puzzleInput, solve(puzzleInput))
