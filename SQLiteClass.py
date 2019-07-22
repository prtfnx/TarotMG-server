import sqlite3
import os.path

class SQLite:
    def __init__(self, db_name = 'tarotmg.db'):
        BASE_DIR = os.path.dirname(os.path.abspath(__file__))
        self.db_name = os.path.join(BASE_DIR, db_name)
    def connect(self):
        self.connection = sqlite3.connect(self.db_name)
    def disconnect(self):
        self.connection.close()

    def create_deck(self, name, user_id):
        self.connect()
        #! Добавить проверку на существование такой колоды у пользователя
        cursor = self.connection.cursor()
        keys = (name, user_id,)
        # Создаем колоду для пользователя        
        cursor.execute('INSERT INTO deck (name, user_id) VALUES (?, ?)', keys)
        deck_id = cursor.lastrowid
        cards = []
        if (name == "thoth"):
            cards = [
                ("fool", deck_id),
                ("magus", deck_id),
                ("priestess", deck_id),
            ]
        # Создаем карты пользователя
        cursor.executemany('INSERT INTO card (name, deck_id) VALUES (?, ?)', cards)
        self.connection.commit()
        self.disconnect()
    def delete_deck(self, name, user_id):
        self.connect()
        #! Добавить проверку на существование такой колоды у пользователя
        cursor = self.connection.cursor()
        keys = (name, user_id,)
        cursor.execute('SELECT id FROM deck WHERE (name = ? AND user_id = ?)', keys)
        deck_id = cursor.fetchone()
        # Удаляем колоду
        cursor.execute('DELETE FROM deck WHERE (name = ? AND user_id = ?)', keys)
        # Удаляем все карты из нее
        cursor.execute('DELETE FROM card WHERE deck_id = ?', deck_id)
        self.connection.commit()
        self.disconnect()
    def select_deck(self, name, user_id):
        '''
        Ecли у пользователя нет колоды, то вызывать метод создания колоды,
        а затем выбор колоды.
        Если у пользователя такая колода есть, то сразу выбираем ее.
        При выборе колоды создается объект класса деки и в него запихиваются
        объекты класса карта.
        Все сие манипуляции отрабатывают в DeckClass.py
        '''

