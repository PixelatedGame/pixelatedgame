import pygame
from Game.Client.Data.Sprites.pixel_object import Pixel_Object
from Game.Client.Modules import eztext


class gui_input(Pixel_Object):
    def __init__(self):
        Pixel_Object.__init__(self)
        self.image = eztext.Input(x = 20, y = 20, maxlength=45, color=(255,0,0), prompt='type here: ')
        #self.image = font.render(text,1, fontColor)
        self.rect = self.image.get_rect()