
from Game.Client.Data.Sprites.pixel_object import Pixel_Object


class Abstract_Object(Pixel_Object):
    def __init__(self, internal_name = None):
        Pixel_Object.__init__(self, internal_name)
        self.sprite = self.get_self_sprite()
        self.rect = self.sprite.rect
        self.image = self.sprite.image
        

    def screen_update(self):
        raise NotImplemented