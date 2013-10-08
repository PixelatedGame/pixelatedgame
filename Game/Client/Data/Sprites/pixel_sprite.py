import pygame
import os
import Game
from Game import Pixel_Utils



class Pixel_Sprite(pygame.sprite.DirtySprite):
    def __init__(self, name,group_name):
        pygame.sprite.DirtySprite.__init__(self)
        self.name = name
        self.path = os.path.join(Game.Client.Data.Sprites.sprites_dir, group_name, name)
        self.image, self.rect = Pixel_Utils.load_image(self.path, -1)
        self.add(Game.Client.Data.Sprites.group_dict[group_name])
        self.dirty = 2