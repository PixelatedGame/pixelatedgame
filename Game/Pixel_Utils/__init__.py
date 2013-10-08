import base64

import os
import pygame
from pygame.locals import * #@UnusedWildImport
from Game.Pixel_Utils.Threading import StoppableThread
import pickle


def pickle_encode( data):
    return base64.encodestring(pickle.dumps(data, -1))

def pickle_decode( data):
    return pickle.loads(base64.decodestring(data))

def load_image(name, colorkey=None):
    fullname = os.path.join(name)
    try:
        image = pygame.image.load(fullname)
    except pygame.error, message:
        print 'Cannot load image:', fullname
        raise SystemExit, message
    image = image.convert()
    if colorkey is not None:
        if colorkey is -1:
            colorkey = image.get_at((0,0))
        image.set_colorkey(colorkey, RLEACCEL)
    return image, image.get_rect()

def load_sound(name):
    class NoneSound:
        def play(self): pass
    if not pygame.mixer or not pygame.mixer.get_init():
        return NoneSound()
    fullname = os.path.join('data', name)
    try:
        sound = pygame.mixer.Sound(fullname)
    except pygame.error, message:
        print 'Cannot load sound:', fullname
        raise SystemExit, message
    return sound

class thread_func( StoppableThread):
    def __init__(self, target, *args):
        StoppableThread.__init__(self)
        self._target = target
        self._args = args
        
 
    def run(self):
        self._target(*self._args)