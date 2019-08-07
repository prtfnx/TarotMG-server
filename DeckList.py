import os
"""
Connect name of decks with files
"""


def get_list_of_cards(deck_name):
    """ link deck name and files"""
    return{
        'thoth': 'lists_of_cards/thoth_card_list.txt',
        'mr': 'lists_of_cards/MR_card_list.txt',
        'rw': 'lists_of_cards/RW_card_list.txt'
    }[deck_name]


def get_list_of_pathes(deck_name):
    """ link card with path of image """
    list_of_pathes = []
    # take path to dir with images
    path = {
        'thoth': 'images/thoth/',
        'mr': 'images/marseille/',
        'rw': 'images/rider_waite/'
    }[deck_name]
    # Get all files in path
    for path, subdirs, files in os.walk(path):
        for name in files:
            list_of_pathes.append(os.path.join(path, name))
    # !!! work only with right organised names with ascedant order
    # maybe TODO something another
    list_of_pathes.sort()
    return list_of_pathes
