from itertools import count

from math import ceil, floor

from analysis.utils import parse_solution, count_transitions

INPUT_GENERATORS = [
    # 0#1#1 00#11#11 000#111#111 ...
    (('0' * n) + '#' + ('1' * n) + '#' + ('1' * n) for n in count(start=1)),

    # 0#1#0 00#11#01 000#111#011 ...
    (('0' * n) + '#' + ('1' * n) + '#0' + ('1' * (n-1)) for n in count(start=1)),

    # 0#1#0 00#11#10 000#111#110 ...
    (('0' * n) + '#' + ('1' * n) + '#' + ('1' * (n-1)) + '0' for n in count(start=1)),

    # 0#1#0 0#1#00 0#1#000 ...
    ('0#1#' + ('0' * n) for n in count(start=1)),

    # 0#1#1 0#1#10 0#1#100 ...
    ('0#1#1' + ('0' * n) for n in count(start=0)),
]

machine = parse_solution('addition.txt')
count_transitions(machine, INPUT_GENERATORS, 100)
