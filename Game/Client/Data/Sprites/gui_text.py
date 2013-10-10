import pygame
from Game.Client.Data.Sprites.pixel_object import Pixel_Object


class gui_text(Pixel_Object):
    def __init__(self, text, position, fontColor = (10, 10, 10), fontSize = 30):
        Pixel_Object.__init__(self)
        font = pygame.font.Font(None, fontSize)
        self.image = font.render(text,1, fontColor)
        self.rect = self.image.get_rect()
        self.rect.topleft = position