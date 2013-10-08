from Game import Pixel_Utils


class Game_Sounds():
    def __init__(self):
    
        self.whiff_sound = Pixel_Utils.load_sound('whiff.wav')
        self.punch_sound = Pixel_Utils.load_sound('punch.wav')