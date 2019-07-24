#from TCPServerClass import TCPServer
from DeckClass import Deck
from SQLiteClass import SQLite

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
deck.select("thoth")

sqlite = SQLite()
sqlite.connect()
if (sqlite.is_deck_exist("thoth", 1)):
    print("exist")
else:
    print("not exist")
sqlite.disconnect()
