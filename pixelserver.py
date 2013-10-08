




import SocketServer
from Game import Pixel_Utils


class MyUDPHandler(SocketServer.BaseRequestHandler):
    """
    This class works similar to the TCP handler class, except that
    self.request consists of a pair of data and client socket, and since
    there is no connection the client address must be given explicitly
    when sending data back via sendto().
    """

    def handle(self):
        self.req_data_type = self.request[0].split(" ")[0]
        self.req_data = self.request[0].split(" ")[1]
        
        
        options = {0 : self.update_player,
                   1 : self.get_characters
                }               
        options[int(self.req_data_type)]()
        
        socket = self.request[1]
        
        socket.sendto(self.data, self.client_address)
    
    def update_player(self):
        data     = Pixel_Utils.pickle_decode(self.req_data) 
        char_data = data['update_player']
        for local_character_data in g_characters:
            if local_character_data.char_name == char_data.char_name:
                g_characters.remove(local_character_data)
        g_characters.append(char_data)
        self.data = "ok"
        
    def get_characters(self):
        self.data = Pixel_Utils.pickle_encode(g_characters)
    

if __name__ == "__main__":
    g_characters = []
    HOST, PORT = "0.0.0.0", 9999
    server = SocketServer.UDPServer((HOST, PORT), MyUDPHandler)
    server.serve_forever()