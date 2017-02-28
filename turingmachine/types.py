from enum import Enum
from typing import Callable, Tuple, Dict, Optional


class Direction(Enum):
    left = 1
    right = 2

# State of a Turing machine
State = str

# Letter of an alphabet
AlphabetLetter = str

# Letter on a tape
TapeLetter = Optional[str]

# Transition table that translates current state and tape letter to next state, tape letter and direction
TransitionTable = Dict[Tuple[State, TapeLetter], Tuple[State, TapeLetter, Direction]]

# Transition function that translates current state and tape letter to next state, tape letter and direction
TransitionFunction = Callable[[State, TapeLetter], Tuple[State, TapeLetter, Direction]]
