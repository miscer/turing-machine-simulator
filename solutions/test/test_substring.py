from solutions.test.utils import parse_solution, assert_accepts, assert_rejects

ACCEPTED_INPUTS = [
    '###', '##0101#', '#0#0#', '#1#1#', '#0101#0101#', '#110#1110#',
]

REJECTED_INPUTS = [
    '#01##', '#01#0#', '#0#111#',
]


def test_substring():
    machine = parse_solution('substring.txt')

    for input_string in ACCEPTED_INPUTS:
        assert_accepts(machine, input_string)

    for input_string in REJECTED_INPUTS:
        assert_rejects(machine, input_string)
