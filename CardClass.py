"""
Class Card describe structure of card
And methods to opearate with them
"""


class Card:
    def __init__(self, name, position, random_id, path_to_image):
        """Constructer"""
        self.name = name
        self.position = position
        self.random_id = random_id
        self.path_to_image = path_to_image
