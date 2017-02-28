from solutions.test.utils import parse_solution, assert_accepts, assert_rejects

ACCEPTED_INPUTS = [
    # Both strings empty
    '###',

    # Needle string empty
    '##0101#',

    # Both strings are equal
    '#0#0#',
    '#1#1#',
    '#0101#0101#',

    # Part of needle string occurrs in the haystack string more than once
    '#110#1110#',
    '#101#100101#',
]

REJECTED_INPUTS = [
    # Empty haystack string
    '#01##',

    # Needle string not in haystack string
    '#01#0#',
    '#0#111#',
]


def test_substring():
    machine = parse_solution('substring.txt')

    for input_string in ACCEPTED_INPUTS:
        assert_accepts(machine, input_string)

    for input_string in REJECTED_INPUTS:
        assert_rejects(machine, input_string)
