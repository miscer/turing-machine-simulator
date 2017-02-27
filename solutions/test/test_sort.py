from solutions.test.utils import parse_solution, assert_machine

TEST_CASES = [
    ('##', True, '##'),
    ('#', False, None),
    ('', False, None),
    ('#1#', True, '#1#'),
    ('#123#', True, '#123#'),
    ('#111#', True, '#111#'),
    ('#321#', True, '#123#'),
    ('#21#', True, '#12#'),
    ('#32#', True, '#23#'),
    ('#31#', True, '#13#'),
    ('#123123#', True, '#112233#'),
]


def test_sort():
    machine = parse_solution('sort3.txt')

    for input_string, accepts, output_string in TEST_CASES:
        assert_machine(machine, input_string, accepts, output_string)
