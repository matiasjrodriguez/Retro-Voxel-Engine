import numpy
import math

class VoxelRender:
    def __init__(self, app):
        self.app = app
        self.fov = math.pi / 3
        self.h_fov = self.fov / 2
        self.num_rays = app.width
        self.delta_angle = self.fov / self.num_rays
        self.ray_distance = 2000
        self.scale_height = 620
        self.screen_array = numpy.full((app.width, app.height, 3), (0, 0, 0))
        