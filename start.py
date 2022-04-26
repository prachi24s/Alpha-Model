 import sys
def check_for_success(command):
    while True:
        received = input()
        if received == 'succeeded ' + command:
            return True
        elif received.startswith('failed ' + command):
            return False
        elif received.startswith('error'):
            return False

 
def action(command):
    print('start ' + command, flush=True)
    return check_for_success(command)

def waitForChoice(choices_list):
    while True:
        dialog_input = input().strip()
        for c in choices_list:
            if c in dialog_input:
                return c

action('ShowMenu()')
action('SetTitle(The Lost Key)')

def Take(character, item, position_name):
    action('Take('+ character + ',' +item + ',' +position_name + ')')

def pocket(char, item):
    action('Pocket(' + char +',' + item + ')')
  
def Die(character):
    action('Die(' + character + ')')
    
def Give(char_from, item, char_to):
    action('Give(' + char_from + ', ' + item +', ' + char_to + ')')

def drink(character):
    action('Drink(' + character + ')')

    
    
while(True):
    i = input()

    if i == 'input Selected Start':
        action('PlaySound(Button)')
        action('HideMenu()')
        action('SetNarration("Welcome to THE LOST KEY! Your name is Kate and you found the lost key of King treasure house. The bandit, Bob wants ro get the key from you. Your gol is to protect the key from bandit and other people and bring that key safely to the king.")')
        action('ShowNarration()')
        action('Wait(7)')
        action('HideNarration()')
        action('EnableInput()')


        action('CreatePlace(Storage,Storage)')
        action('CreatePlace(Camp,Camp)')
        action('CreatePlace(City,City)')
        action('CreatePlace(Blacksmith,Blacksmith)')
        action('CreatePlace(ForestPath,ForestPath)')
        action('CreatePlace(CastleBedroom,CastleBedroom)')

        action('CreateCharacter(Kate)')
        action('SetCameraFocus(Kate)')
        action('SetPosition(Kate,Storage)')
        action('SetClothing(Kate,LightArmour)')
        action('SetHairStyle(Kate,Spiky)')
        action('SetEyeColor(Kate,blue)')
        action('SetRight(Kate)')

    

        action('CreateItem(Sword, Sword)')
        action('CreateItem(BlueKey,BlueKey)')
        action('CreateItem(Coin, Coin)')
        action('CreateItem(GreenPotion, GreenPotion)')
        
        
        action('SetPosition(Sword,Storage.Shelf.Left)')
        action('SetPosition(BlueKey,Storage.Shelf.Right)')
        action('SetPosition(Coin,Storage.Barrel)')
        action('SetPosition(GreenPotion,Blacksmith.Anvil)')
        
        action('EnableIcon(Select_Sword, Select, Sword, Sword, true)')
        action('EnableIcon(Select_BlueKey, Select, BlueKey, BlueKey, true)')
        action('EnableIcon(Select_Coin, Select, Coin, Coin, true)')
        action('FadeIn()')
        action('EnableIcon("Exit_Storage", Exit, Storage.Door, "Enter Camp", true)')
        

        action('CreateCharacter(Bob,F)')
        action('SetPosition(Bob,Camp.RightLog)')
        action('SetClothing(Bob,Bandit)')
        action('SetLeft(Bob)')
        action('EnableIcon(Talk_Bob, Talk, Bob , Talk to the Bob, True)')
        
        
        action('CreateCharacter(Sunny, B)')
        action('SetClothing(Sunny, Peasant)')
        action('SetHairStyle(Sunny, Long)')
        action('SetPosition(Sunny, City.Bench)')
        action('Sit(Sunny, City.Bench')
        action('EnableIcon(Talk_Sunny, Talk, Sunny , Talk to the Sunny, True)')
        action('EnableIcon(Exit_City, Open, City.BrownHouseDoor , Enter the Blacksmith, true)')
        
        
        action('CreateCharacter(Steve, B)')
        action('SetClothing(Steve, Merchant)')
        action('SetHairStyle(Steve, Spiky)')
        action('SetPosition(Steve, Blacksmith.Chest)')
        action('EnableIcon(Talk_Steve, Talk, Steve , Talk to the Steve, True)')
        action('EnableIcon(Exit_Blacksmit, Open, Blacksmith.Door, Enter the Forest, true)')
    
        
        action('CreateCharacter(James, B)')
        action('SetClothing(James, King)')
        action('SetHairStyle(James, Mage_Beard)')
        action('SetPosition(James, CastleBedroom.Bed)')
        action('EnableIcon(Talk_James, Talk, James, Tolk to the James, True)')
    
    
    elif i == 'input Selected Quit':
        init.quit()

    elif i == 'input Selected Credits':
        init.showCredits()

    elif i == 'input Close Credits':
        init.hideCredits()

    elif i == 'input Close Narration':
        init.hideNarration()

    elif i == 'input Exit_Storage Storage.Door':
        action('Exit(Kate,Storage.Door,true')
        action('Enter(Kate,Camp.Exit,true')
        
    elif i.startswith('input Talk_Bob Bob'):
        action('WalkTo(Kate, Bob)')
        
        action('SetLeft(Kate)')
        action('SetRight(Bob)')
        action('SetDialog(Bob: Who are you?)')
        action('SetDialog(Kate: I am Kate)')
        action('SetDialog(Bob: What are you doing here?)')
        action('SetDialog(Kate: I am here to take that key and handover it to the king.)')
        action('SetDialog(Bob:  I want the key...just handover it to me.)')
        action('SetDialog(Kate: No...just go away from my way\\n[Attack | Attack])')
        
        action('ShowDialog()')
        action('Wait(7)')
        action('HideDialog()')
        action('Draw(Kate, Sword)')
        action('Attack(Kate, Bob, false)')
        action('Attack(Bob, Kate, false)')
        action('Attack(Kate, Bob, true)')
        action('Die(Bob)')
        action('Pocket(Kate, Sword')
        action('Exit(Kate, Camp.Exit, true)')
        action('Enter(Kate, City.NorthEnd, true)')
    
    elif i == 'input Select_Coin Coin':
        Take('Kate', 'Coin', 'Storage.Barrel')
        pocket('Kate', 'Coin')
    
    elif i == 'input Select_Sword Sword':
        Take('Kate', 'Sword', 'Storage.Shelf.Left')
        
    elif i == 'input Select_BlueKey BlueKey':
        Take('Kate', 'BlueKey', 'Storage.Shelf.Right')
        pocket('Kate', 'BlueKey' )
        
    elif i == 'input Exit_City City.BrownHouseDoor':
        action('Exit(Kate, City.BrownHouseDoor, true)')
        action('Enter(Kate, Blacksmith.Door, true)')

    elif i == 'input Exit_Blacksmit Blacksmith.Door':
        action('Exit(Kate, Blacksmith.Door, true)')
        action('Enter(Kate, ForestPath.EastEnd, true)')
        action('Exit(Kate, ForestPath.WestEnd, true)')
        action('Enter(Kate, CastleBedroom.Door, true)')
        
    elif i == 'input Talk_Sunny Sunny':
        action('WalkTo(Kate, Sunny)')
        
        action('SetLeft(Kate)')
        action('SetRight(Sunny)')
        action('SetDialog(Kate: Hi! How are you?)')
        action('SetDialog(Sunny: Hey! I am good. You are looking injured, what happened with you?)')
        action('SetDialog(Kate: I had a fight recently thats why I got injured. Can you tell me is there any place where I can get the healing potion?)')
        action('SetDialog(Sunny: Yeah sure! Its just in front of you. Are you able to see the brown house door?)')
        action('SetDialog(Kate: Yes, I can see that.)')
        action('SetDialog(Sunny: Just enter into that door,you can get the healing potion there.)')
        action('SetDialog(Kate: Thank you so much!)')
        action('SetDialog(Sunny: No problem. Take care! \\n[continue | continue])')
        
        action('ShowDialog()')
        action('Wait(7)')
        action('HideDialog()')
        
    elif i == 'input Talk_Steve Steve':
        action('WalkTo(Kate, Steve)')
        
        action('SetLeft(Kate)')
        action('SetRight(Steve)')
        action('SetDialog(Steve: Hi! How can I help you?)')
        action('SetDialog(Kate: I need healing potion, do you have any?)')
        action('SetDialog(Steve: Yes, I am having one.)')
        action('SetDialog(Kate: Fine, how much does it cost?)')
        action('SetDialog(Steve: Its of one gold coin.)')
        action('SetDialog(Kate: I want to take that potion.)')
        action('SetDialog(Steve: Okay!\\n[ continue | continue])')
        
        action('ShowDialog()')
        action('Wait(7)')
        action('HideDialog()')
        
        Take('Steve', 'GreenPotion', 'Blacksmith.Anvil')
        Give('Steve', 'GreenPotion', 'Kate')
        Give('Kate', 'Coin', 'Steve')
        drink('Kate')
        
    
    elif i == 'input Talk_James James':
         action('WalkTo(Kate, James)')
    
         action('SetLeft(Kate)')
         action('SetRight(James)')
         action('SetDialog(Kate: Hello king James. I found the lost key.)')
         action('SetDialog(James: Ohh...Thats great! Where is it?)')
         action('SetDialog(Kate: Here it is)')
         action('SetDialog(James: Thank you so much Kate.\\n[continue | continue])')
    
         action('ShowDialog()')
         action('Wait(7)')
         action('HideDialog()')
    
         Give('Kate', 'BlueKey', 'James')
        
    elif i == 'input Select_Coin Coin':
        Take('Kate', 'Coin', 'Storage.Barrel')
        pocket('Kate', 'Coin')
    


