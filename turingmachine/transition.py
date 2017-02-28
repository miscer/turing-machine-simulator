from turingmachine.types import TransitionTable, TransitionFunction, State, TapeLetter


def create_transition_fn(transition_table: TransitionTable) -> TransitionFunction:
    """
    Converts a transition table into a transition function. The resulting function will
    use the table when looking up transitions.

    :param transition_table: Transition table to be used by the function
    :return: Transition function that will use the table
    """
    def transition_fn(state: State, letter: TapeLetter):
        table_key = (state, letter)

        if table_key in transition_table:
            return transition_table[table_key]
        else:
            raise ValueError("Transition {}, {} is invalid".format(state, letter))

    return transition_fn
