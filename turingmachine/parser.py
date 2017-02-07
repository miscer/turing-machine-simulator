from typing import Tuple, TextIO, Set

from turingmachine.transition import create_transition_fn
from turingmachine.turing_machine import TuringMachine
from turingmachine.types import Direction, TapeLetter, State, AlphabetLetter, TransitionTable


class ParseError(Exception):
    pass


def parse_direction(direction: str) -> Direction:
    if direction == 'L':
        return Direction.left
    elif direction == 'R':
        return Direction.right
    else:
        raise ParseError('Invalid direction: {}'.format(direction))


def parse_letter(letter: str, alphabet: Set[AlphabetLetter]) -> TapeLetter:
    if letter == '_':
        return None
    elif letter in alphabet:
        return letter
    else:
        raise ParseError('Invalid letter: {}'.format(letter))


def parse_states(file: TextIO) -> Tuple[State, State, State, Set[State]]:
    accept_state = None
    reject_state = None
    start_state = None
    all_states = set()

    try:
        line = file.readline()
        header, states_count_string = line.split()
    except ValueError:
        raise ParseError('Invalid states header format: {}'.format(line))

    try:
        states_count = int(states_count_string)
    except ValueError:
        raise ParseError('Invalid number of states: {}'.format(states_count_string))

    if header != 'states':
        raise ParseError('Expected states header, got {}'.format(header))

    if states_count < 2:
        raise ParseError('The machine has to have at least 2 states')

    for _ in range(states_count):
        try:
            state, *accept_reject = file.readline().split()
        except ValueError:
            raise ParseError('Invalid state row')

        if state not in all_states:
            all_states.add(state)
        else:
            raise ParseError('Duplicate state: {}'.format(state))

        if start_state is None:
            start_state = state

        if accept_reject == ['+']:
            if accept_state is None:
                accept_state = state
            else:
                raise ParseError('Multiple accept states: {}'.format(state))
        elif accept_reject == ['-']:
            if reject_state is None:
                reject_state = state
            else:
                raise ParseError('Multiple reject states: {}'.format(state))
        elif accept_reject:
            raise ParseError("Invalid state modifier: {}".format(accept_reject))

    if accept_state is None:
        raise ParseError("Missing accept state")

    if reject_state is None:
        raise ParseError("Missing reject state")

    return accept_state, reject_state, start_state, all_states


def parse_alphabet(file: TextIO) -> Set[AlphabetLetter]:
    alphabet = set()

    try:
        line = file.readline()
        header, alphabet_size_string, *alphabet_letters = line.split()
    except ValueError:
        raise ParseError('Invalid alphabet line: {}'.format(line))

    try:
        alphabet_size = int(alphabet_size_string)
    except ValueError:
        raise ParseError('Invalid alphabet size: {}'.format(alphabet_size_string))

    if header != 'alphabet':
        raise ParseError('Expected alphabet header, got {}'.format(header))

    if alphabet_size < 1 or alphabet_size != len(alphabet_letters):
        raise ParseError('Invalid alphabet size: {}'.format(alphabet_size))

    alphabet.update(alphabet_letters)

    if len(alphabet) != len(alphabet_letters):
        raise ParseError('Duplicate letters in the alphabet')

    return alphabet


def parse_transition_table(file: TextIO, states: Set[State], alphabet: Set[AlphabetLetter]) -> TransitionTable:
    transition_table = {}
    table_rows_count = (len(states) - 2) * (len(alphabet) + 1)

    for _ in range(table_rows_count):
        try:
            line = file.readline()
            in_state, in_letter, out_state, out_letter, direction = line.split()
        except ValueError:
            raise ParseError('Invalid transition table row: {}'.format(line))

        table_key = (in_state, parse_letter(in_letter, alphabet))
        table_value = (out_state, parse_letter(out_letter, alphabet), parse_direction(direction))

        if table_key not in transition_table:
            transition_table[table_key] = table_value
        else:
            raise ParseError('Duplicate transition table row: {}, {}'.format(in_state, in_letter))

    return transition_table


def parse_turing_machine(file: TextIO) -> TuringMachine:
    accept_state, reject_state, start_state, all_states = parse_states(file)
    alphabet = parse_alphabet(file)
    transition_table = parse_transition_table(file, all_states, alphabet)
    transition_fn = create_transition_fn(transition_table)

    return TuringMachine(start_state, accept_state, reject_state, transition_fn)
