import sys

file_name = sys.argv[1]

base_map = []
with open(file_name, 'r') as file:
    for line in file:
       base_map.append(line.rstrip())

def count_trees(base_map, move):
    # 0, 0 at the top left starting position, then increment positively along x, y axis
    tree = '#'
    tree_count = 0
    x_size = len(base_map[0])
    y_size = len(base_map)
    x_move_increment = move['right']
    y_move_increment = move['down']
    curr_x, curr_y = 0, 0
    while (curr_y < y_size):
        tree_count += 1 if base_map[curr_y][curr_x] == tree else 0
        curr_y += y_move_increment
        curr_x = (curr_x + x_move_increment) % x_size
    return tree_count

tree_size = count_trees(base_map, {'right': 3, 'down': 1})
multiplied_size = count_trees(base_map, {'right': 1, 'down': 1}) * \
                   count_trees(base_map, {'right': 3, 'down': 1}) * \
                   count_trees(base_map, {'right': 5, 'down': 1}) * \
                   count_trees(base_map, {'right': 7, 'down': 1}) * \
                   count_trees(base_map, {'right': 1, 'down': 2})

print(f'{tree_size} trees encountered')
print(f'{multiplied_size} multiplied slopes')
