from non_determ_value_iterator import NonDeterministicValueIterator
from value_iterator import ValueIterator
from world import World

if __name__ == '__main__':
    world = World(4, 3, [(1, 1)], {(3, 2): 1.0, (3, 1.0): -1.0})
    value_iter = ValueIterator(world, -0.04)

    print('deterministic iterator')
    for i in range(10):
        value_iter.iter()

    for pos, state in value_iter.pos_states.items():
        print(pos, state)

    non_deterministic = NonDeterministicValueIterator(world, -0.04)
    for i in range(10):
        non_deterministic.iter()

    print('non-deterministic iterator')

    for pos, state in non_deterministic.pos_states.items():
        print(pos, state)
