from TCPServerClass import TCPServer
from DeckClass import Deck

'''
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
'''

deck = Deck("thoth", 1)
deck.create()
deck.delete()

