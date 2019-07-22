"""
Класс Card описывает структуру карты
и методы взаимодействия с ней
"""
class Card:
    # конструктор
    def __init__(self, name):
        self.name = name
    def show(self):
        print("Card name: " + self.name)
