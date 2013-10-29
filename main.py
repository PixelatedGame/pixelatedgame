#/usr/bin/env python

#Import Modules
import pygame
import Game
from pygame.locals import * #@UnusedWildImport
from Game.Client.Gui.background import Background
from Game.Client.Data.Sprites.fire import Fire
from Game.Client.Gui.pointer import Pointer
from Game.Client.Data.Sprites import game_group
import sys




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
#     pygame.key.set_repeat(1, 10)
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
    

    UP = 'up'
    DOWN = 'down'
    LEFT = 'left'
    RIGHT = 'right'
    running = moveUp = moveDown = moveLeft = moveRight = False
    
    currentFocus = "main"
    

#Main Loop
    while 1:
        screen.blit(current_background, (0, 0))
        for event in pygame.event.get(): # event handling loop
     
            # handle ending the program
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
            
     
#         if moveUp or moveDown or moveLeft or moveRight:
#             # draw the correct walking/running sprite from the animation object
#             if running:
#                 if direction == UP:
#                     animObjs['back_run'].blit(windowSurface, (x, y))
#                 elif direction == DOWN:
#                     animObjs['front_run'].blit(windowSurface, (x, y))
#                 elif direction == LEFT:
#                     animObjs['left_run'].blit(windowSurface, (x, y))
#                 elif direction == RIGHT:
#                     animObjs['right_run'].blit(windowSurface, (x, y))
#             else:
#                 # walking
#                 if direction == UP:
#                     animObjs['back_walk'].blit(windowSurface, (x, y))
#                 elif direction == DOWN:
#                     animObjs['front_walk'].blit(windowSurface, (x, y))
#                 elif direction == LEFT:
#                     animObjs['left_walk'].blit(windowSurface, (x, y))
#                 elif direction == RIGHT:
#                     animObjs['right_walk'].blit(windowSurface, (x, y))
#      
#      
#             # actually move the position of the player
#             if running:
#                 rate = RUNRATE
#             else:
#                 rate = WALKRATE
#      
#             if moveUp:
#                 y -= rate
#             if moveDown:
#                 y += rate
#             if moveLeft:
#                 x -= rate
#             if moveRight:
#                 x += rate
#      
#         else:
#             # standing still
#             moveConductor.stop() # calling stop() while the animation objects are already stopped is okay; in that case stop() is a no-op
#             if direction == UP:
#                 windowSurface.blit(back_standing, (x, y))
#             elif direction == DOWN:
#                 windowSurface.blit(front_standing, (x, y))
#             elif direction == LEFT:
#                 windowSurface.blit(left_standing, (x, y))
#             elif direction == RIGHT:
#                 windowSurface.blit(right_standing, (x, y))
#      
#         # make sure the player does move off the screen
#         if x < 0:
#             x = 0
#         if x > WINDOWWIDTH - playerWidth:
#             x = WINDOWWIDTH - playerWidth
#         if y < 0:
#             y = 0
#         if y > WINDOWHEIGHT - playerHeight:
#             y = WINDOWHEIGHT - playerHeight
#         windowSurface.blit(instructionSurf, instructionRect)
#         pygame.display.update()
         
        
        
        
        
        
        
        
        Game.Client.gameclock.tick(60)  # @UndefinedVariable
        
    
        
    #Handle Input Events
    
         
        
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == KEYDOWN and event.key == K_ESCAPE:
                pygame.quit()
                sys.exit()
            elif event.type == MOUSEBUTTONDOWN:
                pass
            elif event.type is MOUSEBUTTONUP:
                pass
            
            if currentFocus == "main":
                if event.type == KEYDOWN and event.key == K_LEFT:
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
            elif currentFocus == "chat":
                Game.Client.hud.chatInput(event)
                
            if event.type == KEYDOWN and event.key == K_t: # Set focus to chat
                currentFocus = "chat"
            elif event.type == KEYDOWN and event.key == K_RETURN: # Return focus to main
                currentFocus = "main"
            
        
        
        game_group.update()
        game_group.draw(screen)
        pygame.display.flip()
        

    #Draw Everything
        

#Game Over


#this calls the 'main' function when this script is executed
if __name__ == '__main__': main()