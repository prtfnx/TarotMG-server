import sys
import socket

from CardClass import Card
from DeckClass import Deck

card1 = Card("test card 1", "test user")
print(card1.show())
card2 = Card("test card 2", "test user")
print(card2.show())

deck = Deck("test deck")
deck.add_card(card1)
deck.add_card(card2)
print(deck.show())
selected_card = deck.get_card("test card 2")
print("Selected card is: " + selected_card.name)



