#!/usr/bin/python3

import sys

def calc_priority(item):
    print(f'ascii value is {ord(item)}')
    if(item.isupper()):
        return ord(item) - 38
    else:
        return ord(item) - 96


def find_badge(group):
    duplicate = set.intersection(set(group[0]), set(group[1]), set(group[2]))
    return duplicate.pop()



filename = sys.argv[1]
input_file = open(filename, 'r')

sum_priorities = 0
group = []

for line in input_file.readlines():
    group.append(line.strip())

    if len(group) == 3:
        sum_priorities += calc_priority(find_badge(group))
        group.clear()
    

print(f'Sum of priorities is {sum_priorities}')

