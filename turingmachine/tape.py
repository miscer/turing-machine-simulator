from typing import List

from turingmachine.types import AlphabetLetter, TapeLetter


def tape_list_to_string(tape_list: List[TapeLetter]) -> str:
    """
    Converts the list of tape letters to a string. Empty cells are converted to _ characters.

    :param tape_list: List of tape letters
    :return: String with tape letters and blank spaces
    """
    tape_string = str()

    for letter in tape_list:
        if letter is not None:
            tape_string += letter
        else:
            tape_string += '_'

    return tape_string


class Tape:
    """
    Represents the tape of a Turing machine.
    """

    def __init__(self, input_word: List[AlphabetLetter]) -> None:
        """
        Initialises the tape with the specified word written on it.

        :param input_word: Word that should be on the tape initially
        """
        self.tape = dict(enumerate(input_word))

    def read(self, position: int) -> TapeLetter:
        """
        Reads a letter from the specified cell.

        :param position: Cell position, 0-indexed
        :return: Letter in the cell, or None if the cell is empty
        """
        self._check_position(position)
        return self.tape.get(position)

    def write(self, position: int, letter: TapeLetter):
        """
        Writes the letter to the specified cell.

        :param position: Cell position, 0-indexed
        :param letter: Letter to write, or None to clear the cell
        """
        self._check_position(position)
        self.tape[position] = letter

    def list(self) -> List[TapeLetter]:
        """
        Converts the tape to a list of letters. The list includes all cells that
        were written to, with Nones between them if there are empty cells between them.

        :return: List containing letters in tape cells
        """
        max_cell = max(self.tape.keys())
        return [self.tape.get(n) for n in range(max_cell + 1)]

    def _check_position(self, position: int) -> None:
        """
        Checks whether the position is valid.

        :param position: Position to check
        """
        if position < 0:
            raise IndexError('Position {} is out of range'.format(position))

    def __str__(self) -> str:
        """
        Converts the tape to a string using tape_list_to_string.

        :return: String with the tape contents
        """
        return tape_list_to_string(self.list())
