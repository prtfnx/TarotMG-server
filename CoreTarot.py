from DeckClass import Deck
from SQLiteClass import SQLite
'''
Main governing class with I/O
For every session make one Tarot object
'''


class Tarot:
    ''' Governor of app'''
    def __init__(self, user_name, user_id):
        self.user_name = user_name
        self.user_id = user_id

    def register_user(self, user_name, user_id):
        pass

    # TODO maybe need to full login authetication process

    def sign_user(self,user_name)
        pass

    def create_new_deck(self, deck_name, user_id):
        new_deck = Deck(deck_name, user_id)
        return new_deck.create()

    def load_deck(self, deck_name, user_id):
        sqlite = SQLite()
        new_deck = sqlite.select_deck(deck_name, user_id)
        return new_deck

    def save_deck(self, deck,():
        sqlite = SQLite()
        sqlite.save_deck(deck)
        return 1

    