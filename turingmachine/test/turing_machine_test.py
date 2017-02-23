from turingmachine.transition import create_transition_fn
from turingmachine.turing_machine import TuringMachine
from turingmachine.types import Direction


def test_turing_machine():
    table = {
        ('q0', 'a'): ('q0', 'a', Direction.right),
        ('q0', 'b'): ('q1', 'b', Direction.right),
        ('q0', None): ('qr', None, Direction.left),
        ('q1', 'a'): ('qr', 'a', Direction.left),
        ('q1', 'b'): ('qr', 'a', Direction.left),
        ('q1', None): ('qa', 'b', Direction.left)
    }

    transition_fn = create_transition_fn(table)
    machine = TuringMachine('q0', 'qa', 'qr', transition_fn)

    assert (True, list('aabb')) == machine.run(list('aab'))
    assert (False, list('aba')) == machine.run(list('aba'))
