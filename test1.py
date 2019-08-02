from DeckClass import Deck
from CardShuffle import card_shuffle
from CardClass import Card

def deck_create_test():
    new_deck=Deck('thoth',1)
    new_deck.create()
    second_card=new_deck.card_list[1]
    return new_deck


def shuffle_test():
    list_test=[]
    result=[]
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
    test_deck=deck_create_test()
    test_deck.shuffle()
    card=test_deck.get_card(4)
    print(card.name)

get_card_test()
