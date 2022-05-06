import unittest
import mocktestcharacter

class TestCharacter(unittest.TestCase):

    def create_character(self):
        self.assertEqual(create_character('Kate','C'),"succeeded CreateCharacter(Kate,C)")

    def character_clothing(self):
        self.assertEqual(character_clothing.SetClothing('Kate','LightArmour'),"succeeded SetClothing(Kate,LightArmour)")
        self.assertEqual(character_clothing.SetHairStyle('Kate','Spiky'),"succeeded SetHairStyle(Kate,Spiky)")

    def set_character_position(self):
        self.assertEqual(set_character_position('Kate','Storage'),"succeeded SetPosition(Kate,Storage)")
