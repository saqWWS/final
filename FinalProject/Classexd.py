from Classbase import Shooter
import random


class Experienced(Shooter):
    def __init__(self, name, age, experience, probability):
        Shooter.__init__(self, name, age, experience)
        self.probability = probability

    def fire(self):
        self.probability = 0.05 * self.experience > random.uniform(0, 1.5)
        return self.probability
