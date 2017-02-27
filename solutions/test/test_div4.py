from solutions.test.utils import parse_solution, assert_accepts, assert_rejects

ACCEPTED_INPUTS = [
    '#0#', '#4#', '#12#', '#16#', '#12312#', '#12304#', '#12300#',
]

REJECTED_INPUTS = [
    '', '#', '##', '#2#', '#6#', '#14#', '#18#',
]


def test_div4():
    machine = parse_solution('div4.txt')

    for input_string in ACCEPTED_INPUTS:
        assert_accepts(machine, input_string)

    for input_string in REJECTED_INPUTS:
        assert_rejects(machine, input_string)
