import os
from itertools import islice
from typing import List, Iterable, Tuple, Iterator
from unittest.mock import patch

from turingmachine.parser import parse_turing_machine
from turingmachine.turing_machine import TuringMachine


def parse_solution(name: str) -> TuringMachine:
    path = os.path.join(os.path.dirname(__file__), '../solutions', name)

    with open(path) as file:
        return parse_turing_machine(file)


def generate_input_table(input_generators: List[Iterator[str]], size: int) -> Iterable[Tuple[str, ...]]:
    return islice(zip(*input_generators), size)


def count_transitions(machine: TuringMachine, input_generators: List[Iterator[str]], size: int):
    header = ['n'] + ['input {}'.format(n) for n in range(len(input_generators))]
    print(','.join(header))

    input_table = generate_input_table(input_generators, size)

    with patch.object(machine, 'transition_fn', wraps=machine.transition_fn) as transition_mock:
        for n, row in enumerate(input_table):
            line = [n]

            for column in row:
                machine.run(list(column))

                line.append(transition_mock.call_count)
                transition_mock.reset_mock()

            print(','.join(map(str, line)))