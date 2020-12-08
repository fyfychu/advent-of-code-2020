import sys
import math
from collections import defaultdict

file_name = sys.argv[1]

index_seen_in_loop = set()
acc= 0
index = 0
lines = []
with open(file_name, 'r') as file:
    lines = [line.rstrip() for line in file]
    total_lines = len(lines)
    line = lines[index]
    while (index not in index_seen_in_loop):
        op, val = line.split()
        sign, val = val[0], val[1:]
        index_seen_in_loop.add(index)
        if op == 'acc':
            acc += int(val) if sign == '+' else -int(val)
            index = (index + 1) % total_lines
        elif op == 'jmp':
            index =  ((index + int(val)) % total_lines) if sign == '+' else ((index - int(val)) % total_lines)
        else: # nop
            index = (index + 1) % total_lines
        line = lines[index]
    print(f'{acc} accumulator value before loop')

def acc_with_flip(lines):
    index, in_flip, acc = 0, False, 0
    while (index != 0 or in_flip is False):
        # if it's in flipped, reset
        if index in index_seen_in_loop and in_flip:
            index, in_flip, acc = 0, False, 0
        line = lines[index]
        op, val = line.split()
        sign, val = val[0], val[1:]
        index_seen_in_loop.add(index)
        if op == 'acc':
            acc += int(val) if sign == '+' else -int(val)
            index = (index + 1) % total_lines
        elif op == 'jmp':
            if in_flip:
                index =  ((index + int(val)) % total_lines) if sign == '+' else ((index - int(val)) % total_lines)
            else: # flip if nothing is flipped
                index_after_flip = (index + 1) % total_lines
                if index_after_flip in index_seen_in_loop:
                    index =  ((index + int(val)) % total_lines) if sign == '+' else ((index - int(val)) % total_lines)
                else:
                    index = index_after_flip
                    in_flip = True
        else: # nop
            if in_flip:
                index = (index + 1) % total_lines
            else: # flip if nothing is flipped
                index_after_flip =  ((index + int(val)) % total_lines) if sign == '+' else ((index - int(val)) % total_lines)
                if index_after_flip in index_seen_in_loop:
                    index = (index + 1) % total_lines
                else:
                    index = index_after_flip
                    in_flip = True
    return acc

print(f'{acc_with_flip(lines)} accumulator value with flipped operation')


