from SQLiteClass import SQLite
from DeckList import get_list_of_cards
from CardClass import Card
from CardShuffle import card_shuffle
"""
Class Deck describe structure of deck
and methods to operate with it
"""


class Deck:

    def __init__(self, name, user_id):
        """Constructor"""
        self.name = name.lower()
        self.user_id = user_id
        self.card_list = []

    def create(self, deck_name=""):
        """Make new deck with all cards"""
        random_id = 1  # TODO
        if (deck_name == ""):
            deck_name = self.name
        file_name = get_list_of_cards(deck_name)
        with open(file_name) as file:
            for position, line in enumerate(file):
                self.card_list.append(Card(line, position, random_id))

    def shuffle(self):
        """Shuffle deck randomly"""
        card_shuffle(self.card_list)

    def get_card(self, position):
        """Take one card by position"""
        return self.card_list[position]

    def delete(self):
        """ Delete deck from database"""
        self.card_list = []
        SQLite.delete_deck(self.name, self.user_id)

    def select(self, deck_name=""):
        """Load deck from database"""
        self.card_list = SQlite.get_list_of_cards
