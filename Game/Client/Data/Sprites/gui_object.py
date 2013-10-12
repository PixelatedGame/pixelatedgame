from Game.Client.Data.Sprites.pixel_object import Pixel_Object
import pygame


class gui_object(Pixel_Object):
    def __init__(self, internal_name = None):
        Pixel_Object.__init__(self, internal_name)
        self.sprite = self.get_self_sprite()
        self.rect = self.sprite.rect
        self.image = self.sprite.image