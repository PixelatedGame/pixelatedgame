import pygame
from Game.Client.Data.Sprites.pixel_object import Pixel_Object
import Game
from Game.Client.Data.Sprites.name_text import Name_Text
from Game.Client.Data.Sprites.energy_bar import Energy_Bar


class Character(Pixel_Object):
    def __init__(self, internal_name, char_name):
        Pixel_Object.__init__(self, internal_name)
        self.front_sprite = self.get_self_sprite("front")
        self.back_sprite = self.get_self_sprite("back")
        self.char_name = char_name
        self.rect = self.front_sprite.rect.copy()
        self.image = self.front_sprite.image
#         self.name_text = Name_Text(self)
        self.energy_bar = Energy_Bar(self)
        self.data = Charachter_Data(char_name, self.rect)
    
        
        
#         self.name_text = Name_Text(game,self.char_name)
#         self.rect = self.data.rect

    def init_name(self,char_name):
        pass
        
    def set_data(self,data):
        self.data = data
        self.rect = self.data.rect
        

    def update(self):
        self.rect = self.data.rect
        
        if self.data.dizzy:
            self._spin()
        else:
            self._walk()
            
        if self.data.up:
            self.image = self.front_sprite.image
        else:
            self.image = self.back_sprite.image
        

    def _walk(self):
        pass
        
    def _move(self, direction):
        self.data.move = direction
        if direction[0] > 0:
            self.data.right = True
        elif direction[0] < 0:
            self.data.right = False
        if direction[1] > 0:
            self.data.up = True
        elif direction[1] < 0:
            self.data.up = False
            
        old_rect = self.data.rect[1]
        newpos = self.data.rect.move(self.data.move)
        
        if newpos.left > 500:
            newpos.right = 0
        if newpos.right < 0:
            newpos.left  = 500
        self.data.rect = newpos
        
        Game.Client.update_char(self)
        
 
    def _spin(self):
        center = self.data.rect.center
        self.data.dizzy = self.data.dizzy + 12
        if self.data.dizzy >= 360:
            self.data.dizzy = 0
            self.image = self.original
        else:
            rotate = pygame.transform.rotate
            self.image = rotate(self.original, self.data.dizzy)
        self.data.rect = self.image.get_rect(center=center)

    def punched(self):
        if not self.data.dizzy:
            self.data.dizzy = 1
            self.original = self.image
            
class Charachter_Data():
    def __init__(self, char_name, rect):
        self.char_name = char_name
        self.rect = rect
        self.rect.topleft = 10, 10
        self.location = (0,0)
        self.move = (0,0)
        self.dizzy = 0
        self.up = True
        self.right = True 