import socket
from CardClass import Card
from DeckClass import Deck
"""
Класс TCPserver описывает структуру tcp сервера
и методы взаимодействия с ним
"""
class TCPServer:
    # конструктор
    def __init__(self, host, port):
        self.host = host
        self.port = port
        self.socket = socket.socket()
    # методы
    def initialize(self):
        self.socket.bind((self.host, self.port))
        self.socket.listen(13)
    # Метод для принятия соединения от клиента
    def accept_client(self):
        self.connection, self.address = self.socket.accept()
    # метод получения данных от клиента
    def get_data(self):
        # получаем первые 4 байта (целое число) - идентификатор клиента, что бы различать их как-то
        client_id = int.from_bytes(self.socket.recv(4), "little")
        # получаем следующее число - тип команды(запроса от клтента)
        #   теоретически, у нас будет какое-то число вариаций запросов от пользователя
        #   и мы сможем все их отрабатывать
        command_type = int.from_bytes(self.socket.recv(4), "little")
        # 0 - закрыть соединение
        if command_type == 0:
            self.close()
        # 1 - создать колоду
        elif command_type == 1:
            # получаем тип колоды, которую хочет создать клиент
            # 1 - тота, 2 - райдер, 3 - марсельское
            deck_type = int.from_bytes(self.socket.recv(4), "little")
            deck_name = "toth"
            if deck_type == 1:
                deck_name = "toth"
            elif deck_type == 2:
                deck_name = "waite"
            elif deck_type == 3:
                deck_name = "marsele"
            deck = Deck(deck_name, client_id)
            print("Колода создана: " + deck.show())
    # Метод отправки данных клиенту
    def send_data(self, data):
        data = b""
    # Метод для закрытия соединения
    def close(self):
        self.socket.close()
