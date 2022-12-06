#!/usr/bin/python3

import sys

NUM_DISTINCT_CHARS = 14

def has_marker(buffer):
    if(len(buffer) == len(set(buffer))):
        return True
    else:
        return False


filename = sys.argv[1]
input_file = open(filename, 'r')

char_count = 0
chars = []
found_it = False


for i in range(0, NUM_DISTINCT_CHARS):
    chars.append(input_file.read(1))
    char_count += 1

found_it = has_marker(chars)

while not found_it:
    if(len(chars) == NUM_DISTINCT_CHARS):
        chars.pop(0)

    chars.append(input_file.read(1))
    char_count += 1
    found_it = has_marker(chars)


if found_it:
    print(f'Detected start-of-packet marker after {char_count} characters.')
else:
    print('Uhh, didn\'t find the marker....')


input_file.close()


