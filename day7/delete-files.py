#!/usr/bin/python3

import re
import sys

class Directory:
    def __init__(self, parent):
        self.parent = parent
        self.dirs = []
        self.files = []

    def add_dir(self):
        dir = Directory(self)
        self.dirs.append(dir)
        return dir

    def add_file(self, size):
        self.files.append(size)

    def calc_size(self, record):
        my_size = 0

        for dir in self.dirs:
            my_size += dir.calc_size(record)

        my_size += sum(self.files)

        record.append(my_size)

        return my_size

        

filename = sys.argv[1]
input_file = open(filename, 'r')

root = Directory(None)
current_node = None

# Super brittle, completely dependent on specific pattern of navigating folders (e.g. not visiting the same folder multiple times)
for line in input_file.readlines():

    line = line.strip()
    print(line)

    # Root dir
    if line == "$ cd /":
        current_node = root
        print('making root node')
    elif line == "$ cd ..":
        current_node = current_node.parent
        print('moving to parent node')
    elif "$ cd" in line:
        current_node = current_node.add_dir()
        print('adding dir to node')
    else:
        m = re.match(r"(?P<file_size>\d+) \S*", line)
        if not m is None:
            file_size = int(m.groupdict()["file_size"])
            current_node.add_file(file_size)
            print(f'adding file of size {file_size}')

input_file.close()


record = []
total_space_used = root.calc_size(record)

sum_dirs = sum([val for val in record if val <= 100000])
print(f'The total size of directories <= 100k is {sum_dirs}')

TOTAL_DISK_SPACE = 70000000
DISK_SPACE_NEEDED = 30000000
free_space = TOTAL_DISK_SPACE - total_space_used

extra_space_needed = DISK_SPACE_NEEDED - free_space

delete_dirs = sorted([val for val in record if val >= extra_space_needed])

print(f'Directory of size {delete_dirs[0]} should be deleted.')

