from state_factory import StateFactory


def possible_next_states(pos, state, states):
    next_states = []
    positions = [pos for pos, state in states.items()]

    for action in state.actions:
        next_position = tuple(map(sum, zip(pos, action.value)))
        if next_position in positions:
            next_states.append(states[next_position])

    return next_states


class ValueIterator:

    def __init__(self, world, reward):
        self.__world = world
        self.__reward = reward
        self.pos_states = {}

        state_factory = StateFactory(self.__world, self.__reward)
        for title in self.__world.tiles:
            self.pos_states[title] = state_factory.create_state(title)

        self.fixed_titles_pos = [pos for pos, state in world.fixed_tiles.items()]

    def iter(self):
        for pos, state in self.pos_states.items():
            max_util_of_next_state = max(
                [next_state.utility for next_state in possible_next_states(pos, state, self.pos_states)], default=0.0)
            state.utility = round(state.reward + max_util_of_next_state,4)
