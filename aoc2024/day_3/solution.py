from pathlib import Path
import sys
import re

def parse(input_file):
    input = Path(input_file).read_text()
    return input

def part1(input):
    pattern = r"mul\(\d+\,\d+\)" #Learning REGEX 
    x = re.findall(pattern, input)
    print(x)

    sum = 0
    for n in x:
        pattern = r"\d+"
        y = re.findall(pattern, n)
        print(y)
        product = int(y[0]) * int(y[1])
        print(product)
        sum += product
    
    print(sum)

def part2(input):
    pattern = r"mul\(\d+\,\d+\)|don't\(\)|do\(\)" #Alternator key | very nice 
    x = re.findall(pattern, input)
    print(x)

    sum = 0
    enabled = True
    y = []

    for i in range(0, len(x)):
        if x[i] == "don't()":
            enabled = False
            i += 1
        elif x[i] == "do()":
            enabled = True
            i += 1
        else:
            if enabled == True:
                y.append(x[i])
            else:
                continue
    
    for n in y:
        pattern = r"\d+"
        y = re.findall(pattern, n)
        print(y)
        product = int(y[0]) * int(y[1])
        print(product)
        sum += product 

    print(sum)
if __name__ == "__main__":
    for input_file in sys.argv[1:]:
        part1(parse(input_file))
        part2(parse(input_file))