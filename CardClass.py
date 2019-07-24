"""
Класс Card описывает структуру карты
и методы взаимодействия с ней
"""
class Card:
    # конструктор
    def __init__(self, name, position = 0):
        self.name = name
        self.position = position

