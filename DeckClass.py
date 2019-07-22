import random
import string
from SQLiteClass import SQLite
from CardClass import Card
"""
Класс Deck описывает структуру колоды
и методы взаимодействия с ней
"""
class Deck:
    sqlite = SQLite()
    # конструктор
    def __init__(self, name, client_id):
        self.name = name.lower()
        self.client_id = client_id
    def create(self):
        self.sqlite.create_deck(self.name, self.client_id)
    def delete(self):
        self.sqlite.delete_deck(self.name, self.client_id)

