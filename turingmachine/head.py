from turingmachine.types import Direction


class Head:
    def __init__(self):
        self.position = 0

    def move(self, direction: Direction) -> None:
        if direction == Direction.left and self.position > 0:
            self.position -= 1
        elif direction == Direction.right:
            self.position += 1