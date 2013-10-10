import pygame


from Game.Client.Data.Sprites.abstract_object import Abstract_Object




class Fire(Abstract_Object):
    def __init__(self,internal_name, source_rect, is_direction_right):
        Abstract_Object.__init__(self, internal_name)
        self.isFiring = True 
        self.rect = source_rect
        if is_direction_right:
            self.direction = "right"
        else:
            self.direction = "left"
        
        self.original = self.image
        

    def screen_update(self):
        rotate = pygame.transform.rotate
        if self.direction == "left":
            self.image = rotate(self.original, 180)
            self.rect[0] -= 10
        if self.direction == "right":
            self.image = self.original
            self.rect[0] += 10
        if self.direction == "up":
            self.image = rotate(self.original, 90)
            self.rect[1] -= 10
        if self.direction == "down":
            self.image = rotate(self.original, -90)
            self.rect[1] += 10
        

       


