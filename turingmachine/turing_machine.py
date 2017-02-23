import os
from typing import List, Tuple

from turingmachine.head import Head
from turingmachine.tape import Tape
from turingmachine.types import AlphabetLetter, State, TransitionFunction, TapeLetter

_debug = "TM_DEBUG" in os.environ

class TuringMachine:
    def __init__(self,
                 start_state: State,
                 accept_state: State,
                 reject_state: State,
                 transition_fn: TransitionFunction) -> None:
        self.start_state = start_state
        self.accept_state = accept_state
        self.reject_state = reject_state
        self.transition_fn = transition_fn

    def run(self, input_word: List[AlphabetLetter]) -> Tuple[bool, List[TapeLetter]]:
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
