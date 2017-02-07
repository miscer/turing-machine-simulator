import pytest

from turingmachine.transition import create_transition_fn
from turingmachine.types import Direction


def test_create_transition_fn():
    table = {
        ('a', '1'): ('b', '2', Direction.left),
        ('a', '2'): ('a', '1', Direction.left),
        ('b', '1'): ('b', '1', Direction.left),
        ('b', '2'): ('b', '1', Direction.left)
    }

    transition_fn = create_transition_fn(table)

    assert transition_fn('a', '1') == ('b', '2', Direction.left)
    assert transition_fn('b', '2') == ('b', '1', Direction.left)

    with pytest.raises(ValueError):
        transition_fn('c', '1')
