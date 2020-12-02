import sys

file_name, target_sum = sys.argv[1:]
with open(file_name, 'r') as file:
   lines = file.readlines()

numbers = []
for line in lines:
   numbers.append(int(line))

numbers.sort()

def find_pair_for_target_sum(target_sum, numbers):
    for index, number in enumerate(numbers):
        if number > target_sum:
            return
        else:
            second_index = len(numbers) - index - 1
            while second_index > index:
                second_number = numbers[second_index]
                this_sum = number + second_number
                if this_sum == target_sum:
                    return number, second_number
                if this_sum < target_sum:
                    break
                else:
                    second_index -= 1


def find_triple_for_target_sum(target_sum, numbers):
    for index, number in enumerate(numbers):
        if number > target_sum:
            return
        else:
            third_index = len(numbers) - index - 1
            while third_index > index:
                third_number = numbers[third_index]
                second_index = third_index - 1
                while second_index > index:
                    second_number = numbers[second_index]
                    this_sum = number + second_number + third_number
                    if this_sum == target_sum:
                        return number, second_number, third_number
                    if this_sum < target_sum:
                        break
                    else:
                        second_index -= 1
                third_index -= 1

try:
    number, second_number = find_pair_for_target_sum(int(target_sum), numbers)
    print(f'{number}*{second_number} = {number*second_number}')
except:
    print(f'Cannot sum to {target_sum} with tuple')

try:
    number, second_number, third_number = find_triple_for_target_sum(int(target_sum), numbers)
    print(f'{number}*{second_number}*{third_number} = {number*second_number*third_number}')
except:
    print(f'Cannot sum to {target_sum} with triple')
