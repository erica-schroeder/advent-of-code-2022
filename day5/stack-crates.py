#!/usr/bin/python3

import re
import sys

stacks = dict()

CHARS_PER_CRATE = 3
SPACE_BETWEEN_CRATES = 1


def calc_columns(str_len):
    return int((str_len - CHARS_PER_CRATE) / (CHARS_PER_CRATE + SPACE_BETWEEN_CRATES) + 1)


def make_stacks(num_cols):
    for col in range(0, num_cols):
        stacks[col] = []


def add_to_stacks(input_str, num_cols):
    for col in range(0, num_cols):
        crate = input_str[col * (CHARS_PER_CRATE + SPACE_BETWEEN_CRATES) + 1]
        if crate != ' ':
            stacks[col].append(crate)


def move_crates_9000(count, source, dest):
    for i in range(0, count):
        stacks[dest].append(stacks[source].pop())


def move_crates_9001(count, source, dest):
    for i in range(count-1, -1, -1):
        stacks[dest].append(stacks[source].pop(-(i+1)))


def process_instruction(input_str):
    m = re.match(r"move (?P<count>\d+) from (?P<source>\d+) to (?P<dest>\d+)", input_str)

    count = int(m.groupdict()["count"])
    source = int(m.groupdict()["source"]) - 1
    dest = int(m.groupdict()["dest"]) - 1

    move_crates_9001(count, source, dest)



filename = sys.argv[1]
input_file = open(filename, 'r')

first_line = input_file.readline()
cols = calc_columns(len(first_line) - 1)

make_stacks(cols)
add_to_stacks(first_line, cols)

# Parse the stacks
parsing_stacks = True
while(parsing_stacks):
    line = input_file.readline()
    if '[' in line:
        add_to_stacks(line, cols)
    else:
        parsing_stacks = False


for i in stacks:
    stacks[i].reverse()


# Parse the move instructions
for line in input_file.readlines():
    if 'move' in line:
        process_instruction(line)


top_crates = ''

for i in stacks:
    top_crates += stacks[i].pop()

print(f'Topmost crates are {top_crates}')



input_file.close()


