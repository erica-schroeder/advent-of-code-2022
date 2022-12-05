#!/usr/bin/python3

import sys

def get_ranges(input_str):
    range_strs = input_str.split(',')

    ranges = []

    for i in [0, 1]:
        r = range_strs[i].split('-')
        ranges.append({j for j in range(int(r[0]), int(r[1]) + 1)})

    return ranges


filename = sys.argv[1]
input_file = open(filename, 'r')

sum_contained_ranges = 0
sum_overlapping_ranges = 0

for line in input_file.readlines():
    r = get_ranges(line.strip())
    inter = set.intersection(r[0], r[1])
    if len(inter):
        sum_overlapping_ranges += 1
    if inter == r[0] or inter == r[1]:
        sum_contained_ranges += 1

print(f'The number of contained ranges is {sum_contained_ranges}.')
print(f'The number of overlapping ranges is {sum_overlapping_ranges}.')

