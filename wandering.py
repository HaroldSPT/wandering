import random
from re import X

class Wandering:

    def __init__(self, name, x=0, y=0):
        self.name = name
        self.x= x
        self.y= y

    def position(self):
        return (self.x, self.y)

    def distance_origin(self):
        return (self.x**2, self.y**2)**0.5

class CommonWandering(Wandering):

    def __init__(self, name):
        super().__init__(name)

    def walk(self):
        dx, dy = random.choice([(-6, 2), (5,-2), (2, 3), (1, 7)])
        self.x += dx
        self.y += dy
        return [dx, dy]

        