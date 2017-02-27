from itertools import count

from analysis.utils import parse_solution, count_transitions

INPUT_GENERATORS = [
    # #12# #112# #1112# #11112# ...
    ('#' + ('1' * n) + '2#' for n in count(start=1)),

    # #15# #115# #1115# #11115# ...
    ('#' + ('1' * n) + '5#' for n in count(start=1)),
]

machine = parse_solution('div4.txt')
count_transitions(machine, INPUT_GENERATORS, 100)