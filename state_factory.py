from moves import all_moves
from state import State


class StateFactory:

    def __init__(self, world, reward):
        self.__reward = reward
        self.__world = world
        self.__world_fixed_tiles_pos = [pos for pos, reward in world.fixed_tiles.items()]

    def create_state(self, pos):
        if pos in self.__world.tiles:
            if pos in self.__world_fixed_tiles_pos:
                return State(self.__world.fixed_tiles[pos], [], self.__world.fixed_tiles[pos])

            possible_actions = []

            for next_position, action in all_moves(pos).items():
                if self.__world.tile_exist(next_position):
                    possible_actions.append(action)

            return State(self.__reward, possible_actions)
        else:
            raise Exception('position not in world exception')
