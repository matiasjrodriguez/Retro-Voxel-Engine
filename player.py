import numpy
import math

class Player:
    def __init__(self):
        self.pos = numpy.array([0, 0], dtype=float)
        self.angle = math.pi / 4
        self.height = 270
        self.pitch = 40
        self.angle_vel = 0.01
        self.vel = 3
        