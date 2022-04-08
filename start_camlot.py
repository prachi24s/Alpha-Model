from Action import *
from Initialize import *

init = Initialize()

while(True):

    i = input()
    
    if i == 'input Selected Start':
        init.startGame()
        
    elif i == 'input Selected Quit':
        init.quit()

    elif i == 'input Selected Credits':
        init.showCredits()

    elif i == 'input Close Credits':
        init.hideCredits()

    elif i == 'input Close Narration':
        init.hideNarration()

    elif i == 'input Exit_Storage Storage.Door':
        init.enter_camp()

    elif i.startswith('input Talk_Bob Bob'):
        init.talkTobob()
        
    elif i == 'input Select_Sword Sword':
        init.take_sword()
        
    elif i == 'input Select_BlueKey BlueKey':
        init.take_key()
        
    elif i == 'input Exit_City City.BrownHouseDoor':
        init.enter_blacksmith()
        
    elif i == 'input Talk_Steve Steve':
        init.talkTosteve()

    elif i == 'input Exit_Blacksmith Blacksmith.BackDoor':
        init.exit_blacksmith()

    elif i == 'input Talk_Sunny Sunny':
        init.talkTosunny()

    elif i == 'input Talk_James James':
        init.talkTojames()
        
    elif i == 'input Select_Coin Coin':
        init.take_coin()

