from Game.Client.Data.Sprites.Character import Character
from Game.Client.Data.Sprites.fire import Fire



class Firing_Character(Character):
    def __init__(self, internal_name, char_name):
        Character.__init__(self, internal_name)
        ranged = Fire("fireball",self)
                fireball.fire_fireball(Game.Client.my_char.data.rect.copy(), Game.Client.my_char.data.right)
                