"""
Класс Card описывает структуру карты
и методы взаимодействия с ней
"""


class Card:
# конструктор
    def __init__(self, name, position, random_id):
        self.name = name
        self.position = position
        self.random_id = random_id
