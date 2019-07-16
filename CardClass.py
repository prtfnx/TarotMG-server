"""
Класс Card описывает структуру карты
и методы вщаимодействия с ней
"""
class Card:
    # конструктор
    def __init__(self, name, user):
        self.name = name
        self.user = user
    # методы
    def show(self):
        return "Card name is: '" + self.name + "'"
