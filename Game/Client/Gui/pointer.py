import pygame
from Game.Client.Data.Sprites.abstract_object import Abstract_Object





class Pointer(Abstract_Object):
    def __init__(self, internal_name):
        Abstract_Object.__init__(self, internal_name)
        self.punching = 0

    def update(self):
        "move the fist based on the mouse position"
        pos = pygame.mouse.get_pos()
        self.rect.midtop = pos
        if self.punching:
            self.rect.move_ip(5, 10)

    def punch(self, target):
        "returns true if the fist collides with the target"
        if not self.punching:
            self.punching = 1
            hitbox = self.rect.inflate(-5, -5)
            hit_target = hitbox.colliderect(target.data.rect)
            return hit_target


    def unpunch(self):
        "called to pull the fist back"
        self.punching = 0


