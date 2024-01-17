import random
from rps_agent import RPSAgent


class TAAgent(RPSAgent):
    def setup(self):
        self.ROCK, self.SCISSORS, self.PAPER = 0, 1, 2
        self.actions = [self.ROCK, self.PAPER]

    def get_action(self):
        return random.choice(self.actions)

    def update(self):
        return None
