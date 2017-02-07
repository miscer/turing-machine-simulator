from enum import Enum
from typing import Callable, Tuple, Dict, Optional


class Direction(Enum):
    left = 1
    right = 2

State = str
AlphabetLetter = str
TapeLetter = Optional[str]

TransitionTable = Dict[Tuple[State, TapeLetter], Tuple[State, TapeLetter, Direction]]
TransitionFunction = Callable[[State, TapeLetter], Tuple[State, TapeLetter, Direction]]
