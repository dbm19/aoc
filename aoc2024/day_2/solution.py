from pathlib import Path
import sys

def parse(input_file):
    input = Path(input_file).read_text().split("\n")
    return input

def part1(input):
    safe_total = 0

    for n in input:
        n = n.split() 
        n = list(map(int, n))
        previous_direction = -9
        current_direction = 0

        for i in range(1, len(n)):
            if n[i] > n[i - 1]:
                current_direction = 1 
            elif n[i] < n[i - 1]:
                current_direction = -1
            else:
                break

            if previous_direction != -9:
                if current_direction != previous_direction:
                    break
            else:
                previous_direction = current_direction

            if abs(n[i] - n[i - 1]) > 3:
                break
            
            if i == (len(n) - 1):
                safe_total += 1

    print("safe total = ", safe_total)

def part2(input):
    safe_total = 0
     
    for n in input:
        n = n.split() 
        n = list(map(int, n))
        previous_direction = -9
        current_direction = 0

        for i in range(1, len(n)):
            if n[i] > n[i - 1]:
                current_direction = 1 
            elif n[i] < n[i - 1]:
                current_direction = -1
            else:
                safe_total += make_test_lists(n, i)
                break

            if previous_direction != -9:
                if current_direction != previous_direction:
                    safe_total += make_test_lists(n, i)
                    break
            else:
                previous_direction = current_direction

            if abs(n[i] - n[i - 1]) > 3:
                safe_total += make_test_lists(n, i)
                break
            
            if i == (len(n) - 1):
                safe_total += 1
    print(safe_total)
    print("safe total with dampener =", safe_total)

def make_test_lists(n, i):
    test_list_1 = n.copy()
    test_list_2 = n.copy()
    test_list_3 = n.copy()
    test_list_1.pop(i)
    test_list_2.pop(i - 1)
    test_list_3.pop(0) #this is to cover the edge in which you get a safe report by removing the first level
    print(test_list_1, test_list_2, test_list_3)

    if check_list(test_list_1):
        print("huh")
        return 1
    elif check_list(test_list_2):
        return 1
    elif check_list(test_list_3):
        return 1
    else:
        return 0


def check_list(n):
    safe = False
    previous_direction = -9
    current_direction = 0

    for i in range(1, len(n)):
        if n[i] > n[i - 1]:
            current_direction = 1 
        elif n[i] < n[i - 1]:
            current_direction = -1
        else:
            break

        if previous_direction != -9:
            if current_direction != previous_direction:
                break
        else:
            previous_direction = current_direction

        if abs(n[i] - n[i - 1]) > 3:
            break
        
        if i == (len(n) - 1):
            safe = True
    print(safe)
    return safe 

if __name__ == "__main__":
    for input_file in sys.argv[1:]:
        part1(parse(input_file))
        part2(parse(input_file))