import os
from typing import Optional

from turingmachine.parser import parse_turing_machine
from turingmachine.turing_machine import TuringMachine


def parse_solution(name: str) -> TuringMachine:
    path = os.path.join(os.path.dirname(__file__), '..', name)

    with open(path) as file:
        return parse_turing_machine(file)


def assert_machine(machine: TuringMachine, input_string: str, should_accept: bool=True,
                   expected_output: Optional[str]=None):
    input_list = list(input_string)
    accepts, output_list = machine.run(input_list)

    if should_accept:
        assert accepts, "Machine did not accept input {}".format(input_string)
    else:
        assert not accepts, "Machine did accept input {}".format(input_string)

    if expected_output is not None:
        assert list(expected_output) == output_list


def assert_accepts(machine: TuringMachine, input_string: str):
    assert_machine(machine, input_string, should_accept=True)


def assert_rejects(machine: TuringMachine, input_string: str):
    assert_machine(machine, input_string, should_accept=False)
