import pygame
from pygame.locals import * #@UnusedWildImport

from Game import Pixel_Utils


class Background():
    def __init__(self,screen):
        self.current_background = pygame.Surface(screen.get_size())
        self.current_background = self.current_background.convert()
        self.get_default_background()

    def get_default_background(self):
        self.image, self.rect = Pixel_Utils.load_image(r'data\Sprites\Levels\TEST5B.bmp', -1)
        self.current_background.blit(self.image, (0,0) )
        return self.current_background