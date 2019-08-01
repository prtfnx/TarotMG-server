from DeckClass import Deck


def main():
    new_deck=Deck('thoth',1)
    new_deck.create()
    second_card=new_deck.card_list[1]
    print(new_deck.get_card(2).name)
    
main()