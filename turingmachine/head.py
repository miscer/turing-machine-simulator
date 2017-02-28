from turingmachine.types import Direction


class Head:
    """
    Represents the head of a Turing machine
    """

    def __init__(self):
        """
        Initialises the head at the starting position
        """
        self.position = 0

    def move(self, direction: Direction) -> None:
        """
        Moves the head in the specified direction. If the head is at the starting position
        and it is instructed to move left, it does not move.

        :param direction: Direction to move the head; either left or right
        """
        if direction == Direction.left and self.position > 0:
            self.position -= 1
        elif direction == Direction.right:
            self.position += 1