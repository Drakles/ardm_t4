from value_iterator import ValueIterator
from world import World

if __name__ == '__main__':
    world = World(4,3, [(1, 1)], {(3, 2): 1.0, (3, 1): -1.0})
    value_iter = ValueIterator(world, -0.04)

    for i in range(100):
        value_iter.iter()

    print(value_iter.pos_states)
