import sys
import copy

file_name = sys.argv[1]

lines = []
with open(file_name, 'r') as file:
    lines = [int(line.rstrip()) for line in file]

count_1 = 0
count_3 = 0
max_adapter = max(lines)
device_joltage = max_adapter + 3
joltage = 0
lines.sort()
for line in lines:
    if (line - joltage) == 1:
        count_1 += 1
    elif (line - joltage) == 3:
        count_3 += 1
    joltage = line

if device_joltage - joltage == 1:
    count_1 += 1
else:
    count_3 += 1

print(f'{count_1} {count_3} {count_1 * count_3}')

cache = {}
def count_combinations(input_nums, start):
    if len(input_nums) == 0:
        result = 1
    else:
        input_nums.sort()
        result = 0
        for n in range(1, 4):
            if (start + n) in input_nums:
                next_input_nums = copy.deepcopy(input_nums)
                if start in next_input_nums:
                    next_input_nums.remove(start)
                next_input_nums.remove(start+n)
                next_input_nums = [x for x in next_input_nums if x > start + n]
                key = (start + n, len(next_input_nums), sum(next_input_nums))
                if key in cache:
                    result += cache[key]
                else:
                    result += count_combinations(next_input_nums, start + n)
                    cache[key] = result
    return result

input_lines = copy.deepcopy(lines)
input_lines.append(device_joltage)
input_lines.sort()
result = count_combinations(input_lines, 0)
print(f'{result}')
