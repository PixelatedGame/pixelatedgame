#/usr/bin/env python

#Import Modules
import pygame
import Game
from pygame.locals import * #@UnusedWildImport
from Game.Client.Gui.background import Background
from Game.Client.Data.Sprites.fire import Fire
from Game.Client.Gui.pointer import Pointer
from Game.Client.Data.Sprites import game_group



if not pygame.font: print 'Warning, fonts disabled'
if not pygame.mixer: print 'Warning, sound disabled'


#classes for our game objects





def main():
    """this function is called when the program starts.
       it initializes everything it needs, then runs in
       a loop until the function returns."""
#Initialize Everything

    
    
    pygame.init()
    screen = pygame.display.set_mode((640, 480))
    
    pygame.display.set_caption('Pyxelated')
    pygame.mouse.set_visible(0)
    pygame.key.set_repeat(1, 10)
    Game.Client.init()
    
    background = Background(screen)
    current_background = background.get_default_background()
    
    
#Put Text On The Background, Centered
    if pygame.font:
        font = pygame.font.Font(None, 48)
        text = font.render("Pixelated alpha 0.2", 1, (10, 10, 10))
        textpos = text.get_rect(centerx=current_background.get_width()/2)
        current_background.blit(text, textpos)

#Display The Background
    screen.blit(current_background, (0, 0))
    pygame.display.flip()

#Prepare Game Objects
    
    
    

# SOCK_DGRAM is the socket type to use for UDP sockets

    fist = Pointer("fist")
    
    

#Main Loop
    while 1:
        Game.Client.gameclock.tick(60)  # @UndefinedVariable
        
    
        
    #Handle Input Events
        for event in pygame.event.get():
            if event.type == QUIT:
                return
            elif event.type == KEYDOWN and event.key == K_ESCAPE:
                return
            elif event.type == MOUSEBUTTONDOWN:
                pass
            elif event.type is MOUSEBUTTONUP:
                pass
            elif event.type == KEYDOWN and event.key == K_LEFT:
                Game.Client.my_char._move((-10,0))
                
            elif event.type == KEYDOWN and event.key == K_RIGHT:
                Game.Client.my_char._move((10,0))
                
            elif event.type == KEYDOWN and event.key == K_UP:
                Game.Client.my_char.image = Game.Client.my_char.back_sprite.image
                Game.Client.my_char._move((0,-10))
                
            elif event.type == KEYDOWN and event.key == K_DOWN:
                Game.Client.my_char.image = Game.Client.my_char.back_sprite.image
                Game.Client.my_char._move((0,10))
            elif event.type == KEYDOWN and event.key == K_SPACE:
                Game.Client.my_char._fire()
                
        
        screen.blit(current_background, (0, 0))
        game_group.update()
        game_group.draw(screen)
        pygame.display.flip()
        

    #Draw Everything
        

#Game Over


#this calls the 'main' function when this script is executed
if __name__ == '__main__': main()