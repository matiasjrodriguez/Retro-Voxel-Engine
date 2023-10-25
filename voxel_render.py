import pygame
import numpy
import math

height_map_img = pygame.image.load('img/height_map.jpg')
height_map = pygame.surfarray.array3d(height_map_img)

color_map_img = pygame.image.load('img/color_map.jpg')
color_map = pygame.surfarray.array3d(color_map_img)

map_height = len(height_map[0])
map_width = len(height_map)

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
        self.player = app.player
        