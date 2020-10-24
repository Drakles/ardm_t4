class State:

    def __init__(self, reward, actions, utility=0.0):
        self.reward = reward
        self.actions = actions
        self.utility = utility

    def __str__(self):
        return 'utility:' + str(self.utility) + ' reward: ' + str(self.reward) + ' actions: ' + str(self.actions)
