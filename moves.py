from actions import Action


def all_moves(pos):
    return {
            (pos[0], pos[1] + 1): Action.UP,
            (pos[0] + 1, pos[1]): Action.RIGHT,
            (pos[0], pos[1] - 1): Action.DOWN,
            (pos[0] - 1, pos[1]): Action.LEFT
            }
