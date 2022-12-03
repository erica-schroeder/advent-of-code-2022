#!/usr/bin/python3

import sys
from typing import NamedTuple

class RpsOutcome(NamedTuple):
    points: int
    conditions: list

win_outcome = RpsOutcome(points=6,
                         conditions=[ ('X', 'C'),
                                      ('Y', 'A'),
                                      ('Z', 'B') ])

lose_outcome = RpsOutcome(points=0,
                          conditions=[ ('X', 'B'),
                                       ('Y', 'C'),
                                       ('Z', 'A') ])

draw_outcome = RpsOutcome(points=3,
                          conditions=[ ('X', 'A'),
                                       ('Y', 'B'),
                                       ('Z', 'C') ])

move_values = {
        'X': 1,
        'Y': 2,
        'Z': 3
    }

def calc_score(me, them):
    for outcome in [win_outcome, lose_outcome, draw_outcome]:
        if (me, them) in outcome.conditions:
            return outcome.points + move_values[me]


filename = sys.argv[1]
input_file = open(filename, 'r')

total_score = 0;

for line in input_file.readlines():
    move = line.split()
    them = move[0]
    me = move[1]

    total_score += calc_score(me, them)

print(f'Total score is {total_score}')

