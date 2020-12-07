import sys
import math
from collections import defaultdict

file_name = sys.argv[1]

groups = []
children_to_parents = defaultdict(list)
parents_to_children = defaultdict(list)
with open(file_name, 'r') as file:
    for line in file:
        line = line.rstrip()
        parent, all_children = line.replace('bags', '').replace('bag', '').replace('.', '').strip().split(" contain ")
        if all_children != 'no other':
            children = all_children.split(" , ")
            cleaned_children = [x.split(' ', 1) for x in children]
            for num, child in cleaned_children:
                children_to_parents[child.strip()].append(parent.strip())
                parents_to_children[parent.strip()].append((num, child.strip()))

parents = set()
def count_bags(children_to_parents, colour):
    immediate_parents = children_to_parents[colour]
    for immediate_parent in immediate_parents:
        parents.add(immediate_parent)
        count_bags(children_to_parents, immediate_parent)
    return len(parents)

result = 0
def count_bags_sum(children_to_parents, colour, level_mult):
    global result
    immediate_children = children_to_parents[colour]
    for count, immediate_child in immediate_children:
        result += int(level_mult) * int(count)
        count_bags_sum(children_to_parents, immediate_child, int(level_mult) * int(count))
    return result

sum_parents = count_bags(children_to_parents, 'shiny gold')
print(f'{sum_parents} top-level bags' )

bags_sum = count_bags_sum(parents_to_children, 'shiny gold', 1)
print(f'{bags_sum} needed bags' )
