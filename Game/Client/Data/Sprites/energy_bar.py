import pygame



from Game.Client.Data.Sprites.pixel_object import Pixel_Object

class Energy_Bar(Pixel_Object):
    """moves a clenched fist on the screen, following the mouse"""
    def __init__(self, attached_object):
        Pixel_Object.__init__(self)
        self.attached_object = attached_object
        bar = pygame.Surface((50, 10))
        bar_rect = bar.get_rect().copy()
        bar_rect.width = 5
        bar.fill(pygame.Color('red'), rect=None, special_flags=0)
        bar.fill(pygame.Color('green'), rect=bar_rect, special_flags=0)
        self.image = bar
        self.rect = self.image.get_rect()

    def screen_update(self):
                self.rect.midbottom = self.attached_object.rect.midtop
        