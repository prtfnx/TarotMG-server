import random
"""
Класс Deck описывает структуру колоды
и методы вщаимодействия с ней
"""
class Deck:
    # конструктор
    def __init__(self, name, card_list=[]):
        self.name = name
        self.card_list = card_list
    # методы
    def show(self):
        return "Deck name is '" + self.name + "'\r\nDeck contains " + str(len(self.card_list)) + " cards"
    def add_card(self, card):
        if (card in self.card_list) == False:
            self.card_list.append(card)
    def get_card(self, name):
        for c in self.card_list:
            if c.name == name:
                return c
    def shuffle(self):
        list_len = len(self.card_list)
        if (list_len > 1):
            while list_len > 1:
                k = random.randint(0)
