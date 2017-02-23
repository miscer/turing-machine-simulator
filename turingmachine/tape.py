from typing import List

from turingmachine.types import AlphabetLetter, TapeLetter


class Tape:
    def __init__(self, input_word: List[AlphabetLetter]) -> None:
        self.tape = dict(enumerate(input_word))

    def read(self, position: int) -> TapeLetter:
        self._check_position(position)
        return self.tape.get(position)

    def write(self, position: int, letter: TapeLetter):
        self._check_position(position)
        self.tape[position] = letter

    def _check_position(self, position: int) -> None:
        if position < 0:
            raise IndexError('Position {} is out of range'.format(position))

    def __str__(self) -> str:
        num_cells = len(self.tape)
        tape_string = str()

        for n in range(num_cells):
            tape_string += self.tape.get(n)

        return tape_string
