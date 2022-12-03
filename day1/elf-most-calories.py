#!/usr/bin/python3

import sys

filename = sys.argv[1]

input_file = open(filename, 'r')

calorie_list = [0]
i = 0

for line in input_file.readlines():
    if not line.strip():
        i += 1
        calorie_list.append(0)
    else:
        calorie_list[i] += int(line)


print(f'The most calories carried by one elf is {max(calorie_list)}')

calorie_list.sort(reverse=True)

print(f'The number of calories carried by the top three elves is {sum(calorie_list[0:3])}')


