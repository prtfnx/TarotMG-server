"""
Connect name of decks with files
"""


def get_list_of_cards(deck_name):
    return{
        'thoth': 'thoth_card_list.txt',
        'mr': 'MR_card_list.txt',
        'rw': 'RW_card_list.txt'
    }[deck_name]
