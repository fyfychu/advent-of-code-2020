import sys
import math

file_name = sys.argv[1]

partitions = []
with open(file_name, 'r') as file:
    for line in file:
        partitions.append(line.rstrip())

def get_seat_numbers(partitions):
    seat_numbers = []
    for partition in partitions:
        row_l, row_h = 0, 127
        col_l, col_h = 0, 7
        for row_char in partition[:7]:
            if row_char == 'F':
               row_h = row_l + math.floor((row_h - row_l) / 2)
            else:
               row_l = row_h - math.floor((row_h - row_l) / 2)
        for col_char in partition[7:]:
            if col_char == 'L':
               col_h = col_l + math.floor((col_h - col_l) / 2)
            else:
               col_l = col_h - math.floor((col_h - col_l) / 2)
        seat_numbers.append(row_l * 8 + col_l)
    return seat_numbers

def find_highest_seat_id(partitions):
    seat_numbers = get_seat_numbers(partitions)
    return max(seat_numbers)

def find_my_seat(partitions):
    seat_numbers = get_seat_numbers(partitions)
    seat_numbers.sort()
    for index in range(1, len(seat_numbers) - 1):
        if seat_numbers[index - 1] == seat_numbers[index] - 2:
            return seat_numbers[index] - 1

seat = find_highest_seat_id(partitions)
my_seat = find_my_seat(partitions)
print(f'{seat} is the highest seat id')
print(f'{my_seat} is my seat')
