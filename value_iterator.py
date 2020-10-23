from state_factory import StateFactory


def possible_next_states(pos, state, states):
    next_states = []
    positions = [pos for pos, state in states]

    for action in state.actions:
        next_position = tuple(map(sum, zip(pos, action)))
        if next_position in positions:
            next_states.append(states[next_position])

    return next_states


class ValueIterator:

    def __init__(self, world, reward):
        self.__world = world
        self.__reward = reward
        self.pos_states = {}

    def iter(self):
        state_factory = StateFactory(self.__world, self.__reward)

        for title in self.__world.titles:
            self.pos_states[title] = state_factory.create_state(title)

        for pos, state in self.pos_states.items():
            state.utility = self.__reward + max(
                [next_state.utility for pos, next_state in possible_next_states(pos, state, self.pos_states)])
