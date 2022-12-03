#!/usr/bin/python3

import sys
from typing import NamedTuple

class RpsOutcome(NamedTuple):
    name: str
    points: int
    conditions: list

win_outcome = RpsOutcome(name='win',
                         points=6,
                         conditions=[ ('X', 'C'),
                                      ('Y', 'A'),
                                      ('Z', 'B') ])

lose_outcome = RpsOutcome(name='lose',
                          points=0,
                          conditions=[ ('X', 'B'),
                                       ('Y', 'C'),
                                       ('Z', 'A') ])

draw_outcome = RpsOutcome(name='draw',
                          points=3,
                          conditions=[ ('X', 'A'),
                                       ('Y', 'B'),
                                       ('Z', 'C') ])

move_values = {
        'X': 1,
        'Y': 2,
        'Z': 3
}

outcome_dict = {
        'X': lose_outcome,
        'Y': draw_outcome,
        'Z': win_outcome
}

def calc_score(outcome, them):
    me = next((cond[0] for cond in outcome.conditions if cond[1] == them), None)
    return outcome.points + move_values[me]


filename = sys.argv[1]
input_file = open(filename, 'r')

total_score = 0;

for line in input_file.readlines():
    move = line.split()
    them = move[0]
    outcome = outcome_dict[move[1]]

    total_score += calc_score(outcome, them)

print(f'Total score is {total_score}')

