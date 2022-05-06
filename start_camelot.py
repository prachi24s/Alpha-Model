from action_execution import *
from camelot_utiles import *
from create_dialog import *
from create_character import *

start_game()

while(True):
    i = input()
    menu_list(i)
    
    if i == 'input Exit_Storage Storage.Door':
         exit_place('Kate', 'Storage.Door')
         enter_place('Kate', 'Camp.Exit')
         
    elif i == 'input Select_Coin Coin':
         take_item('Kate', 'Coin', 'Storage.Barrel')
         action('AddToList(Coin, "Coin for buying the potion")')
         pocket('Kate', 'Coin')
         
    elif i == 'input Select_Sword Sword':
         take_item('Kate', 'Sword', 'Storage.Shelf')
         action('AddToList(Sword, "Sword to fight with bandit and other people")')
         
    elif i == 'input Select_BlueKey BlueKey':
         take_item('Kate', 'BlueKey', 'Storage.Shelf')
         action('AddToList(BlueKey, "Bluekey is the treasure key")')
         pocket('Kate', 'BlueKey')
    
    elif i == 'input Talk_Bob Bob':
         talktobob('Kate', 'Bob')
         
    elif i == 'input Talk_Sunny Sunny':
         talktosunny('Kate', 'Sunny')
        
    elif i == 'input Exit_City City.BrownHouseDoor':
         exit_place('Kate', 'City.BrownHouseDoor')
         enter_place('Kate', 'Blacksmith.Door')
    
    elif i == 'input Talk_Steve Steve':
         talktosteve('Kate', 'Steve')
         
    elif i == 'input Select_GreenPotion GreenPotion':
         give_item('GreenPotion', 'Steve', 'Kate')
         
    elif i == 'input Select_Apple Apple':
         give_item('Apple', 'Steve', 'Kate')
         
    elif i == 'input Exit_Blacksmith Blacksmith.BackDoor':
         exit_place('Kate', 'Blacksmith.Backdoor')
         enter_place('Kate', 'ForestPath.EastEnd')
         
    elif i == 'input Talk_Tom Tom':
         talktotom('Kate', 'Tom')
     
    elif i == 'input Exit_ForestPath ForestPath.WestEnd':
         exit_place('Kate', 'ForestPath.WestEnd')
         enter_place('Kate', 'Tavern.Door')
         
    elif i == 'input Talk_Kim Kim':
         talktokim('Kate', 'Kim')
     

    elif i == 'input Select_Scroll Scroll':
         take_item('Kate', 'Scroll', 'Tavern.Shelf')
         action('AddToList(Scroll, "Scroll for getting map of location")')

    elif i == 'input Exit_Tavern Tavern.Exit':
         exit_place('Kate', 'Tavern.BackDoor')
         enter_place('Kate', 'Courtyard.Gate')
     
    elif i == 'input Talk_Jerry Jerry':
         talktojerry('Kate', 'Jerry')
         
         
    elif i == 'input Talk_James James':
         talktojames('Kate', 'James')
         
    elif i == 'input arrived Kate position Bridge.WestEnd':
         exit_place('Kate', 'Bridge.WestEnd')
         enter_place('Kate', 'AlchemyShop.Door')
         

    elif i == 'input arrived Kate position Bridge.NorthEnd':
         exit_place('Kate', 'Bridge.NorthEnd')
         enter_place('Kate', 'Tavern.BackDoor')
         
    elif i == 'input Exit_Tavern Tavern.BackDoor':
         exit_place('Kate', 'Tavern.BackDoor')
         enter_place('Kate', 'Courtyard.Gate')
         

    elif i == 'input Talk_Lily Lily':
         talktolily('Kate', 'Lily')
         
    elif i == 'input Exit_AlchemyShop AlchemyShop.Door':
         exit_place('Kate', 'AlchemyShop.Door')
         enter_place('Kate', 'CastleBedroom.Door')

    elif i == 'input Key Inventory':
        action('ShowList(Kate)')
    
    elif i == 'input Close List':
         action('HideList()')
