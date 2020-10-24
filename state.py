class State:

    def __init__(self, reward, actions):
        self.reward = reward
        self.actions = actions
        self.utility = 0.0

    def __str__(self):
        return 'utility:' + str(self.utility) + ' reward: ' + str(self.reward) + ' actions: ' + str(self.actions)
