import sqlite3
import os.path
import DeckClass
from CardClass import Card
"""
Class that make connection with database
And operate with it
"""


class SQLite:

    def __init__(self, db_name='tarotmg.db'):
        """Constructer"""
        BASE_DIR = os.path.dirname(os.path.abspath(__file__))
        self.db_name = os.path.join(BASE_DIR, db_name)

    def connect(self):
        """Connect to database"""
        # Maybe that is not optimal
        try:
            self.connection = sqlite3.connect(self.db_name)
        except sqlite3.Error as e:
            print(e)

    def is_deck_exist(self, name, user_id):
        """Check for existence of deck in database"""
        conn = self.connection
        with conn:
            cursor = conn.cursor()
            keys = (name, user_id,)
            result = cursor.execute(
                'SELECT count(*) FROM Decks WHERE (name = ? AND user_id = ?)', keys)
            return (result.fetchone()[0] > 0)

    def save_deck(self, deck):
        """Save deck to database"""
        user_id = deck.user_id
        self.connect()
        conn = self.connection  # Maybe is not optimal
        # Some mess with safe connection and statement "with"
        if self.is_deck_exist(deck.name, user_id):
            # check if deck alredy exist
            self.update_deck(deck, user_id)
            return
        with conn:
            cursor = conn.cursor()
            keys = (deck.name, user_id,)
            # save deck
            cursor.execute(
                'INSERT INTO Decks (name, user_id) VALUES (?, ?)', keys)
            deck_id = cursor.lastrowid
            cards = deck.card_list
            # generator for unpack name,position and random data from card
            rows_gen = ([deck_id, c.name, c.position, c.random_id, c.path_to_image]
                        for c in cards)
            # save cards
            cursor.executemany(
                'INSERT INTO Cards (deck_id, name, position, random_id, path_to_image) VALUES (?, ?, ?,?,?)', rows_gen)

    def update_deck(self, deck, user_id):
        """Update deck, exucated if deck already exist"""
        conn = self.connection
        with conn:
            cursor = conn.cursor()
            keys = (deck.name, user_id,)
            # all operations analogy to save_deck
            cursor.execute(
                'SELECT id FROM Decks WHERE (name = ? AND user_id = ?)', keys)
            deck_id = cursor.fetchone()[0]
            cards = deck.card_list
            rows_gen = ([c.position, deck_id, c.name] for c in cards)
            cursor.executemany(
                'UPDATE Cards SET position=? WHERE (deck_id = ? AND name= ?)', rows_gen)

    def select_deck(self, name, user_id,):
        """Load deck from database"""
        self.connect()
        conn = self.connection
        # Check for existence of deck, TODO for not
        if (self.is_deck_exist(name, user_id)):
            with conn:
                cursor = self.connection.cursor()
                keys = (name, user_id,)
                cursor.execute(
                    'SELECT id FROM Decks WHERE (name = ? AND user_id = ?)', keys)
                deck_id = cursor.fetchone()
                cursor.execute(
                    'SELECT name, position, random_id, path_to_image FROM Cards WHERE deck_id = ?', deck_id)
                card_rows = cursor.fetchall()
                card_list = []
                # Unpacking cards
                for c_name, c_position, c_random_id, c_path_to_image in card_rows:
                    card = Card(c_name, c_position, c_random_id, c_path_to_image)
                    card_list.append(card)
                deck = DeckClass.Deck(name, user_id)
                deck.card_list = card_list
                return deck

    def delete_deck(self, name, user_id):
        """Delete deck from database"""
        if self.is_deck_exist(name, user_id):
            with conn:
                cursor = self.connection.cursor()
                keys = (name, user_id,)
                cursor.execute(
                    'SELECT id FROM deck WHERE (name = ? AND user_id = ?)', keys)
            deck_id = cursor.fetchone()
            # Delete deck
            cursor.execute('DELETE FROM deck WHERE (name = ? AND user_id = ?)', keys)
            # Delete all cards
            cursor.execute('DELETE FROM card WHERE deck_id = ?', deck_id)
            self.connection.commit()
