import random
import string

from SQLiteClass import SQLite

"""
Класс Deck описывает структуру колоды
и методы взаимодействия с ней
"""
class Deck:
    sqlite = SQLite()
    card_list = []
    # конструктор
    def __init__(self, name, client_id):
        self.name = name.lower()
        self.client_id = client_id
    def create(self, deck_name = ""):
        if (deck_name == ""):
            deck_name = self.name
        self.sqlite.connect()
        self.sqlite.create_deck(deck_name, self.client_id)
        self.sqlite.disconnect()
    def delete(self):
        self.sqlite.connect()
        self.sqlite.delete_deck(self.name, self.client_id)
        self.sqlite.disconnect()
    def select(self, deck_name = ""):
        if (deck_name == ""):
            deck_name = self.name
        self.sqlite.connect()
        self.card_list = self.sqlite.select_deck(deck_name, self.client_id, True)
        self.sqlite.disconnect()

