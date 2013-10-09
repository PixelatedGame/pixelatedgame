import pygame
import Game
from Game.Client.Data.Sprites.gui_object import gui_object
from Game.Client.Data.Sprites.pixel_object import Pixel_Object
from Game.Client.Data.Sprites.name_text import Name_Text
from Game.Client.Data.Sprites.energy_bar import Energy_Bar

class character_info(gui_object):
    def __init__(self):
        self.char_name = Game.Client.my_char.char_name
        self.draw_portrait()
        self.draw_name()
        #self.draw_energy_bar()
        
        
    def draw_portrait(self):
        self.portrait = gui_object("portrait")
        self.portrait.rect = (10, 10, 10, 10)
        
    def draw_name(self):
        font = pygame.font.Font(None, 30)
        self.name_text = font.render(self.char_name,1, (10, 10, 10))
        self.rect = self.image.get_rect()
        portrait_rect = self.portrait.image.get_rect()
        self.rect.top = portrait_rect.bottom
    
    def draw_energy_bar(self):
        Pixel_Object.__init__(self)
        bar = pygame.Surface((50, 10))
        bar_rect = bar.get_rect().copy()
        bar_rect.width = 5
        bar.fill(pygame.Color('red'), rect=None, special_flags=0)
        bar.fill(pygame.Color('green'), rect=bar_rect, special_flags=0)
        self.image = bar
        self.rect = pygame.Rect(50, 50, 50, 50)

        