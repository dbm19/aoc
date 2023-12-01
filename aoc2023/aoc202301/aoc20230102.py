from pathlib import Path
import sys

def parse(inputFile):
    parsedInput = Path(inputFile).read_text().splitlines()
    return parsedInput 

def solve(input):
    sumCalibrationValues = 0

    for i in range(0, len(input)):
        calibrationValue = ""
        for j in range(0, len(input[i])):
            if not input[i][j].isalpha():
                calibrationValue = calibrationValue + input[i][j]
            if len(calibrationValue) >= 3:
                calibrationValue = calibrationValue[0] + calibrationValue[-1]        
            elif len(calibrationValue) == 1:
                calibrationValue = calibrationValue + input[i][j]
        sumCalibrationValues += int(calibrationValue)

    print(sumCalibrationValues)

if __name__ == "__main__":
    for path in sys.argv[1:]:
        solve(parse(path))