import sys
import math

file_name = sys.argv[1]

groups = []
with open(file_name, 'r') as file:
    group_member_count = 0
    group_map = {}
    for line in file:
        if line != '\n':
            items = line.rstrip()
            for item in items:
                group_map[item] = group_map.get(item, 0) + 1
            group_member_count += 1
        else:
            groups.append((group_member_count, group_map))
            group_member_count = 0
            group_map = {}
    groups.append((group_member_count, group_map))

def sum_answers_over_groups(groups, all_present=False):
    answers_sum = 0
    for group_member_count, group_map in groups:
        if all_present:
            keys_all_present = list(filter(lambda key: group_map[key] == group_member_count, group_map.keys()))
            answers_sum += len(keys_all_present)
        else:
            answers_sum += len(group_map)
    return answers_sum

answers_sum = sum_answers_over_groups(groups)
answers_sum_all_present = sum_answers_over_groups(groups, True)
print(f'{answers_sum} unique over groups' )
print(f'{answers_sum_all_present} all present in groups' )
