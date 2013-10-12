import pygame
from Game.Client.Data.Sprites.gui_text import gui_text

class chat():
    def __init__(self):
        chat_messages = [{"name": "some_guy", "message" : "Wow, this is a really long messages! How can it be?" }, {"name" : "Fez", "message" : "McLolz!"}, {"name" : "Timmy", "message" : "Dkalim."}, {"name" : "n00b", "message" : "hi :)"}]
        self.draw_messages(chat_messages)
        
    def draw_messages(self, chat_messages):
        screen = pygame.display.get_surface()
        screenX, screenY = screen.get_size()        
        fontColor = (255,255,255)
        fontSize = 16
        xpos = screenX / 4
        ypos = screenY - 20
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
            
    