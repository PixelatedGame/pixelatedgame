import pygame
import Game
from Game.Client.Data.Sprites.gui_object import gui_object
from Game.Client.Data.Sprites.gui_text import gui_text
from Game.Client.Data.Sprites.gui_bar import gui_bar

class character_info(gui_object):
    def __init__(self):
        self.char_name = Game.Client.my_char.char_name
        self.draw_portrait()
        self.draw_name()
        self.draw_bar()
        
        
    def draw_portrait(self):
        self.portrait = gui_object("portrait")
        self.portrait.rect.topleft = (0, 0)
        
    def draw_name(self):
        self.name_text = gui_text(self.char_name, self.portrait.rect.bottomleft)
        
    def draw_bar(self):
        self.energy_bar = gui_bar(self.name_text.rect.bottomleft)

        