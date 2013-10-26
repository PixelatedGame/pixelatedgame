from Game.Client.Gui.Hud.character_info import character_info
from Game.Client.Gui.Hud.chat import chat

class hud():
    
    def __init__(self):
        character_info()
        self.hudChat = chat()
        
    def chatInput(self, event):
        self.hudChat.update_input(event)