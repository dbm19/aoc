from pathlib import Path
import sys

def parse(input_file):
    input = Path(input_file).read_text().split("\n")
    return input

def part1(input):
    xmas_total = 0

    for i, n in enumerate(input):
        input[i] = list(n) 
    
    for j, n in enumerate(input):
        for i in range(0, len(n)):
            if n[i] == "X":
                if i < len(n) - 3: 
                    if n[i + 1] == "M" and n[i + 2] == "A" and n[i + 3] == "S":
                        xmas_total += 1
                    if j < len(input) - 3:
                        if input[j + 1][i + 1] == "M" and input[j + 2][i + 2] == "A" and input[j + 3][i + 3] == "S":
                            xmas_total += 1
                    if j > 2:
                        if input[j - 1][i + 1] == "M" and input[j - 2][i + 2] == "A" and input[j - 3][i + 3] == "S":
                            xmas_total += 1
                if i > 2:
                    if n[i - 1] == "M" and n[i - 2] == "A" and n[i - 3] == "S":
                        xmas_total += 1
                    if j < len(input) - 3:
                        if input[j + 1][i - 1] == "M" and input[j + 2][i - 2] == "A" and input[j + 3][i - 3] == "S":
                            xmas_total += 1 
                    if j > 2:
                        if input[j - 1][i - 1] == "M" and input[j - 2][i - 2] == "A" and input[j - 3][i - 3] == "S":
                            xmas_total += 1
                if j < len(input) - 3:
                    if input[j + 1][i] == "M" and input[j + 2][i] == "A" and input[j + 3][i] == "S":
                        xmas_total += 1
                if j > 2:
                    if input[j - 1][i] == "M" and input[j - 2][i] == "A" and input[j - 3][i] == "S":
                        xmas_total += 1 
 

    print(xmas_total)
    pass

def part2(input):
    pass

if __name__ == "__main__":
    for input_file in sys.argv[1:]:
        part1(parse(input_file))
        part2(parse(input_file))