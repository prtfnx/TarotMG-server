import socket

from CardClass import Card
from DeckClass import Deck
from TCPServer import TCPServer

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

sock = TCPServer("", 13666)
sock.initialize()

try:
    while 1:
        sock.accept_client()
        print("Client accepted: " + sock.address[0])
        try:
            sock.get_data()
        except:
            sock.send_data(b"test")
        finally:
            sock.connection.close()
finally:
    sock.close()

