import sys
import math
from collections import defaultdict

file_name = sys.argv[1]

lines = []
with open(file_name, 'r') as file:
    lines = [int(line.rstrip()) for line in file]

def find_no_sum_in_preamble(input_data, preamble_length):
    for index in range(preamble_length, len(input_data)):
        num = input_data[index]
        preamble = input_data[index - preamble_length:index]
        second_nums = [(num - first_num) for first_num in preamble]
        if True not in [(second_num in preamble) for second_num in second_nums]:
            return num
    return "No Result"

def find_contiguous_sum(input_data, target):
    curr_min_index = 0
    curr_max_index = 1
    curr_sum = sum(input_data[curr_min_index:curr_max_index + 1])
    while (curr_max_index < len(input_data) - 1):
        if curr_sum == target:
            curr_range = input_data[curr_min_index:curr_max_index + 1]
            return min(curr_range), max(curr_range), min(curr_range) + max(curr_range)
        if curr_sum < target:
            curr_max_index += 1
            curr_sum = sum(input_data[curr_min_index:curr_max_index + 1])
        elif curr_sum > target:
            curr_min_index += 1
            curr_sum = sum(input_data[curr_min_index:curr_max_index + 1])
    return "No Result"

print(f'{find_no_sum_in_preamble(lines, 25)} with preamble length 25')
print(f'{find_contiguous_sum(lines, 1124361034)} min and max values for 1124361034')
