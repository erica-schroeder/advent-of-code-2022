#!/usr/bin/python3

import math
import sys

class Point:
    def __init__(self, x, y):
        self.x = x 
        self.y = y

    def __add__(self, other):
        x = self.x + other.x
        y = self.y + other.y
        return Point(x, y)

    def __repr__(self):
        return str((self.x, self.y))

    def __str__(self):
        return str((self.x, self.y))


UP = Point(0, 1)
DOWN = Point(0, -1)
LEFT = Point(-1, 0)
RIGHT = Point(1, 0)

DIR_MAP = { 'U': UP,
            'D': DOWN,
            'L': LEFT,
            'R': RIGHT }


# def move_knots(head, tail, direction):
#     new_head = Point(head.x + direction.x, head.y + direction.y)
#     new_tail = Point(tail.x, tail.y)

#     dist = math.dist((new_head.x, new_head.y), (tail.x, tail.y))

#     # diagonal case
#     if(dist > 2):
#         if direction == UP or direction == DOWN:
#             new_tail.x = new_head.x
#             new_tail.y += direction.y
#         else:
#             new_tail.x += direction.x
#             new_tail.y = new_head.y

#     # straight case
#     elif(dist == 2):
#         new_tail.x += direction.x
#         new_tail.y += direction.y

#     return new_head, new_tail
    

def adjust_knots(head, tail, i):
    new_tail = Point(tail.x, tail.y)

    delta = Point(head.x - tail.x, head.y - tail.y)
    abs_delta = Point(int(abs(delta.x)), int(abs(delta.y)))


    x_sign = 0 if not delta.x else int(delta.x/abs(delta.x))
    y_sign = 0 if not delta.y else int(delta.y/abs(delta.y))

    if(abs_delta.y == 2):
        if(abs_delta.x == 1):
            new_tail.x = head.x
            new_tail.y += y_sign
        elif(abs_delta.x == 2):
            new_tail.y += y_sign
            new_tail.x += x_sign
        else:
            new_tail.y += y_sign

    elif(abs_delta.x == 2):
        if(abs_delta.y == 1):
            new_tail.y = head.y
            new_tail.x += x_sign
            
        elif(abs_delta.y == 2):
            new_tail.y += y_sign
            new_tail.x += x_sign
        else:
            new_tail.x += x_sign
    

    # print(tail, new_tail)
    return new_tail



filename = sys.argv[1]
input_file = open(filename, 'r')

NUM_KNOTS = 10
knots = [Point(0,0) for _ in range(NUM_KNOTS)]
print(knots)

tails = set()

tails.add((int(knots[-1].x), int(knots[-1].y)))
for linenum,line in enumerate(input_file.readlines()):
    direction, number = line.split()
    
    for x in range(0, int(number)):
        knots[0].x += DIR_MAP[direction].x
        knots[0].y += DIR_MAP[direction].y

        for i in range(1, NUM_KNOTS):
            knots[i] = adjust_knots(knots[i-1], knots[i], (linenum, DIR_MAP[direction],line, x, i))

        
        tails.add((int(knots[-1].x), int(knots[-1].y)))


print(f'Number of points visited by tail is {len(tails)}')





