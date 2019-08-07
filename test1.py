from DeckClass import Deck
from CardShuffle import card_shuffle
from CardClass import Card
from SQLiteClass import SQLite


def deck_create_test():
    new_deck = Deck('thoth', 33333)
    new_deck.create()
    second_card = new_deck.card_list[1]
    return new_deck


def shuffle_test():
    list_test = []
    result = []
    for i in range(78):
        list_test.append(Card(str(i),i,i))
    for card in list_test:
        result.append(card.name)
    print(','.join(result))
    result=[]
    card_shuffle(list_test)
    for card in list_test:
        result.append(card.name)
    print(','.join(result))


def get_card_test():
    test_deck = deck_create_test()
    test_deck.shuffle()
    card = test_deck.get_card(4)
    print(card.name)


def sql_test(): 
    deck = deck_create_test()
    sqlite = SQLite()
    sqlite.save_deck(deck)
    new_deck = sqlite.select_deck('thoth',33333)
    new_deck.shuffle()
    sqlite.save_deck(new_deck)
    new_new_deck=sqlite.select_deck('thoth',33333)
    card = new_deck.get_card(4)
    print(card.name)
    print(card.path_to_image)
sql_test()