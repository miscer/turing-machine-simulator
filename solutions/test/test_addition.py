from solutions.test.utils import parse_solution, assert_accepts, assert_rejects

ACCEPTED_INPUTS = [
    # Correct sums for each combination of digits
    '0#0#0',
    '0#1#1',
    '1#0#1',
    '1#1#01',

    # Longer numbers
    '001#010#0110000',

    # Using carry bit with longer numbers
    '11#11#011',
    '11#11#011000',

    # Different lengths of numbers
    '0#11#11',
    '1#01#11',
    '11#0#11',
    '01#1#11',
    '00#10#1',
    '00#00#0',
]

REJECTED_INPUTS = [
    # Invalid inputs
    '', '#', '0#0', '##', '0##0', '#0#0', '0#0#', '0##', '#0#', '##0',

    # Incorrect sums
    '0#0#1', '0#1#0', '1#0#0', '1#1#1', '1#1#0', '000#111#11',
]


def test_addition():
    machine = parse_solution('addition.txt')

    for input_string in ACCEPTED_INPUTS:
        assert_accepts(machine, input_string)

    for input_string in REJECTED_INPUTS:
        assert_rejects(machine, input_string)
