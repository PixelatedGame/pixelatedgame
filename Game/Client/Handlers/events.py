import Game
from pygame.locals import * #@UnusedWildImport

def eventHandler(event):
    if event.type == QUIT:
                    return
    elif event.type == KEYDOWN and event.key == K_ESCAPE:
        return
    elif event.type == MOUSEBUTTONDOWN:
        if Game.Client.fist.punch(Game.Client.my_char):
            Game.Client.sounds.punch_sound.play() #punch
            Game.Client.my_char.punched()
        else:
            Game.Client.sounds.whiff_sound.play() #miss
    elif event.type is MOUSEBUTTONUP:
        Game.Client.fist.unpunch()
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