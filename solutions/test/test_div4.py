from solutions.test.utils import parse_solution, assert_accepts, assert_rejects

ACCEPTED_INPUTS = [
    # Divisible, single digit
    '#0#', '#4#',

    # Divisible, two digits
    '#12#', '#16#',

    # Divisible, more than two digits
    '#12312#', '#12304#', '#12300#',
]

REJECTED_INPUTS = [
    # Invalid inputs
    '', '#', '##',

    # Not divisible, one digit
    '#2#', '#6#',

    # Not divisible, two digits
    '#14#', '#18#',

    # Not divisible, more than two digits
    '#12314#', '#12318#',
]


def test_div4():
    machine = parse_solution('div4.txt')

    for input_string in ACCEPTED_INPUTS:
        assert_accepts(machine, input_string)

    for input_string in REJECTED_INPUTS:
        assert_rejects(machine, input_string)
