from solutions.test.utils import parse_solution, assert_machine

TEST_CASES = [
    # Empty list
    ('##', True, '##'),

    # Invalid inputs
    ('#', False, None),
    ('', False, None),

    # Length 1
    ('#1#', True, '#1#'),

    # Larger length, sorted items
    ('#123#', True, '#123#'),

    # All elements the same
    ('#111#', True, '#111#'),

    # Reversed order
    ('#321#', True, '#123#'),

    # Only some elements
    ('#21#', True, '#12#'),
    ('#32#', True, '#23#'),
    ('#31#', True, '#13#'),

    # Larger list with unordered items
    ('#123123#', True, '#112233#'),
]


def test_sort():
    machine = parse_solution('sort3.txt')

    for input_string, accepts, output_string in TEST_CASES:
        assert_machine(machine, input_string, accepts, output_string)
