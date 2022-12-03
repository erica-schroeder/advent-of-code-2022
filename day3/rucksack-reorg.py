#!/usr/bin/python3

import sys

def calc_priority(item):
    if(item.isupper()):
        return ord(item) - 38
    else:
        return ord(item) - 96


def find_bad_item(items):
    comp1, comp2 = items[:len(items)//2], items[len(items)//2:]
    duplicate = set(comp1).intersection(comp2)
    return duplicate.pop()



filename = sys.argv[1]
input_file = open(filename, 'r')

sum_priorities = 0

for line in input_file.readlines():
    sum_priorities += calc_priority(find_bad_item(line.strip()))
    

print(f'Sum of priorities is {sum_priorities}')

