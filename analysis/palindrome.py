from itertools import count

from math import ceil, floor

from analysis.utils import parse_solution, count_transitions

INPUT_GENERATORS = [
    # ab aab aabb aaabb ...
    (('a' * ceil(n)) + ('b' * floor(n)) for n in count(start=1, step=0.5)),

    # ab aab aaab ...
    (('a' * n) + 'b' for n in count(start=1)),

    # ab aba aaba aabaa aaabaa aaabaaa ...
    (('a' * floor(n)) + 'ab' + ('a' * ceil(n)) for n in count(start=0, step=0.5)),

    # a aa aaa aaaa ...
    ('a' * n for n in count(start=1)),
]

machine = parse_solution('palindrome.txt')
count_transitions(machine, INPUT_GENERATORS, 100)
