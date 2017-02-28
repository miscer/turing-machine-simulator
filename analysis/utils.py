import os
from itertools import islice
from typing import List, Iterable, Tuple, Iterator
from unittest.mock import patch

from turingmachine.parser import parse_turing_machine
from turingmachine.turing_machine import TuringMachine


def parse_solution(name: str) -> TuringMachine:
    """
    Opens a solution file and parses the Turing machine defined in it.

    :param name: Name of the solution file
    :return: Parsed Turing machine
    """
    path = os.path.join(os.path.dirname(__file__), '../solutions', name)

    with open(path) as file:
        return parse_turing_machine(file)


def generate_input_table(input_generators: List[Iterator[str]], size: int) -> Iterable[Tuple[str, ...]]:
    """
    Given a list of iterators that produce strings, takes the specified number of strings from each of them
    and returns a list containing tuples with a single element from each of the iterators.

    Example:

    generate_input_table([['a', 'aa', 'aaa'], ['b', 'bb', 'bbb']], 2) -> [('a', 'b'), ('aa', 'bb')]

    :param input_generators: List of input generators
    :param size: Number of inputs to generate
    :return: List of tuples with inputs
    """
    return islice(zip(*input_generators), size)


def count_transitions(machine: TuringMachine, input_generators: List[Iterator[str]], size: int):
    """
    Runs the Turing machine on each of the inputs returned by the generate_input_table function called
    with the specified input_generators and size. Counts the number of transitions taken for each run.
    Prints CSV output to STDOUT.

    :param machine: Machine to be used for counting
    :param input_generators: List of input generators, used for generate_input_table
    :param size: Number of inputs to generate, used for generate_input_table
    """

    # print CSV header
    header = ['n'] + ['input {}'.format(n) for n in range(len(input_generators))]
    print(','.join(header))

    # generate the input table
    input_table = generate_input_table(input_generators, size)

    # patch the transition function of the machine, so that we can count the number of times it was called
    with patch.object(machine, 'transition_fn', wraps=machine.transition_fn) as transition_mock:
        for n, row in enumerate(input_table):
            line = [n]

            for column in row:
                # run the machine on the input from the table
                machine.run(list(column))

                # store the number of transitions taken and reset it
                line.append(transition_mock.call_count)
                transition_mock.reset_mock()

            # print CSV row
            print(','.join(map(str, line)))
