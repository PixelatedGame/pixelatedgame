import pygame
from Game.Client.Data.Sprites.abstract_object import Abstract_Object





class Pointer(Abstract_Object):
    def __init__(self, internal_name):
        Abstract_Object.__init__(self, internal_name)
        

    def screen_update(self):
        "move the fist based on the mouse position"
        pos = pygame.mouse.get_pos()
        self.rect.midtop = pos



