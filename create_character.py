from action_execution import *
from create_dialog import *
from create_place import *
from camelot_utiles import *
from create_item import *

def create_character(character_name, body_Type):
    action('CreateCharacter(' + character_name + ', ' + body_Type + ')' )

def character_clothing(character_name, Hairstyle, Outfit):
    action('SetHairStyle('+ character_name +', ' + Hairstyle +')')
    action('SetClothing('+ character_name +', ' + Outfit +')')
    
def set_character_position(character_name, position_name):
     action('SetPosition(' + character_name + ', ' + position_name + ')')

def sit_character(character_name, place_name):
    action('Sit('+ character_name +', '+ place_name +')')

def die_character(character_name):
    action('Die('+ character_name +')')

def character_drink(character_name):
    action('Drink('+ character_name +')')

def take_item(character_name, item, Position):
     action('Take('+ character_name +', '+ item +', '+ Position +')')

def pocket(character_name, item):
    action('Pocket('+ character_name +', '+ item +')')

def character_attack(character1, character2):
     action('Attack('+ character1 +', '+ character2 +', false)')

def character_attack_success(character1, character2):   
     action('Attack('+ character1 +', '+ character2 +', true)')

def give_item(item, character1, character2):
     action('Give('+ character1 +', '+ item +', '+ character2 +')')

def character_walk(character1, character2):
    action('WalkTo(' + character1 + ', ' + character2 + ')')
    
def draw(character_name, item):
    action('Draw(' + character_name + ',' + item + ')')

def talktobob(character1, character2):
    character_walk(character1, character2)
    set_right(character1)
    set_left(character2)
    set_dialog('Bob: Who are you?')
    set_dialog('Kate: I am Kate')
    set_dialog('Bob: What are you doing here?')
    set_dialog('Kate: I am here to take that key and handover it to the king.')
    set_dialog('Bob:  I want the key...just handover it to me.')
    set_dialog('Kate: No...just go away from my way\\n[Attack | Attack]')
    show_dialog()
    while 1:
        if 'Attack' in input():
           select ='Attack'
           break
    if select == 'Attack':
        hide_dialog()
        draw('Kate', 'Sword')
        draw('Bob', 'bob_sword')
        character_attack('Bob','Kate')
        character_attack('Kate', 'Bob')
        character_attack('Bob', 'Kate')
        character_attack_success('Kate', 'Bob')
        die_character('Bob')
        pocket('Kate', 'Sword')
        exit_place('Kate', 'Camp.Exit')
        enter_place('Kate', 'City.NorthEnd')

def talktosunny(character1, character2):
     character_walk(character1, character2)
     set_right(character1)
     set_left(character2)
     set_dialog('Kate: Hi! How are you?')
     set_dialog('Sunny: Hey! I am good. You are looking injured what happened with you?')
     set_dialog('Kate: I had a fight recently thats why I got injured. Can you tell me is there any place where I can get the healing potion?')
     set_dialog('Sunny: Yeah sure! Its just in front of you. Are you able to see the brown house door? .')
     set_dialog('Kate: Yes, I can see that.')
     set_dialog('Sunny: Just enter into that door,you can get the healing potion there.')
     set_dialog('Kate: Thank you so much!')
     set_dialog('Sunny: No problem. Take care! \\n[continue | continue]')
     show_dialog()
     while 1:
         if 'continue' in input():
            select ='continue'
            break
     if select == 'continue':
         hide_dialog()
         


def talktosteve(character1, character2):
     character_walk(character1, character2)
     set_right(character1)
     set_left(character2)
     set_dialog('Steve: Hi! How can I help you?')
     set_dialog('Kate: I need healing potion, do you have any?')
     set_dialog('Steve: Yes, I am having one.')
     set_dialog('Kate: Fine, how much does it cost?')
     set_dialog('Steve: Its of one gold coin.')
     set_dialog('Kate: I want to take that potion.')
     set_dialog('Steve: Okay!\\n[ continue | continue]')
     show_dialog()
     while 1:
         if 'continue' in input():
            select ='continue'
            break
     if select == 'continue':
         hide_dialog()
         take_item('Steve', 'GreenPotion', 'Blacksmith.Anvil' )
         give_item('GreenPotion', 'Steve', 'Kate')
         give_item('Coin', 'Kate', 'Steve')
         action('AddToList(GreenPotion, "GreenPotion for getting heal")')
         character_drink('Kate')

         
def talktotom(character1, character2):
     character_walk(character1, character2)
     set_right(character1)
     set_left(character2)
     set_dialog('Tom: Give me the key')
     set_dialog('Kate: I will not give the key... go away from me or else...I will kill you..')
     set_dialog('\\n[ Attack | Attack]')
     show_dialog()
     while 1:
         if 'Attack' in input():
            select ='Attack'
            break
     if select == 'Attack':
        hide_dialog()
        draw('Kate', 'Sword')
        draw('Tom', 'tom_sword')
        character_attack('Kate', 'Tom')
        character_attack('Tom', 'Kate')
        character_attack_success('Kate', 'Tom')
        die_character('Tom')
        pocket('Kate', 'Sword')
        exit_place('Kate', 'ForestPath.WestEnd')
        enter_place('Kate', 'Bridge.SouthEnd')

def talktolily(character1, character2):
     character_walk(character1, character2)
     set_right(character1)
     set_left(character2)
     set_dialog('Lily: You found the key...I want it..just give it to me otherwise it will not be good for you.')
     set_dialog('Kate: No.. I cant give it to you.')
     set_dialog('Lily: Okay! Lets see...\\n[ Attack | Attack]')
     show_dialog()
     while 1:
         if 'Attack' in input():
            select ='Attack'
            break
     if select == 'Attack':
        hide_dialog()
        draw('Kate', 'Sword')
        draw('Lily', 'lily_sword')
        character_attack('Lily', 'Kate')
        character_attack('Kate', 'Lily')
        character_attack('Kate', 'Lily')
        character_attack_success('Kate', 'Lily')
        die_character('Lily')
        pocket('Kate', 'Sword')


def talktokim( character1, character2):
    character_walk(character1, character2)
    set_right(character1)
    set_left(character2)
    set_dialog('Kim: Who are you?')
    set_dialog('Kate: I am Kate')
    set_dialog('Kim: why did you come here ?')
    set_dialog('Kate: I need your help....')
    set_dialog('Kim:  What help do you need ?')
    set_dialog('Kate: I need direction of a place for that I need Campass can you please give me campass')
    set_dialog('Kim:  ok..I will help you..here is the compass\\n[continue | continue]')
    show_dialog()
    while 1:
        if 'continue' in input():
           select ='continue'
           break
    if select == 'continue':
        hide_dialog()
        take_item('Kim', 'Compass', 'Tavern.RoundTable' )
        give_item('Compass', 'Kim', 'Kate')
        action('AddToList(Compass, "Compass for getting direction")')
        pocket('Kate', 'Compass')

def talktojerry(character1, character2):
    character_walk(character1, character2)
    set_right(character1)
    set_left(character2)
    set_dialog('Jerry: Hi! I am serving food and drink for free would you like to have something?\\n[RedPotion | RedPotion] \\n[Bottle | Bottle]')
    show_dialog()
    while 1:
        if 'RedPotion' in input():
            hide_dialog()
            take_item('Jerry', 'RedPotion', 'Courtyard.BigStall')
            give_item('RedPotion', 'Jerry', 'Kate')
            action('AddToList(RedPotion, "RedPotion is poison")')
            character_drink('Kate')
            die_character('Kate')
            set_position('BlueKey', 'Courtyard.Barrel')
            take_item('Jerry', 'BlueKey', 'Courtyard.Barrel')
            break
        elif 'Bottle' in input():
            hide_dialog()
            take_item('Jerry', 'Bottle', 'Courtyard.BigStall')
            give_item('Bottle', 'Jerry', 'Kate')
            set_right(character1)
            set_left(character2)
            set_dialog('Jerry: Give me that key')
            set_dialog('Jerry: Hi! I am serving food and drink for free would you like to have something?\\n[Attack | Attack]')
            show_dialog()
            while 1:
                if 'Attack' in input():
                    hide_dialog()
                    character_attack('Kate', 'Jerry')
                    character_attack('Jerry', 'Kate')
                    character_attack_success('Kate', 'Jerry')
                    exit_place('Kate', 'Courtyard.Gate' )
                    enter_place('Kate', 'CastleCrossroads.WestEnd')
                    exit_place('Kate', 'CastleCrossroads.Gate')
                    enter_place('Kate', 'CastleBedroom.Door')
                    break
            break

def talktojames(character1, character2):
     character_walk(character1, character2)
     set_right(character1)
     set_left(character2)
     set_dialog('Kate: Hello King James...I found the lost key')
     set_dialog('James: Ohh...Thats great! Where is it?')
     set_dialog('Kate: Here it is')
     set_dialog('James: Thank you so much Kate.I want to give you reward for your work.\\n[continue | continue]')
     set_dialog('Thank you king James!')
     show_dialog()
     while 1:
         if 'continue' in input():
            select ='continue'
            break
     if select == 'continue':
         hide_dialog()
         give_item('BlueKey', 'Kate', 'James')
         action('Put(James, BlueKey, CastleBedroom.SmallTable)')
         take_item('James', 'GoldCup', 'CastleBedroom.SmallTable')
         give_item('GoldCup', 'James', 'Kate')
         

