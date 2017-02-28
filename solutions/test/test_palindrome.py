from solutions.test.utils import parse_solution, assert_accepts, assert_rejects

ACCEPTED_INPUTS = [
    # Empty string
    '',

    # Single letter
    'a',

    # Even number of letters
    'aa', 'abba',

    # Odd number of letters
    'aba', 'ababa',
]

REJECTED_INPUTS = [
    # Not palindromes
    'ab', 'aab', 'aaba',
]


def test_palindrome():
    machine = parse_solution('palindrome.txt')

    for input_string in ACCEPTED_INPUTS:
        assert_accepts(machine, input_string)

    for input_string in REJECTED_INPUTS:
        assert_rejects(machine, input_string)
