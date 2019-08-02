import sqlite3
import os.path
import DeckClass

from CardClass import Card
 


class SQLite:
    
    def __init__(self, db_name = 'tarotmg.db'):
        BASE_DIR = os.path.dirname(os.path.abspath(__file__))
        self.db_name = os.path.join(BASE_DIR, db_name)

    def connect(self):
        try:
            self.connection = sqlite3.connect(self.db_name)
        except sqlite3.Error as e:
            print(e)
              

    def disconnect(self):
        self.connection.close()

    def is_deck_exist(self, name, user_id):
        conn = self.connection
        with conn:
            cursor = conn.cursor()
            keys = (name, user_id,)
            result = cursor.execute('SELECT count(*) FROM Decks WHERE (name = ? AND user_id = ?)', keys)
            return (result.fetchone()[0] > 0)

    def save_deck(self, deck):
        user_id = deck.client_id
        self.connect()
        conn=self.connection
        if self.is_deck_exist(deck.name, user_id):
            self.update_deck(deck, user_id)
            return
        with conn:
            cursor = conn.cursor()
            keys = (deck.name, user_id,)
            cursor.execute('INSERT INTO Decks (name, user_id) VALUES (?, ?)', keys)
            deck_id = cursor.lastrowid
            cards = deck.card_list
            rows_gen=([deck_id,c.name,c.position,c.random_id] for c in cards)
            cursor.executemany('INSERT INTO Cards (deck_id, name, position, random_id) VALUES (?, ?, ?,?)', rows_gen)
        

    def update_deck(self, deck,user_id):
        conn=self.connection
        with conn:
            cursor = conn.cursor()
            keys = (deck.name, user_id,)
            cursor.execute('SELECT id FROM Decks WHERE (name = ? AND user_id = ?)', keys)
            deck_id = cursor.fetchone()[0]
            cards = deck.card_list  
            rows_gen=([c.position,deck_id,c.name] for c in cards)
            cursor.executemany('UPDATE Cards SET position=? WHERE (deck_id = ? AND name= ?)', rows_gen)
            
    def select_deck(self, name, user_id, card_list_only = False):
        self.connect()
        conn=self.connection
        if (self.is_deck_exist(name, user_id) == True):
            with conn:
                cursor = self.connection.cursor()
                keys = (name, user_id,)
                cursor.execute('SELECT id FROM Decks WHERE (name = ? AND user_id = ?)', keys)
                deck_id = cursor.fetchone()
                cursor.execute('SELECT name, position, random_id FROM Cards WHERE deck_id = ?', deck_id)
                card_rows = cursor.fetchall()
                card_list = []
                for card_name, card_position, card_random_id in card_rows:
                    card = Card(card_name, card_position,card_random_id)
                    card_list.append(card)
                if (card_list_only):
                    return card_list
                else:
                    deck = DeckClass.Deck(name, user_id)
                    deck.card_list = card_list
                return deck
        
#TODO
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
