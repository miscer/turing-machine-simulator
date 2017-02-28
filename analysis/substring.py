from itertools import count

from analysis.utils import parse_solution, count_transitions

INPUT_GENERATORS = [
    # #0#1# #0#11# #0#111# ...
    ('#0#' + ('1' * n) + '#' for n in count(start=1)),

    # #0#0# #0#10# #0#110# ...
    ('#0#' + ('1' * n) + '0#' for n in count(start=0)),

    # #0#0# #0#00# #0#000# ...
    ('#0#' + ('0' * n) + '#' for n in count(start=1)),

    # #0#0# #00#00# #000#000# ...
    ('#' + ('0' * n) + '#' + ('0' * n) + '#' for n in count(start=1)),
]

machine = parse_solution('substring.txt')
count_transitions(machine, INPUT_GENERATORS, 100)
