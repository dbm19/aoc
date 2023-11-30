#aoc202201

from pathlib import Path
import sys

def parse(inputFile):
  puzzleInput = [x.split(',') for x in Path(inputFile).read_text().splitlines()]
  for i in range(len(puzzleInput)):
    puzzleInput[i][0] = puzzleInput[i][0].partition('-')    
    puzzleInput[i][1] = puzzleInput[i][1].partition('-')
  return puzzleInput

def solvePartOne(puzzleInput):

def solvePartTwo(puzzleInput):

if __name__ == "__main__":
  for path in sys.argv[1:]:
    puzzleInput = parse(path)
    #solvePartOne(puzzleInput)
    #solvePartTwo(puzzleInput)
