from typing import Tuple, TextIO, Set

from turingmachine.transition import create_transition_fn
from turingmachine.turing_machine import TuringMachine
from turingmachine.types import Direction, TapeLetter, State, AlphabetLetter, TransitionTable


def parse_direction(direction: str) -> Direction:
    if direction == 'L':
        return Direction.left
    elif direction == 'R':
        return Direction.right


def parse_letter(letter: str) -> TapeLetter:
    if letter == '_':
        return None
    else:
        return letter


def parse_states(file: TextIO) -> Tuple[State, State, State, Set[State]]:
    accept_state = None
    reject_state = None
    start_state = None
    all_states = set()

    _, states_count = file.readline().split()

    for _ in range(int(states_count)):
        state, *accept_reject = file.readline().split()
        all_states.add(state)

        if start_state is None:
            start_state = state

        if accept_reject == ['+']:
            accept_state = state
        elif accept_reject == ['-']:
            reject_state = state

    return accept_state, reject_state, start_state, all_states


def parse_alphabet(file: TextIO) -> Set[AlphabetLetter]:
    alphabet = set()

    _, _, *alphabet_letters = file.readline().split()
    alphabet.update(alphabet_letters)

    return alphabet


def parse_transition_table(file: TextIO, states: Set[State], alphabet: Set[AlphabetLetter]) -> TransitionTable:
    transition_table = {}
    table_rows_count = (len(states) - 2) * (len(alphabet) + 1)

    for _ in range(table_rows_count):
        in_state, in_letter, out_state, out_letter, direction = file.readline().split()

        transition_table[(
            in_state,
            parse_letter(in_letter)
        )] = (
            out_state,
            parse_letter(out_letter),
            parse_direction(direction)
        )

    return transition_table


def parse_turing_machine(file: TextIO) -> TuringMachine:
    accept_state, reject_state, start_state, all_states = parse_states(file)
    alphabet = parse_alphabet(file)
    transition_table = parse_transition_table(file, all_states, alphabet)
    transition_fn = create_transition_fn(transition_table)

    return TuringMachine(start_state, accept_state, reject_state, transition_fn)
