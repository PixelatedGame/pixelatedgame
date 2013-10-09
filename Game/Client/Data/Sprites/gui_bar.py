import pygame
from Game.Client.Data.Sprites.pixel_object import Pixel_Object


class gui_bar(Pixel_Object):
    def __init__(self, position):
        Pixel_Object.__init__(self)
        bar = pygame.Surface((50, 10))
        bar_rect = bar.get_rect().copy()
        bar_rect.width = 5
        bar.fill(pygame.Color('red'), rect=None, special_flags=0)
        bar.fill(pygame.Color('green'), rect=bar_rect, special_flags=0)
        self.image = bar
        self.rect = self.image.get_rect()
        self.rect.topleft = position