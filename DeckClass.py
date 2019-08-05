import random
import string

from SQLiteClass import SQLite
from DeckList import get_list_of_cards
from CardClass import Card
from CardShuffle import card_shuffle
"""
Class Deck describe structure of deck
and methods to operate with it
"""


class Deck:
    sqlite = SQLite()
    # конструктор

    def __init__(self, name, client_id):
        self.name = name.lower()
        self.client_id = client_id
        self.card_list = []

    def create(self, deck_name=""):
        # make new deck with all cards
        random_id = 1  # TODO
        if (deck_name == ""):
            deck_name = self.name
        file_name = get_list_of_cards(deck_name)
        with open(file_name) as file:
            for position, line in enumerate(file):
                self.card_list.append(Card(line, position, random_id))

    def shuffle(self):
        # shuffle deck randomly
        card_shuffle(self.card_list)

    def get_card(self, position):
        # take one card by position
        return self.card_list[position]

    def delete(self):
        self.card_list = []

    def select(self, deck_name=""):
        # load deck from database
        self.card_list = SQlite.get_list_of_cards
