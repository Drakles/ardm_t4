from state_factory import StateFactory
from value_iterator import possible_next_states


class NonDeterministicValueIterator:

    def __init__(self, world, reward):
        self.__world = world
        self.__world_fixed_tiles_position = [pos for pos,reward in world.fixed_tiles.items()]
        self.__reward = reward
        self.pos_states = {}

        state_factory = StateFactory(self.__world, self.__reward)
        for tile in self.__world.tiles:
            self.pos_states[tile] = state_factory.create_state(tile)

        self.fixed_titles_pos = [pos for pos, state in world.fixed_tiles.items()]

    def iter(self):
        for pos, state in self.pos_states.items():
            if pos not in self.__world_fixed_tiles_position:
                max_util_of_next_state = max(
                    [next_state.utility for next_state in possible_next_states(pos, state, self.pos_states)], default=0.0)

                state.utility = round(state.reward + 0.9 * max_util_of_next_state + 0.1 * state.utility, 4)
