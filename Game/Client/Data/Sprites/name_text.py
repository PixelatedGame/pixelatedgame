import pygame



from Game.Client.Data.Sprites.pixel_object import Pixel_Object

class Name_Text(Pixel_Object):
    """moves a clenched fist on the screen, following the mouse"""
    def __init__(self, attached_object):
        Pixel_Object.__init__(self)
        self.attached_object = attached_object
        self.char_name = self.attached_object.char_name
        font = pygame.font.Font(None, 30)
        self.image = font.render(self.attached_object.char_name,1, (10, 10, 10))
        self.rect = self.image.get_rect()

    def screen_update(self):
                self.rect.midbottom = self.attached_object.rect.midtop
        