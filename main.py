from voxel_render import VoxelRender
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
        self.voxel_render = VoxelRender(self)
        
    def update(self):
        self.voxel_render.update()
        
    def draw(self):
        self.voxel_render.draw()
        pygame.display.flip()
        
    def run(self):
        run = True
        while run:
            self.update()
            self.draw()
                
            for i in pygame.event.get():
                if i.type == pygame.QUIT:
                    run = False
                    
            self.clock.tick(60)
            pygame.display.set_caption(f'FPS: {self.clock.get_fps()}')