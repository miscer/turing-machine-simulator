from solutions.test.utils import parse_solution, assert_accepts, assert_rejects

ACCEPTED_INPUTS = [
    '0#0#0', '0#1#1', '1#0#1', '1#1#01', '001#010#0110000', '11#11#011', '11#11#011000',
]

REJECTED_INPUTS = [
    '', '#', '0#0', '0#0#1', '0#1#0', '1#0#0', '1#1#1', '1#1#0', '000#111#11',
    '##', '0##0', '#0#0', '0#0#', '0##', '#0#', '##0'
]


def test_addition():
    machine = parse_solution('addition.txt')

    for input_string in ACCEPTED_INPUTS:
        assert_accepts(machine, input_string)

    for input_string in REJECTED_INPUTS:
        assert_rejects(machine, input_string)
