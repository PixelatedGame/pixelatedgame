from Game.Client.Data.Sprites.Character import Character
from Game.Client.Data.Sprites.fire import Fire
from win32con import NULL



class Firing_Character(Character):
    def __init__(self, internal_name, char_name, ranged_attack="fireball"):
        Character.__init__(self, internal_name, char_name)
        self.data.isFiring = False
        self.data.ranged_attack = ranged_attack
        
        
    
    def _fire(self):
        if not self.data.isFiring:
            self.data.isFiring = True
            self.ranged = Fire(self.data.ranged_attack,self.rect.copy(),self.data.right)
            
    
    def screen_update(self):
        if self.data.isFiring:
            if not self.area.contains(self.ranged.rect):
                    self.data.isFiring = False
                    self.ranged.destory()
                    self.ranged = NULL
                    
                
        self.rect = self.data.rect
        
        
            
        if self.data.up:
            self.image = self.front_sprite.image
        else:
            self.image = self.back_sprite.image
            