import pygame


from Game.Client.Data.Sprites.abstract_object import Abstract_Object




class Fire(Abstract_Object):
    def __init__(self,internal_name, attached_object):
        Abstract_Object.__init__(self, internal_name)
        self.attached_object = attached_object
        screen = pygame.display.get_surface()
        self.area = screen.get_rect()
        self.direction = "right"
        

    def update(self):
        rotate = pygame.transform.rotate
        if self.direction == "left":
            self.image = rotate(self.original, 180)
            self.rect[0] -= 10
        if self.direction == "right":
            self.rect[0] += 10
        if self.direction == "up":
            self.image = rotate(self.original, 90)
            self.rect[1] -= 10
        if self.direction == "down":
            self.image = rotate(self.original, -90)
            self.rect[1] += 10
        if not self.area.contains(self.rect):
            self.charObject.isFiring = False
            
    def fire_fireball(self, right, charObject):
        #self.rect = self.attached_object.rect.copy()
        self.charObject = charObject
        if right:
            self.direction = "right"
        else:
            self.direction = "left"
        self.original = self.image
        self.rect = charObject.rect.copy()


