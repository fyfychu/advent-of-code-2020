import sys
from copy import deepcopy

file_name = sys.argv[1]

lines = []
area =[]
with open(file_name, 'r') as file:
    lines = [line.rstrip() for line in file]
    for line in lines:
        area.append(list(line))

print(area)


# seat empty + no occupied seats -> sit
# seat occupied with 4+ seats around -> empty
# otherwise same
def modify_seat(x, y, area):
    seat = area[x][y]
    num_occupied_seats = 0
    if x-1 >= 0 and area[x-1][y] == '#':
        num_occupied_seats += 1
    if x+1 < len(area) and area[x+1][y] == '#':
        num_occupied_seats += 1
    if y-1 >= 0 and area[x][y-1] == '#':
        num_occupied_seats += 1
    if y+1 < len(area[0]) and area[x][y+1] == '#':
        num_occupied_seats += 1
    if x-1 >= 0 and y-1 >= 0 and area[x-1][y-1] == '#':
        num_occupied_seats += 1
    if x-1 >= 0 and y+1 < len(area[0]) and area[x-1][y+1] == '#':
        num_occupied_seats += 1
    if x+1 < len(area) and y+1 < len(area[0]) and area[x+1][y+1] == '#':
        num_occupied_seats += 1
    if x+1 < len(area) and y-1 >= 0 and area[x+1][y-1] == '#':
        num_occupied_seats += 1

    #if x == 5 and y == 5:
    #    print(f'FOR {x}, {y} {seat} the OCCUPIED SEATS IS {num_occupied_seats} IN MAP: {area}')

    if num_occupied_seats >= 4 and seat == '#':
        return 'L'
    elif num_occupied_seats == 0 and seat == 'L':
        return '#'
    else:
        return seat

def count_occupied(area):
    result = 0
    for x in range(0, len(area)):
        for y in range(0, len(area[0])):
            if area[x][y] == '#':
                result += 1
    return result

def solve():
    iter_count = 0
    prev_area_iter = []
    next_area_iter = deepcopy(area)
    while next_area_iter != prev_area_iter:
        prev_area_iter = deepcopy(next_area_iter)
        for x in range(0, len(area)):
            for y in range(0, len(area[0])):
                new_position = modify_seat(x, y, prev_area_iter)
                next_area_iter[x][y] = new_position
        iter_count += 1
        print(f'ITER COUNT {iter_count}')
        for row in next_area_iter:
            print(f'{row}')
    return count_occupied(next_area_iter)

result = solve()

print(f'{result}')
