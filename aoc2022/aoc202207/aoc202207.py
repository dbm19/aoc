from pathlib import Path
import sys

def parse(inputFile):
  puzzleInput = Path(inputFile).read_text().splitlines()
  return puzzleInput

def solve(puzzleInput):
	directories = {}
	currentDirectory = ''

	for i in range(2, len(puzzleInput)):
		array = puzzleInput[i].split(' ')

		if array[0] == '$':
			if array[1] == 'cd' and array[2] != '..':
				currentDirectory = array[2]
			#else:
							
		elif array[0] == 'dir':
			directories['{}'.format(array[1])] = {}  
		#elif int(array[0]): 
		#	directories['{}'.format(array[1])] = array[0]

	print(directories)

if __name__ == '__main__':
  for path in sys.argv[1:]:
    puzzleInput = parse(path)
    solve(puzzleInput)
