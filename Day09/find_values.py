import sys
import math
from collections import defaultdict

file_name = sys.argv[1]

lines = []
with open(file_name, 'r') as file:
    lines = [int(line.rstrip()) for line in file]

def solver(input_data, preamble_length):
    for index, num in enumerate(input_data):
        has_sum = False
        if index >= preamble_length:
            five_numbers = input_data[index-preamble_length:index]
            for test_num in five_numbers:
                if (num - test_num) in five_numbers:
                    has_sum = True
                    continue
            if not has_sum:
                return num
    return "No Result"

def find_contiguous_sum(input_data, target):
    curr_min_index = 0
    curr_max_index = 1
    curr_sum = input_data[curr_min_index] + input_data[curr_max_index]
    while (curr_max_index < len(input_data) - 1):
        if curr_sum == target:
            return min(input_data[curr_min_index:curr_max_index + 1]),  max(input_data[curr_min_index:curr_max_index + 1]), min(input_data[curr_min_index:curr_max_index + 1]) + max(input_data[curr_min_index:curr_max_index + 1])
        if curr_sum < target:
            next_val = input_data[curr_max_index + 1]
            curr_max_index += 1
            curr_sum = (curr_sum + next_val)
        elif (curr_sum > target):
            remove_val = input_data[curr_min_index]
            curr_min_index += 1
            curr_sum = (curr_sum - remove_val)
    return "No Result"

print(f'{solver(lines, 5)} with preamble length 5')
print(f'{solver(lines, 25)} with preamble length 25')
print(f'{find_contiguous_sum(lines, 127)} min and max values for 127')
print(f'{find_contiguous_sum(lines, 1124361034)} min and max values for 1124361034')
