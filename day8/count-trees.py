#!/usr/bin/python3

import sys

class Tree:
    def __init__(self, coords, height):
        self.coords = coords 
        self.height = height
        self.scenic_score = 1

    def __repr__(self):
        return str(self.coords) + ' ' + str(self.height) + ' ' + str(self.scenic_score)

    def __str__(self):
        return str(self.coords) + ' ' + str(self.height) + ' ' + str(self.scenic_score)


def scan_trees(forest, visible_trees):
    top = 0
    bottom = len(forest)
    left = 0
    right = len(forest[0])
    
    for i in range(top, bottom) :
        for j in range(left, right):
            this_tree = forest[i][j]

            to_the_left = [tree.height for tree in forest[i][0:j]]
            to_the_right = [tree.height for tree in forest[i][j+1:right+1]]

            if not to_the_left or not to_the_right:
                visible_trees.add(this_tree.coords)
                this_tree.scenic_score = 0
            else:
                if this_tree.height > max(to_the_left) or this_tree.height > max(to_the_right):
                    visible_trees.add(this_tree.coords)

                score_left = 0
                for height in reversed(to_the_left):
                    score_left += 1
                    if this_tree.height <= height:
                        break

                score_right = 0
                for height in to_the_right:
                    score_right += 1
                    if this_tree.height <= height:
                        break


                this_tree.scenic_score *= score_left * score_right



filename = sys.argv[1]
input_file = open(filename, 'r')

forest = []

row = 0
for line in input_file.readlines():
    forest.append([])
    col = 0

    for height in line.strip():
        forest[row].append(Tree((row, col), int(height)))
        col += 1

    row += 1

input_file.close()


visible_trees = set()

scan_trees(forest, visible_trees)

temp = list(zip(*forest))
transposed_forest = [list(x) for x in temp]
scan_trees(transposed_forest, visible_trees)

print(f'Total visible trees: {len(visible_trees)}')

maxes = set()
for row in forest:
    maxes.add(max([tree.scenic_score for tree in row]))

print(f'Max scenic score is {max(maxes)}')

