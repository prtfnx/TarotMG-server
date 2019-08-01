import random
import string

from SQLiteClass import SQLite
from DeckList import get_list_of_cards
from CardClass import Card
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
        self.card_list=[]


    def create(self, deck_name = ""):
        random_id=1 # TODO
        if (deck_name == ""):
            deck_name = self.name
        file_name = get_list_of_cards(deck_name)
        with open(file_name) as file:
            for index,line in enumerate(file):
                self.card_list.append(Card(line,random_id,index,))
        
    def sort(self):
        pass  

    def get_card(self,position):
        return self.card_list[position]


    def delete(self):
        self.card_list=[]
        #self.sqlite.connect()
        #self.sqlite.delete_deck(self.name, self.client_id)
        #self.sqlite.disconnect()
    def select(self, deck_name = ""):
        self.card_list=SQlite.get_list_of_cards

        #if (deck_name == ""):
        #    deck_name = self.name
        #self.sqlite.connect()
        #self.card_list = self.sqlite.select_deck(deck_name, self.client_id, True)
        #self.sqlite.disconnect()

