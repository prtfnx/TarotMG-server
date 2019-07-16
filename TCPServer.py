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
        # Допустим, если мы приняли 0, то клиент хочет закрыть соединение
        if command_type == 0:
            self.close()
        # 1 - что-то другое
        elif command_type == 1:
            self.close()
        # И так далее
        elif command_type == 2:
            self.close()
            # close тут для примера прост висит, но в реальности,
            # в зависиммости от того что от нас хочет клиент
            # он будет высылать разные пакеты данных и обрабатывать
            # их нужно будет по-разному
        elif command_type == 3:
            self.close()
        elif command_type == 4:
            self.close()
    # Метод отправки данных клиенту
    def send_data(self, data):
        data = b""
    # Метод для закрытия соединения
    def close(self):
        self.socket.close()
