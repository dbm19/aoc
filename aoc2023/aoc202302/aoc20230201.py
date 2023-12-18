from pathlib import Path
import sys

def parse(inputFile):
    parsedInput = Path(inputFile).read_text().splitlines()
    return parsedInput 

def solve(parsedInput):
    redCubeLimit = 12
    greenCubeLimit = 13
    blueCubeLimit = 14
    sum = 0
    
    for i in range(0, len(parsedInput)):
        gameNumber = parsedInput[i].split(":")[0].split(" ")[1]
        gameData = parsedInput[i].split(":")[1].split(";")
        possible = True

        for j in range(0, len(gameData)):
            gameData[j] = gameData[j].lstrip()
            parsedGameData = gameData[j].split(", ")

            for k in range(0, len(parsedGameData)):
                superParsedGameData = parsedGameData[k].split(" ")
                amount = int(superParsedGameData[0])
                colour = superParsedGameData[1]
                match colour:
                    case "red":
                        if amount > redCubeLimit:
                            possible = False
                            break
                    case "blue":
                        if amount > blueCubeLimit:
                            possible = False 
                            break
                    case "green":
                        if amount > greenCubeLimit:
                            possible = False 
                            break

        if possible == True:
            sum += int(gameNumber)

    print(sum)

if __name__ == "__main__":
    for path in sys.argv[1:]:
        solve(parse(path))