import Data
import Gui
import Network
import pygame

from Game.Client.Data import Sounds

import random
from Game import Pixel_Utils
import time
import Game
from Game.Client.Data.Sprites.Firing_Character import Firing_Character
from Game.Client.Gui.Hud import hud



gameclock = None
sounds = None
clientconnection = None
my_char = None
characters = []

def init():
    
    Game.Client.gameclock = pygame.time.Clock()
#sounds = Sounds()
    Game.Client.clientconnection = Network.clientconnection()
    Game.Client.sounds = Sounds.Game_Sounds()
    Game.Client.Data.Sprites.init()
    init_my_char()
    init_charachters()
    update_thread = Pixel_Utils.thread_func(update_charachters_thread)
    update_thread.start()
    Game.Client.hud = hud()
    
def init_my_char():
        random_name = ''.join(random.choice('abcde') for x in range(3))
        Game.Client.my_char = Firing_Character("main", "Stavi-" + random_name)
        clientconnection.update_player(my_char.data)
        
def update_char(Character):
    Game.Client.clientconnection.update_player(Character.data)
    

def init_charachters():
    remote_charachters_data = clientconnection.get_characters()
    for remote_character_data in remote_charachters_data:
        
        if remote_character_data.char_name == my_char.char_name:
            continue
        new_char = Firing_Character("main",remote_character_data.char_name)
        new_char.set_data(remote_character_data)
        characters.append(new_char)
    
        
def update_charachters():
    remote_charachters_data = clientconnection.get_characters()
    for remote_character_data in remote_charachters_data:
        
        if remote_character_data.char_name == my_char.char_name:
            continue
        found = False
        for local_character in characters:
            
            if remote_character_data.char_name == local_character.data.char_name:
                local_character.set_data(remote_character_data)
                found = True
                break

        if not found:                    
            new_char = Firing_Character("main", remote_character_data.char_name)
            new_char.set_data(remote_character_data)
            characters.append(new_char)
        
        
def update_charachters_thread():
    while 1:
        time.sleep(0.005)
        update_charachters()
        
        
if __name__ == '__main__':
    init()