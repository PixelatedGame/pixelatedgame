import pygame
from Game.Client.Data.Sprites.pixel_object import Pixel_Object
from Game.Client.Modules import eztext


class gui_input(Pixel_Object):
    def __init__(self, position, fontStyle = 'pygame.font.Font(None, 32)', fontColor = (255,255,255), inputPrompt = 'type here: ', textLength = 45):
        Pixel_Object.__init__(self)
        self.textBox = eztext.Input(maxlength=textLength, font = fontStyle, color=fontColor, prompt=inputPrompt)
        self.drawText()
        self.rect = self.image.get_rect()
        self.rect.topleft = position
        
    def drawText(self):
        self.textBox.drawText()
        self.image = self.textBox.text
        
    def screen_update(self, event = None):
        if event:
            self.textBox.getFocus(event)
            
    def update(self):
        self.drawText()