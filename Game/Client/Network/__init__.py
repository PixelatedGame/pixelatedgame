import socket

from Game import Pixel_Utils




class clientconnection():

    def __init__(self):
            self.sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
            self.HOST, self.PORT = "127.0.0.1", 9999
    def send_request(self,request_id,data):
        init_player_packet = Pixel_Utils.pickle_encode(data)
        self.sock.sendto(request_id + " " + init_player_packet , (self.HOST, self.PORT))
        self.sock.recv(60000)
        
    def update_player(self,char_data):
        self.send_request("0", {'update_player': char_data})
        
    def get_characters(self):
        get_players_packet = "get_characters"
        self.sock.sendto("1 " + get_players_packet , (self.HOST, self.PORT))
        received = self.sock.recv(60000)
        return Pixel_Utils.pickle_decode(received)     