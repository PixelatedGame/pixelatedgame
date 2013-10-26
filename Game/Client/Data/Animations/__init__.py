import os
import pprint
from Game import Pixel_Utils
from Game.Client.Data.Animations.pixel_animation import Pixel_Animation

sprites_dir = r'data\Animations'
data_dir = os.path.join(sprites_dir)
animations_dict = {}

def init():
    for root, dirs, files in os.walk(data_dir):
        if files:
            object_class =  root.split('\\')[-2]
            print object_class
            object_name = root.split('\\')[-1]
            print object_name
            temp_animations_dict = {}
            for file in files:
                full_file_dir = os.path.join(sprites_dir, object_class, object_name, file)
                animation_class = file.split('.')[0]
                if animation_class in temp_animations_dict:
                    temp_animations_dict[animation_class].append(Pixel_Utils.load_image(full_file_dir))
                else:
                    temp_animations_dict[animation_class] = []
                    temp_animations_dict[animation_class].append(Pixel_Utils.load_image(full_file_dir))
            for k in temp_animations_dict.keys():
                animations_dict[k] = Pixel_Animation(k, object_name, temp_animations_dict[k])
                
            pp = pprint.PrettyPrinter(indent=4)
            pp.pprint(animations_dict)
              
    
# def add_object(object_name, object):
#     object_dict[object_name] = object
#     
# def get_object(object_name):
#     return object_dict[object_name]            
#         
# def add_sprite(sprite_name, group_name):
#     
#     new_sprite = Pixel_Sprite(sprite_name,group_name)
#     sprite_shortName = sprite_name.split('.', 1)[0]
#     sprite_dict[sprite_shortName] = new_sprite
    
def get_animation(sprite_name):
    return animations_dict[sprite_name]

def get_animations(sprite_name):
    temp_dict = {}
    for key in animations_dict:
        if sprite_name in key:
            temp_dict[key] = animations_dict[key]
    return temp_dict

# def create_sprite_group(group_name):
#     group_dict[group_name] = pygame.sprite.LayeredDirty()



# class Charachter_Sprites():
#     def __init__(self):
#         self.s_image, self.s_rect = pixelutils.load_image('straight.bmp', -1)
#         self.b_image, self.b_rect = pixelutils.load_image('back.bmp', -1)
#         self.image = self.s_image
#         screen = pygame.display.get_surface()
#         self.area = screen.get_rect()

if __name__ == '__main__': init()

