from Classbase import Shooter
import random


class Novice(Shooter):
    def __init__(self, name, age, experience, probability):
        Shooter.__init__(self, name, age, experience)
        self.probability = probability

    def fire(self):
        self.probability = 0.01 * self.experience > random.uniform(0, 2)
        return self.probability
