from player import Player
import pygame

class App:
    def __init__(self):
        self.width = 800
        self.height = 450
        self.res = self.width, self.height
        self.screen = pygame.display.set_mode(self.res)
        self.clock = pygame.time.clock()
        self.player = Player()
        