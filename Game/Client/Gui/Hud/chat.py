import pygame
from Game.Client.Data.Sprites.gui_object import gui_object
from Game.Client.Data.Sprites.gui_text import gui_text

class chat():
    def __init__(self):
        chat_messages = [{"name": "some_guy", "message" : "Wow, this is a really long messages! How can it be?" }, {"name" : "Fez", "message" : "McLolz!"}, {"name" : "Timmy", "message" : "Dkalim."}, {"name" : "n00b", "message" : "hi :)"}]
        self.screen = pygame.display.get_surface()
        self.screenX, self.screenY = self.screen.get_size()   
        self.draw_background()
        self.draw_messages(chat_messages)
        
    def draw_background(self):
        self.chatBG = gui_object("chatBG")
        xpos = self.screenX / 2
        ypos = self.screenY - 80
        self.chatBG.rect.topleft = (0, 0)
        
    def draw_messages(self, chat_messages):
        
             
        fontColor = (255,255,255)
        fontSize = 16
        xpos = self.screenX / 4
        ypos = self.screenY - 20
        lineSpacing = 20
        messagesAmount = 3
        lineLengthLimit = 60
        
        for i in range(messagesAmount):
            pName = chat_messages[i]["name"]
            pMessage = chat_messages[i]["message"]
            chatLine = "%s: %s" % (pName, pMessage)
            if len(chatLine) > lineLengthLimit:
                print "split line"
            self.chat_text = gui_text(chatLine, (xpos, ypos), fontColor, fontSize)
            ypos -= lineSpacing
            
    