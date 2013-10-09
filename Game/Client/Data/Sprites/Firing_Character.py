from Game.Client.Data.Sprites.Character import Character
from Game.Client.Data.Sprites.fire import Fire



class Firing_Character(Character):
    def __init__(self, internal_name, char_name):
        Character.__init__(self, internal_name, char_name)
        self.isFiring = False
        
        
    
    def _fire(self):
        if not self.isFiring:
            self.isFiring = True
            self.ranged = Fire("fireball",self.rect.copy(),self.data.right)
            
    
    def update(self):
        if self.isFiring:
            if not self.area.contains(self.ranged.rect):
                    self.isFiring = False
                    self.ranged = []
                
        self.rect = self.data.rect
        
        if self.data.dizzy:
            self._spin()
        else:
            self._walk()
            
        if self.data.up:
            self.image = self.front_sprite.image
        else:
            self.image = self.back_sprite.image
            