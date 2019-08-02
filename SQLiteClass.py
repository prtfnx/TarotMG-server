import sqlite3
import os.path

from CardClass import Card


class SQLite:
    
    def __init__(self, db_name = 'tarotmg.db'):
        BASE_DIR = os.path.dirname(os.path.abspath(__file__))
        self.db_name = os.path.join(BASE_DIR, db_name)

    def connect(self):
        self.connection = sqlite3.connect(self.db_name)

    def disconnect(self):
        self.connection.close()

    def is_deck_exist(self, name, user_id):
        cursor = self.connection.cursor()
        keys = (name, user_id,)
        result = cursor.execute('SELECT count(*) FROM Decks WHERE (name = ? AND user_id = ?)', keys)
        return (result.fetchone()[0] > 0)

    def save_deck(self, deck, user_id):
        if self.is_deck_exist(name, user_id)
            self.update_deck(deck,user_id)
            return
        cursor = self.connection.cursor()
        keys = (deck.name, user_id,)
        cursor.execute('INSERT INTO Decks (name, user_id) VALUES (?, ?)', keys)
        deck_id = cursor.lastrowid
        cards = deck.card_list
        cursor.executemany('INSERT INTO Cards (deck_id, name, random_id, position) VALUES (?, ?, ?,?)', ([deck_id,c.name,c.random_id,c.position] for c in cards))
        

'''
    def create_deck(self, name, user_id):
        if (self.is_deck_exist(name, user_id) == False):
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
'''
'''   
    def delete_deck(self, name, user_id):
        if (self.is_deck_exist(name, user_id) == True):
            cursor = self.connection.cursor()
            keys = (name, user_id,)
            cursor.execute('SELECT id FROM deck WHERE (name = ? AND user_id = ?)', keys)
            deck_id = cursor.fetchone()
            # Удаляем колоду
            cursor.execute('DELETE FROM deck WHERE (name = ? AND user_id = ?)', keys)
            # Удаляем все карты из нее
            cursor.execute('DELETE FROM card WHERE deck_id = ?', deck_id)
            self.connection.commit()
'''
    def select_deck(self, name, user_id, card_list_only = False):
        if (self.is_deck_exist(name, user_id) == True):
            cursor = self.connection.cursor()
            keys = (name, user_id,)
            cursor.execute('SELECT id FROM deck WHERE (name = ? AND user_id = ?)', keys)
            deck_id = cursor.fetchone()
            cursor.execute('SELECT name, position FROM card WHERE deck_id = ?', deck_id)
            card_rows = cursor.fetchall()
            card_list = []
            for c in card_rows:
                card = Card(c[0], c[1])
                card_list.append(card)
            if (card_list_only):
                return card_list
            else:
                deck = Deck(name, user_id)
                deck.card_list = card_list
                return deck
        else:
            self.create_deck(name, user_id)
            self.select_deck(name, user_id, card_list_only)

