import os

from turingmachine.parser import parse_turing_machine
from turingmachine.types import Direction

FIXTURES_DIR = os.path.join(os.path.dirname(__file__), 'fixtures')

def test_parse():
    file = open(os.path.join(FIXTURES_DIR, 'machine.txt'), 'r')
    machine = parse_turing_machine(file)

    assert machine.start_state == 'q0'
    assert machine.accept_state == 'qa'
    assert machine.reject_state == 'qr'

    assert machine.transition_fn('q0', 'a') == ('q0', 'a', Direction.right)
    assert machine.transition_fn('q1', None) == ('qa', 'b', Direction.left)
