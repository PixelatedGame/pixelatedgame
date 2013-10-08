import pygame
import os
from Game.Client.Data.Sprites import pixel_sprite
from Game.Client.Data.Sprites.pixel_sprite import Pixel_Sprite
import Game

sprites_dir = 'c:\Data\sprites'
group_dict = {}
sprite_dict = {}
object_dict = {}
game_group = pygame.sprite.LayeredDirty() 


def init():

    data_dir = os.path.join(sprites_dir)
    files_in_dir = os.listdir(data_dir)
    for file_in_dir in files_in_dir:
        data_sub_dir =os.path.join(sprites_dir,file_in_dir)
        if os.path.isdir(data_sub_dir):
            files_data_sub_dir = os.listdir(data_sub_dir)
            create_sprite_group(file_in_dir)
            for file_data_sub_dir in files_data_sub_dir:
                add_sprite(file_data_sub_dir, file_in_dir)
              
    
def add_object(object_name, object):
    object_dict[object_name] = object
    
def get_object(object_name):
    return object_dict[object_name]            
        
def add_sprite(sprite_name, group_name):
    new_sprite = Pixel_Sprite(sprite_name,group_name)
    sprite_dict[sprite_name] = new_sprite
    
def get_sprite(sprite_name):
    return sprite_dict[sprite_name]

def get_sprites(sprite_name):
    temp_dict = {}
    for key in sprite_dict:
        if sprite_name in key:
            temp_dict[key] = sprite_dict[key]
    return temp_dict

def create_sprite_group(group_name):
    group_dict[group_name] = pygame.sprite.LayeredDirty()



# class Charachter_Sprites():
#     def __init__(self):
#         self.s_image, self.s_rect = pixelutils.load_image('straight.bmp', -1)
#         self.b_image, self.b_rect = pixelutils.load_image('back.bmp', -1)
#         self.image = self.s_image
#         screen = pygame.display.get_surface()
#         self.area = screen.get_rect()



