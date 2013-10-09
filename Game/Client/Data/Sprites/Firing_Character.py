from Game.Client.Data.Sprites.Character import Character
from Game.Client.Data.Sprites.fire import Fire



class Firing_Character(Character):
    def __init__(self, internal_name, char_name):
        Character.__init__(self, internal_name, char_name)
        self.isFiring = False
        self.ranged = Fire("fireball",self)
    
    def _fire(self):
        if not self.isFiring:
            self.isFiring = True 
            self.ranged.fire_fireball(self.data.right, self)