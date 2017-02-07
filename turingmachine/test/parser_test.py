import os
from unittest.mock import mock_open

import pytest

from turingmachine.parser import parse_turing_machine, parse_direction, ParseError, parse_letter, parse_states, \
    parse_alphabet, parse_transition_table
from turingmachine.types import Direction

FIXTURES_DIR = os.path.join(os.path.dirname(__file__), 'fixtures')


def open_mock_file(lines):
    file_content = '\n'.join(lines)
    open = mock_open(read_data=file_content)
    return open()


def test_parse_direction():
    assert parse_direction('L') == Direction.left
    assert parse_direction('R') == Direction.right

    with pytest.raises(ParseError):
        parse_direction('a')


def test_parse_letter():
    assert parse_letter('A', {'A', 'B'}) == 'A'
    assert parse_letter('_', {'A'}) is None

    with pytest.raises(ParseError):
        parse_letter('B', {'A'})


def test_parse_states():
    def open_fixture(name):
        return open(os.path.join(FIXTURES_DIR, '{}.txt'.format(name)))

    with open_mock_file(['states 4', 'q0', 'q1', 'qa +', 'qr -']) as file:
        assert parse_states(file) == ('qa', 'qr', 'q0', {'q0', 'q1', 'qa', 'qr'})

    with open_mock_file(['states 4', 'q0', 'q1', 'qa', 'qr -']) as file, pytest.raises(ParseError):
        parse_states(file)

    with open_mock_file(['states 4', 'q0', 'q1', 'qa +', 'qr +']) as file, pytest.raises(ParseError):
        parse_states(file)

    with open_mock_file(['states 4', 'q0', 'q0', 'qa +', 'qr -']) as file, pytest.raises(ParseError):
        parse_states(file)

    with open_mock_file(['states 0']) as file, pytest.raises(ParseError):
        parse_states(file)

    with open_mock_file(['foo 4', 'q0', 'q1', 'qa +', 'qr -']) as file, pytest.raises(ParseError):
        parse_states(file)

    with open_mock_file(['states']) as file, pytest.raises(ParseError):
        parse_states(file)

    with open_mock_file(['states bar']) as file, pytest.raises(ParseError):
        parse_states(file)


def test_parse_alphabet():
    with open_mock_file(['alphabet 2 a b']) as file:
        assert parse_alphabet(file) == {'a', 'b'}

    with pytest.raises(ParseError), open_mock_file(['alphabet 0']) as file:
        parse_alphabet(file)

    with pytest.raises(ParseError), open_mock_file(['alphabet 2 a a']) as file:
        parse_alphabet(file)

    with pytest.raises(ParseError), open_mock_file(['alphabet 2 a b c']) as file:
        parse_alphabet(file)

    with pytest.raises(ParseError), open_mock_file(['foo 2 a b']) as file:
        parse_alphabet(file)

    with pytest.raises(ParseError), open_mock_file(['alphabet']) as file:
        parse_alphabet(file)

    with pytest.raises(ParseError), open_mock_file(['alphabet foo']) as file:
        parse_alphabet(file)


def test_parse_transition_table():
    with open_mock_file([
        'q0 a q0 a R',
        'q0 _ qr _ L',
        'q1 a qr a L',
        'q1 _ qa _ L'
    ]) as file:
        assert parse_transition_table(
            file,
            {'q0', 'q1', 'qa', 'qr'},
            {'a'}
        ) == {
            ('q0', 'a'): ('q0', 'a', Direction.right),
            ('q0', None): ('qr', None, Direction.left),
            ('q1', 'a'): ('qr', 'a', Direction.left),
            ('q1', None): ('qa', None, Direction.left),
        }

    with open_mock_file([
        'q0 a q0 a R',
        'q0 _ qr',
        'q1 a qr a L',
        'q1 _ qa _ L'
    ]) as file, pytest.raises(ParseError):
        parse_transition_table(file, {'q0', 'q1', 'qa', 'qr'}, {'a'})

    with open_mock_file([
        'q0 a q0 a R',
        'q0 _ qr _ L',
        'q0 a qr a L',
        'q1 _ qa _ L'
    ]) as file, pytest.raises(ParseError):
        parse_transition_table(file, {'q0', 'q1', 'qa', 'qr'}, {'a'})


def test_parse():
    file = open(os.path.join(FIXTURES_DIR, 'machine.txt'), 'r')
    machine = parse_turing_machine(file)

    assert machine.start_state == 'q0'
    assert machine.accept_state == 'qa'
    assert machine.reject_state == 'qr'

    assert machine.transition_fn('q0', 'a') == ('q0', 'a', Direction.right)
    assert machine.transition_fn('q1', None) == ('qa', 'b', Direction.left)
