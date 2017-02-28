import os
from typing import Optional

from turingmachine.parser import parse_turing_machine
from turingmachine.turing_machine import TuringMachine


def parse_solution(name: str) -> TuringMachine:
    """
    Opens a solution file and parses the Turing machine defined in it.

    :param name: Name of the solution file
    :return: Parsed Turing machine
    """
    path = os.path.join(os.path.dirname(__file__), '..', name)

    with open(path) as file:
        return parse_turing_machine(file)


def assert_machine(machine: TuringMachine, input_string: str, should_accept: bool=True,
                   expected_output: Optional[str]=None):
    """
    Runs the Turing machine and asserts that it accepted/rejected the input and optionally
    what the tape should look like after the machine has finished.

    :param machine: Machine to run
    :param input_string: Input for the machine
    :param should_accept: Whether the machine should accept
    :param expected_output: Expected contents of the tape
    """
    input_list = list(input_string)
    accepts, output_list = machine.run(input_list)

    if should_accept:
        assert accepts, "Machine did not accept input {}".format(input_string)
    else:
        assert not accepts, "Machine did accept input {}".format(input_string)

    if expected_output is not None:
        assert list(expected_output) == output_list


def assert_accepts(machine: TuringMachine, input_string: str):
    """
    Asserts that the machine accepts the input
    :param machine: Machine to run
    :param input_string: Input for the machine
    :return:
    """
    assert_machine(machine, input_string, should_accept=True)


def assert_rejects(machine: TuringMachine, input_string: str):
    """
    Asserts that the machine rejects the input
    :param machine: Machine to run
    :param input_string: Input for the machine
    :return:
    """
    assert_machine(machine, input_string, should_accept=False)
