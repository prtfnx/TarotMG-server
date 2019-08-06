import random
import settings
"""
Shuffle cards in deck
"""
# Handmade, needs testing and maybe to look
# for normal algorithm


def card_shuffle(card_list):
    """
    Overhand shuffle
    Take part of cards from deck to hand
    And then randomly insert part of it to deck
    Like in real life shuffling
    """
    for card in range(settings.NUMBER_OF_SHUFFLE):
        rand1 = random.randint(30, 77)  # which part of deck from end we will take to hand
        hand = card_list[rand1:settings.NUMBER_OF_CARDS]  # take part of cards from end
        card_list[rand1:settings.NUMBER_OF_CARDS] = []  # clear it from deck
        while len(hand) != 0:  # will shuffle until we have cards in hand
            rand2 = random.randint(1, len(hand))  # choose part of parted cards
            index = random.randint(0, len(card_list))  # position to insert cards
            for card in hand[0:rand2]:  # insert random part of cards in hand to random position in deck
                card_list.insert(index, card)  # insert card
                index += 1  # change position to next
            hand[0:rand2] = []  # clear cards that we insert to deck from hand
    for i, card in enumerate(card_list):
        card.position = i
