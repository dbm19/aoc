from pathlib import Path
import sys
import re

def parse(input_file):
    input = Path(input_file).read_text()
    return input

def part1(input):
    pattern = r"mul\(\d+\,\d+\)" 
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
   pattern = r"don't\(\)" 
   x = re.findall(pattern, input)
   print(x)

if __name__ == "__main__":
    for input_file in sys.argv[1:]:
        part1(parse(input_file))
        part2(parse(input_file))