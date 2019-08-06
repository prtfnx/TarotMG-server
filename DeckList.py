"""
Connect name of decks with files
"""


def get_list_of_cards(deck_name):
    return{
        'thoth': 'lists_of_cards/thoth_card_list.txt',
        'mr': 'lists_of_cards/MR_card_list.txt',
        'rw': 'lists_of_cards/RW_card_list.txt'
    }[deck_name]
