from turingmachine.head import Head
from turingmachine.types import Direction


def test_head_move():
    head = Head()

    assert head.position == 0

    head.move(Direction.left)
    assert head.position == 0

    head.move(Direction.right)
    assert head.position == 1

    head.move(Direction.left)
    assert head.position == 0