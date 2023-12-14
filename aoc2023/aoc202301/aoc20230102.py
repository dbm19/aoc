from pathlib import Path
import sys

def parse(inputFile):
    parsedInput = Path(inputFile).read_text().splitlines()
    return parsedInput 

def solve(input):
    sumCalibrationValues = 0

    for i in range(0, len(input)):
        calibrationValue = ""
        numberWord = ""
        isLetters = True
        numberWords = {
                "one": "1", 
                "two": "2",
                "three": "3",
                "four": "4",
                "five": "5",
                "six": "6",
                "seven": "7",
                "eight": "8",
                "nine": "9"
            }

        for j in range(0, len(input[i])):
            if not input[i][j].isalpha():
                calibrationValue = calibrationValue + input[i][j]
                isLetters = False
                numberWord = ""
            else: 
                isLetters = True
                k = j
                while isLetters == True:
                    if len(numberWord) <= 4:
                        print(numberWord)
                        if input[i][k].isalpha():
                            numberWord = numberWord + input[i][k]
                            print(numberWord)
                            if len(numberWord) > 2:
                                for l in numberWords: 
                                    if numberWord == l:
                                        calibrationValue = calibrationValue + numberWords[l]
                                        numberWord = ""
                            k += 1 
                            if k == len(input[i]):
                                isLetters = False
                                numberWord = ""
                        else:
                            isLetters = False
                            numberWord = ""
                    else:
                        numberWord = ""
                        break
        if len(calibrationValue) >= 3:
            calibrationValue = calibrationValue[0] + calibrationValue[-1]        
        elif len(calibrationValue) == 1:
            calibrationValue = calibrationValue + calibrationValue 
        print(calibrationValue)
        sumCalibrationValues += int(calibrationValue)

    print("Sum =", sumCalibrationValues)

if __name__ == "__main__":
    for path in sys.argv[1:]:
        solve(parse(path))