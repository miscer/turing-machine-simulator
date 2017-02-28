import os
from typing import List, Tuple

from turingmachine.head import Head
from turingmachine.tape import Tape
from turingmachine.types import AlphabetLetter, State, TransitionFunction, TapeLetter

_debug = "TM_DEBUG" in os.environ

class TuringMachine:
    """
    Represents a Turing machine that has a transition function and the start, accept and reject states.
    Simulates a Turing machine on some input.
    """
    def __init__(self,
                 start_state: State,
                 accept_state: State,
                 reject_state: State,
                 transition_fn: TransitionFunction) -> None:
        """
        Initialises a new Turing machine with the specified parameters
        :param start_state: Start state for the machine
        :param accept_state: Accept state for the machine
        :param reject_state: Reject state for the machine
        :param transition_fn: Transition function for the machine
        """
        self.start_state = start_state
        self.accept_state = accept_state
        self.reject_state = reject_state
        self.transition_fn = transition_fn

    def run(self, input_word: List[AlphabetLetter]) -> Tuple[bool, List[TapeLetter]]:
        """
        Simulates a Turing machine with the given input on the tape.

        Debug mode can be enabled by setting the TM_DEBUG environment variable. In debug mode the machine will
        print out the tape, head position and current state as it runs.

        :param input_word: Initial tape input
        :return: Whether the machine has accepted the input, tape contents after the machine stops
        """
        head = Head()
        tape = Tape(input_word)
        current_state = self.start_state

        while current_state not in [self.accept_state, self.reject_state]:
            if _debug:
                tape_string = str(tape)

                print(
                    tape_string[:head.position],
                    current_state,
                    tape_string[head.position:]
                )

            read_letter = tape.read(head.position)
            next_state, written_letter, direction = self.transition_fn(current_state, read_letter)

            tape.write(head.position, written_letter)
            head.move(direction)

            current_state = next_state

        return current_state == self.accept_state, tape.list()
