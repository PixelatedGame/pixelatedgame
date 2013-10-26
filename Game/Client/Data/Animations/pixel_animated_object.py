import pygame
from Game.Client.Data.Animations import pixel_animation
from Game.Client.Data import Animations
from Game.Client.Data.Sprites import game_group
from pygame.locals import * #@UnusedWildImport


class Pixel_Animated_Object(pygame.sprite.DirtySprite):
    def __init__(self, internal_name = None):
        pygame.sprite.DirtySprite.__init__(self)
        self.internal_name = internal_name
        screen = pygame.display.get_surface()
        self.area = screen.get_rect()
        if internal_name:
            self.animations_dict = Animations.get_animations(self.internal_name)
        game_group.add(self)
        self.dirty =2
        
        self.rect = self.front_sprite.rect.copy()
        self.image = self.front_sprite.image
        
        self.UP = 'up'
        self.DOWN = 'down'
        self.LEFT = 'left'
        self.RIGHT = 'right'
        self.running = self.moveUp = self.moveDown = self.moveLeft = self.moveRight = False
    
    def handle_movement(self,event):
        if event.type == KEYDOWN:
            if event.key in (K_LSHIFT, K_RSHIFT):
                # player has started running
                self.running = True
 
            if event.key == K_UP:
                moveUp = True
                moveDown = False
                if not self.moveLeft and not self.moveRight:
                    # only change the direction to up if the player wasn't moving left/right
                    self.direction = self.UP
            elif event.key == K_DOWN:
                moveDown = True
                moveUp = False
                if not self.moveLeft and not self.moveRight:
                    self.direction = self.DOWN
            elif event.key == K_LEFT:
                moveLeft = True
                moveRight = False
                if not moveUp and not moveDown:
                    self.direction = self.LEFT
            elif event.key == K_RIGHT:
                moveRight = True
                moveLeft = False
                if not moveUp and not moveDown:
                    self.direction = self.RIGHT
 
        elif event.type == KEYUP:
            if event.key in (K_LSHIFT, K_RSHIFT):
                # player has stopped running
                self.running = False
 
            if event.key == K_UP:
                moveUp = False
                # if the player was moving in a sideways direction before, change the direction the player is facing.
                if moveLeft:
                    self.direction = self.LEFT
                if moveRight:
                    self.direction = self.RIGHT
            elif event.key == K_DOWN:
                moveDown = False
                if moveLeft:
                    self.direction = self.LEFT
                if moveRight:
                    self.direction = self.RIGHT
            elif event.key == K_LEFT:
                moveLeft = False
                if moveUp:
                    self.direction = self.UP
                if moveDown:
                    self.direction = self.DOWN
            elif event.key == K_RIGHT:
                moveRight = False
                if moveUp:
                    self.direction = self.UP
                if moveDown:
                    self.direction = self.DOWN
                    
        if self.moveUp or self.moveDown or self.moveLeft or self.moveRight:
            # draw the correct walking/running sprite from the animation object
            if self.running:
                if self.direction == self.UP:
                    self.animations_dict['back_run'].blit(windowSurface, (x, y))
                elif self.direction == self.DOWN:
                    self.animations_dict['front_run'].blit(windowSurface, (x, y))
                elif self.direction == self.LEFT:
                    self.animations_dict['left_run'].blit(windowSurface, (x, y))
                elif self.direction == self.RIGHT:
                    self.animations_dict['right_run'].blit(windowSurface, (x, y))
            else:
                # walking
                if direction == UP:
                    animObjs['back_walk'].blit(windowSurface, (x, y))
                elif direction == DOWN:
                    animObjs['front_walk'].blit(windowSurface, (x, y))
                elif direction == LEFT:
                    animObjs['left_walk'].blit(windowSurface, (x, y))
                elif direction == RIGHT:
                    animObjs['right_walk'].blit(windowSurface, (x, y))
     
     
            # actually move the position of the player
            if running:
                rate = RUNRATE
            else:
                rate = WALKRATE
     
            if moveUp:
                y -= rate
            if moveDown:
                y += rate
            if moveLeft:
                x -= rate
            if moveRight:
                x += rate
     
        else:
            # standing still
            moveConductor.stop() # calling stop() while the animation objects are already stopped is okay; in that case stop() is a no-op
            if direction == UP:
                windowSurface.blit(back_standing, (x, y))
            elif direction == DOWN:
                windowSurface.blit(front_standing, (x, y))
            elif direction == LEFT:
                windowSurface.blit(left_standing, (x, y))
            elif direction == RIGHT:
                windowSurface.blit(right_standing, (x, y))
     
        # make sure the player does move off the screen
        if x < 0:
            x = 0
        if x > WINDOWWIDTH - playerWidth:
            x = WINDOWWIDTH - playerWidth
        if y < 0:
            y = 0
        if y > WINDOWHEIGHT - playerHeight:
            y = WINDOWHEIGHT - playerHeight
        windowSurface.blit(instructionSurf, instructionRect)
        
    def update(self, t):
        # Note that this doesn't work if it's been more that self._delay
        # time between calls to update(); we only update the image once
        # then, but it really should be updated twice.
        self.update_animation(t)
        
    def update_animation(self, t):
        if t - self._last_update > self._delay:
            self._frame += 1
            if self._frame >= len(self._images): self._frame = 0
            self.image = self._images[self._frame]
            self._last_update = t
        