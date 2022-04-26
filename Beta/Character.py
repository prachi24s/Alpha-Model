from Action import *

class Character:

    def __init__(self, name, body_type, hair_style, outfit, initial_position):
        self.name = name
        self.body_type = body_type
        self.hair_style = hair_style
        self.outfit = outfit

        action(f'CreateCharacter({self.name}, {self.body_type})')
        action(f'SetClothing({self.name}, {self.outfit})')
        action(f'SetHairStyle({self.name}, {self.hair_style})')
        self.setPosition(initial_position)

    def setPosition(self, position):
        action(f'SetPosition({self.name}, {position})')
