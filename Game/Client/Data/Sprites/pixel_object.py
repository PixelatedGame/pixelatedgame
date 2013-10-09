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
    
    def update(self):
        self.screen_update()
        self.check_bounds()
        self.check_collision()
    
    
    def screen_update(self):
        pass
    
    def check_bounds(self):
        pass
    
    def check_collision(self):
        pass   
        
    def get_self_sprite(self,modifier = None):
        if modifier == None:
            return self.sprite_dict[self.internal_name]
        else:
            return self.sprite_dict[self.internal_name + "_" + modifier]
        
    def destory(self):
        game_group.remove(self)