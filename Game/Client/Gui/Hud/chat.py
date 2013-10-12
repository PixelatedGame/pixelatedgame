import pygame
from Game.Client.Data.Sprites.gui_object import gui_object
from Game.Client.Data.Sprites.gui_text import gui_text

class chat():
    def __init__(self):
        self.chat_messages = [{"name": "some_guy", "message" : "Wow, this is a really long messages! How can it be?" }, {"name" : "Fez", "message" : "McLolz!"}, {"name" : "Timmy", "message" : "Dkalim."}, {"name" : "n00b", "message" : "hi :)"}]
        self.screen = pygame.display.get_surface()
        self.screenX, self.screenY = self.screen.get_size()   
        self.lineLengthLimit = 60
        self.messagesAmountLimit = 5
        self.sorted_messages = []
        self.draw_background()
        self.sort_messages()
        self.draw_messages()
        
    def split_by_length(self, stringToSplit, block_size):
        splittedString = []
        stringLength = len(stringToSplit)
        for i in range(0, stringLength , block_size):
            splittedString.append(stringToSplit[i:i+block_size])
        splittedString = splittedString[::-1] # Reverse line order for chat display
        return splittedString
        
        
    def draw_background(self):
        self.chatBG = gui_object("chatBG")
        xpos = self.screenX / 4
        ypos = self.screenY - 80
        self.chatBG.rect.topleft = (xpos, ypos)
        
    def sort_messages(self):
        for item in self.chat_messages:
            pName = item["name"]
            pMessage = item["message"]
            chatLine = "%s: %s" % (pName, pMessage)
            if len(chatLine) > self.lineLengthLimit:
                splittedLine = self.split_by_length(chatLine, self.lineLengthLimit)
                for line in splittedLine:
                    self.sorted_messages.append(line)
            else:
                self.sorted_messages.append(chatLine)
        
    def draw_messages(self):  
        fontColor = (255,255,255)
        fontSize = 16
        xpos = self.screenX / 4
        ypos = self.screenY - 20
        lineSpacing = 20
        
        counter = 0
        
        for item in self.sorted_messages:
            if not counter + 1 > self.messagesAmountLimit:
                self.chat_text = gui_text(item, (xpos, ypos), fontColor, fontSize)
                ypos -= lineSpacing
            else:
                break
            counter += 1
            

    