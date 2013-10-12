import pygame
from Game.Client.Data.Animations import pixel_animation



class Pixel_Animated_Object(pygame.sprite.DirtySprite):
    def __init__(self, internal_name = None):
        pygame.sprite.DirtySprite.__init__(self)
        self.internal_name = internal_name
        screen = pygame.display.get_surface()
        self.area = screen.get_rect()
        if internal_name is not None:
            self.sprite_dict = Sprites.get_sprites(self.internal_name)
        game_group.add(self)
        self.dirty =2
    
    
        
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
        