"""
Класс Card описывает структуру карты
и методы взаимодействия с ней
"""


class Card:
# конструктор
    def __init__(self, name,random_id, position ):
        self.name = name
        self.position = position
        self.random_id = random_id
