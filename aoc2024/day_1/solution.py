from pathlib import Path
import sys

def parse(inputFile):
    input = Path(inputFile).read_text().split()
    return input 

def part1(input):
    left_list = []
    right_list = []
    total_distance = 0

    for idx, n in enumerate(input):
        if idx % 2 == 0:
            left_list.append(int(n))
        else:
            right_list.append(int(n))

    left_list.sort()
    right_list.sort()

    for l, r in zip (left_list, right_list):
        total_distance += abs(l - r)

    print(total_distance)

def part2(input):
    left_list = []
    right_list = []
    similarity_score = 0

    for idx, n in enumerate(input):
        if idx % 2 == 0:
            left_list.append(int(n))
        else:
            right_list.append(int(n))
    
    for l in left_list:
        multiplier = 0
        for r in right_list:
            if l == r:
               multiplier += 1 
        similarity_score += l * multiplier

    print(similarity_score)

if __name__ == "__main__":
    for path in sys.argv[1:]:
        part1(parse(path))
        part2(parse(path))