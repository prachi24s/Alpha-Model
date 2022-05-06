from action_execution import *
from create_character import *
from create_place import *
from create_item import *
from enable_icon import *


def setCameraFocus(name):
    action('SetCameraFocus('+ name + ')')
    

def start_game():
    create_place('Storage', 'Storage')
    create_character('Kate', 'C')
    character_clothing('Kate', 'Spiky', 'LightArmour')
    set_character_position('Kate', 'Storage')
    create_item('Sword', 'Sword')
    set_position('Sword', 'Storage.Shelf.Left')
    create_item('BlueKey', 'BlueKey')
    set_position('BlueKey', 'Storage.Shelf.Right')
    create_item('Coin', 'Coin')
    set_position('Coin', 'Storage.Barrel')
    enableIcon('Select_Sword', 'Select', 'Sword', "Sword", True)
    enableIcon('Select_BlueKey', 'Select', 'BlueKey', "BlueKey", True)
    enableIcon('Select_Coin', 'Select', 'Coin', "Coin", True)
    enableIcon('Exit_Storage', 'Open', 'Storage.Door', 'Enter the Camp', True)
    
    create_place('Camp', 'Camp')
    create_character('Bob', 'F')
    character_clothing('Bob','Spiky', 'Bandit')
    create_item('bob_sword', 'Sword')
    set_position('bob_sword', 'Bob')
    set_character_position('Bob', 'Camp.RightLog')
    enableIcon('Talk_Bob', 'Talk', 'Bob', "Talk to the Bob", True)
    
    create_place('City', 'City')
    create_character('Sunny', 'B')
    character_clothing('Sunny', 'Long', 'Peasant')
    set_character_position('Sunny', 'City.Bench')
    sit_character('Sunny', 'City.Bench')
    enableIcon('Talk_Sunny', 'Talk', 'Sunny', "Talk to the Sunny", True)
    enableIcon('Exit_City', 'Open', 'City.BrownHouseDoor', 'Enter the Blacksmith', True)
    
    create_place('Blacksmith', 'Blacksmith')
    create_character('Steve', 'D')
    character_clothing('Steve', 'Spiky', 'Merchant')
    set_character_position('Steve', 'Blacksmith.Chest')
    enableIcon('Talk_Steve', 'Talk', 'Steve', "Talk to the Steve", True)
    create_item('GreenPotion', 'GreenPotion')
    set_position('GreenPotion', 'Blacksmith.Anvil')
    create_item('Apple', 'Apple')
    set_position('Apple','Blacksmith.Table.Left')
    enableIcon('Select_Apple', 'Select', 'Apple', "Apple", True)
    enableIcon('Select_GreenPotion', 'Select', 'GreenPotion', "GreenPotion", True)
    enableIcon('Exit_Blacksmith', 'Open', 'Blacksmith.BackDoor', 'Enter the ForestPath', True)
    
    create_place('ForestPath', 'ForestPath')
    create_character('Tom', 'D')
    character_clothing('Tom', 'Short', 'Warlock')
    set_character_position('Tom', 'ForestPath.DirtPile')
    create_item('tom_sword', 'Sword')
    set_position('tom_sword', 'Tom')
    enableIcon('Talk_Tom', 'Talk', 'Tom', "Talk to the Tom", True)
    enableIcon('Exit_ForestPath', 'Open', 'ForestPath.WestEnd', 'Enter the Tavern', True)
    
    create_place('Bridge', 'Bridge')
    #enableIcon('Exit_Bridge', 'Open', 'Bridge.NorthEnd' 'Enter the AlchemyShop', True)
    
    
    create_place('AlchemyShop', 'AlchemyShop')
    create_character('Lily', 'F')
    character_clothing('Lily', 'Long', 'Priest')
    set_character_position('Lily', 'AlchemyShop.LeftBookcase')
    create_item('lily_sword', 'Sword')
    set_position('lily_sword', 'Lily')
    enableIcon('Talk_Lily', 'Talk', 'Lily', "Talk to the Lily", True)
    create_item('BluePotion', 'BluePotion')
    set_position('BluePotion', 'AlchemyShop.Table')
    enableIcon('Select_BluePotion', 'Select', 'BluePotion', "BluePotion", True)
    enableIcon('Exit_AlchemyShop', 'Open', 'AlchemyShop.Door', 'Enter to CastleBedroom', True)
    
    
    create_place('Tavern', 'Tavern')
    create_character('Kim', 'D')
    character_clothing('Kim', 'Short', 'Peasant')
    set_character_position('Kim', 'Tavern.Chair')
    enableIcon('Talk_Kim', 'Talk', 'Kim', "Talk to the Kim", True)
    create_item('Compass', 'Compass')
    set_position('Compass', 'Tavern.RoundTable')
    create_item('Scroll', 'Scroll')
    set_position('Scroll', 'Tavern.Shelf')
    enableIcon('Select_Scroll', 'Select', 'Scroll', "Scroll", True)
    enableIcon('Exit_Tavern', 'Open', 'Tavern.BackDoor', 'Enter the Courtyard', True)
    
    create_place('Courtyard', 'Courtyard')
    create_character('Jerry', 'D')
    character_clothing('Jerry', 'Mage', 'Peasant')
    set_character_position('Jerry', 'Courtyard.BigStall')
    create_item('RedPotion', 'RedPotion')
    set_position('RedPotion', 'Courtyard.BigStall.Left')
    create_item('Bottle', 'Bottle')
    set_position('Bottle', 'Courtyard.BigStall.Right')
    enableIcon('Talk_Jerry', 'Talk', 'Jerry', "Talk to the Jerry", True)
    enableIcon('Exit_Courtyard', 'Open', 'Courtyard.Gate', 'Enter the CastleCrossroads', True)
    
    create_place('CastleCrossroads', 'CastleCrossroads')
    create_character('Mike', 'D')
    character_clothing('Mike', 'Long', 'HeavyArmour')
    enableIcon('Talk_Mike', 'Talk', 'Mike', "Talk to the mike", True)
    enableIcon('Exit_CastleCrossroads', 'Open', 'CastleCrossroads.Gate', 'Enter the CastleBedroom', True)
    
    create_place('CastleBedroom', 'CastleBedroom')
    create_character('James', 'B')
    character_clothing('James', 'Mage_Beard', 'King')
    set_character_position('James', 'CastleBedroom.Bed')
    enableIcon('Talk_James', 'Talk', 'James', "Talk to the James", True)
    create_item('GoldCup', 'GoldCup')
    set_position('GoldCup', 'CastleBedroom.SmallTable')
    
    
    setCameraFocus('Kate')
    action('ShowMenu()')
  
  
  
  
def menu_list(input_string):
    if 'Start' in input_string:
        action('HideMenu()')
        narration_msg = "Welcome to THE LOST KEY! Your name is Kate and you found the lost key of King's treasure house. The bandit, Bob wants to get key from you. Your goal is to protect key from bandit and other people and bring that key safely to the King."
        action('SetNarration(' + narration_msg + ')')
        action('ShowNarration()')
        action('EnableInput()')
    elif 'Selected Credits' in input_string:
        action('ShowCredits()')
    elif 'Close Credits' in input_string:
        action('HideCredits()')
    elif 'Quit' in input_string:
        action('Quit()')
    elif 'Close Narration' in input_string:
        action('HideNarration()')
    
    

    
