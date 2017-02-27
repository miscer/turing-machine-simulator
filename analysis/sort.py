from itertools import count

from analysis.utils import parse_solution, count_transitions

INPUT_GENERATORS = [
    # ## #1# #11# #111# ...
    ('#' + ('1' * n) + '#' for n in count(start=0)),

    # #13# #113# #1113# ...
    ('#' + ('1' * n) + '3#' for n in count(start=1)),

    # #321# #332211# #333222111# ...
    ('#' + ('3' * n) + ('2' * n) + ('1' * n) + '#' for n in count(start=1)),
]

machine = parse_solution('sort3.txt')
count_transitions(machine, INPUT_GENERATORS, 100)