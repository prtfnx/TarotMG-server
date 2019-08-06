"""
Class Card describe structure of card
And methods to opearate with them
"""


class Card:
    def __init__(self, name, position, random_id):
        """Constructer"""
        self.name = name
        self.position = position
        self.random_id = random_id
