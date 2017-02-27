from solutions.test.utils import parse_solution, assert_accepts, assert_rejects

ACCEPTED_INPUTS = [
    '', 'a', 'aa', 'aba', 'abba',
]

REJECTED_INPUTS = [
    'ab', 'aab', 'aaba',
]


def test_palindrome():
    machine = parse_solution('palindrome.txt')

    for input_string in ACCEPTED_INPUTS:
        assert_accepts(machine, input_string)

    for input_string in REJECTED_INPUTS:
        assert_rejects(machine, input_string)
