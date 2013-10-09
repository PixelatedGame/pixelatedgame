from Game.Client.Data import Sprites
from Game.Client.Data.Sprites.pixel_sprite import Pixel_Sprite
import pygame
from Game.Client.Data.Sprites import game_group

class Pixel_Object(pygame.sprite.DirtySprite):
    def __init__(self, internal_name = None):
        pygame.sprite.DirtySprite.__init__(self)
        self.internal_name = internal_name
        screen = pygame.display.get_surface()
        self.area = screen.get_rect()
        if internal_name is not None:
            self.sprite_dict = Sprites.get_sprites(self.internal_name)
        game_group.add(self)
        self.dirty =2
        
    def get_self_sprite(self,modifier = None):
        if modifier == None:
            return self.sprite_dict[self.internal_name]
        else:
            return self.sprite_dict[self.internal_name + "_" + modifier]
        