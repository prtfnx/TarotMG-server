import socket
"""
Класс TCPserver описывает структуру tcp сервера
и методы вщаимодействия с ним
"""
class TCPServer:
    # конструктор
    def __init__(self, host, port):
        self.host = host
        self.port = port
        self.socket = socket.socket()
        #self.socket.settimeout(60)
        #self.data = self.connection.recv(4)
    # методы
    def initialize(self):
        self.socket.bind((self.host, self.port))
        self.socket.listen(13)
    def accept_client(self):
        self.connection, self.address = self.socket.accept()
    def get_data(self):
        data = ""
    def send_string(self, string):
        string = ""