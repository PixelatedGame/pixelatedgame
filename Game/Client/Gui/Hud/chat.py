import pygame
from pgu import gui
from Game.Client.Data.Sprites.gui_object import gui_object
from Game.Client.Data.Sprites.gui_text import gui_text
from Game.Client.Data.Sprites.gui_input import gui_input

class chat():
    def __init__(self):
        
        self.chat_messages = [{"name": "some_guy", "message" : "Wow, this is a really long messages! How can it be?" }, {"name" : "Fez", "message" : "McLolz!"}, {"name" : "Timmy", "message" : "Dkalim."}, {"name" : "n00b", "message" : "hi :)"}]
        self.screen = pygame.display.get_surface()
        self.screenX, self.screenY = self.screen.get_size()   
        self.lineLengthLimit = 60
        self.messagesAmountLimit = 4
        self.sorted_messages = []
        self.chatInput = None
        
        self.chatNameColor = (255, 0, 0)
        self.chatTextColor = (255, 255, 255)
        self.chatFontSize = 16
        
        self.draw_background()
        self.draw_input()
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
        self.chatBG = gui_object("chatBGnew")
        xpos = self.screenX / 4
        ypos = self.screenY - 100
        self.chatBG.rect.topleft = (xpos, ypos)
        bgAlpha = 100
        self.chatBG.image.fill((255, 255, 255, bgAlpha), None, pygame.BLEND_RGBA_MULT)
        self.chatBG.image.set_alpha(bgAlpha)
        
    def draw_input(self):
        inputX = self.screenX / 4
        inputY = self.screenY - 20
        inputFont = pygame.font.Font(None, self.chatFontSize)
        promptText = "Say: "
        maxInputLength = self.lineLengthLimit - len(promptText)
        
        #self.chatInput = gui_input(position = (inputX, inputY), fontStyle = inputFont, inputPrompt = promptText, textLength = maxInputLength)
        self.chatInput = gui_input(position = (inputX, inputY), fontStyle = inputFont, inputPrompt = promptText, textLength = 10)
    
    def update_input(self, event):
        if event:
            self.chatInput.screen_update(event)
            
    def sort_messages(self):
        for item in self.chat_messages:
            pName = item["name"]
            pMessage = item["message"]
            chatLine = "%s: %s" % (pName, pMessage)
            if len(chatLine) > self.lineLengthLimit: # Split line according to length
                splittedLine = self.split_by_length(chatLine, self.lineLengthLimit)
                for line in splittedLine:
                    self.sorted_messages.append(line)
            else:
                self.sorted_messages.append(chatLine)
        
    def draw_messages(self):  
        xpos = self.screenX / 4
        ypos = self.screenY - 40
        lineSpacing = 20
        
        counter = 0
        
        for item in self.sorted_messages:
            if not counter + 1 > self.messagesAmountLimit:
                self.chat_text = gui_text(item, (xpos, ypos), self.chatTextColor, self.chatFontSize)
                ypos -= lineSpacing
            else:
                break
            counter += 1
            

    