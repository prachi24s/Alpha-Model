from action_execution import *
from create_dialog import *

def create_character(character_name, Body_Type):
    action('CreateCharacter(' + character_name + ', ' +  + ')')

def character_clothing(character_name, Hairstyle, Outfit):
    action('SetHairStyle('+ character_name +', ' + Hairstyle +')')
    action('SetClothing('+ character_name +', ' + Outfit +')')

def set_character_position(character_name, position_name):
     action('SetPosition(' + character_name + ', ' + position_name + ')')

def sit_character(character_name, place_name):
    action('Sit('+ character_name +', '+ place_name +')')


def die_character(character_name):
    action('Die('+ character_name +')')


def character_dirnk(character_name):
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
    action(f'WalkTo({character1}, {character2})')

def talktobob(self, character1, character2):
    character_walk(character1, character2)
    set_right(character1)
    set_left(character2)
    set_dialog('Bob: tum kaun ho?')
    set_dialog('Kate: main ket hoon')
    set_dialog('Bob: too yahaan kya kar raha hai?')
    set_dialog('Kate: main yahaan vah chaabee lene aur raaja ko saumpane aaya hoon.')
    set_dialog('Bob:  mujhe chaabee chaahie...bas ise mujhe saump do.')
    set_dialog('Kate: nahin...bas mere raaste se hat jao\\n[Attack | aakraman karana]')
    show_dialog()
    while 1:
        if 'Attack' in input():
           select ='Attack'
           break
    if select == 'Attack':
        hide_dialog()
        draw('Kate', 'Sword')
        character_attack('Bob','Kate')
        character_attack('Kate', 'Bob')
        character_attack('Bob', 'Kate')
        character_attack_success('Kate', 'Bob')
        die_character('Bob')
        pocket('Kate', 'Sword')
        exit_place('Kate', 'Camp.Exit')
        enter_place('kate', 'City.NorthEnd')


def talktosunny(self, character1, character2):
     character_walk(character1, character2)
     setLeft(character1)
     setRight(character2)
     set_dialog('Kate: hailo! kya haal hai ?')
     set_dialog('Sunny: are! main achchha hoon. aap ghaayal dikh rahe hain, aapake saath kya hua?')
     set_dialog('Kate: mera haal hee mein jhagada hua tha isalie main ghaayal ho gaya. kya aap mujhe bata sakate hain ki kya koee jagah hai jahaan mujhe upachaar aushadhi mil sakatee hai?')
     set_dialog('Sunny: haan yakeenan! yah sirph aapake saamane hai. kya aap bhoore rang ke ghar ka daravaaja dekh pa rahe hain? .')
     set_dialog('Kate: haan main vah dekh sakata hoon.')
     set_dialog('Sunny: bas us daravaaje mein pravesh karen, aap vahaan upachaar aushadhi praapt kar sakate hain.')
     set_dialog('Kate: bahut-bahut dhanyavaad!!')
     set_dialog('Sunny: koee baat nahin. khyaal rakhana! \\n[ continue | jaaree rakhen]')
     show_dialog()
     while 1:
         if 'continue' in input():
            select ='continue'
            break
     if select == 'continue':
         hide_dialog()
     
         


def talktoSteve(self, character1, character2):
    character_walk(character1, character2)
    set_right(character1)
    set_left(character2)
    set_dialog('Steve: hailo! main tumhaaree kya madad kar sakata hoon ')
    set_dialog('Kate: mujhe heeling pojeeshan chaahie, kya aapake paas hai ? ')
    set_dialog('Steve: haan, mere paas ek hai ')
    set_dialog('Kate: theek hai, isakee keemat kitanee hai.')
    set_dialog('Steve: isaka ek sone ka sikka  .')
    set_dialog('Kate: main vah aushadhi lena chaahata hoon\\n[ Continue | jaaree rakhen]')
    show_dialog()
    while 1:
         if 'continue' in input():
            select ='continue'
            break
     if select == 'continue':
         hide_dialog()
         take_item('Steve', 'GreenPotion', 'Blacksmith.Anvil' )
         give_item('Coin', 'Kate', 'Steve')
         character_drink('Kate')
     



def talktotom(self, character1, character2):
     character_walk(character1, character2)
     setLeft(character1)
     setRight(character2)
     set_dialog('Tom: chaabee mujhe do')
     set_dialog('Kate: main chaabee nahin doonga... mujhase door chale jao varana...main tumhen maar doonga..')
     set_dialog('Tom: theek!\\n[ kill | maarana]')
     show_dialog()
     while 1:
         if 'continue' in input():
            select ='continue'
            break
     if select == 'Kill':
        hide_dialog()
        draw('Kate', 'Sword')
        character_attack('Kate', 'Tom')
        character_attack('Tom', 'Kate')
        character_attack_success('Kate', 'Tom')
        die_character('Tom')
        pocket('Kate', 'Sword')
        exit_place('Kate', 'ForestPath.Exit')
        enter_place('Kate', 'Bridge.SouthEnd')


#def talktopeter(self, character1, character2):
     character_walk(character1, character2)
     setLeft(character1)
     setRight(character2)
     set_dialog('Peter: are ket, tum yahaan kya kar rahee ho?')
     set_dialog('Kate: haay .. mainne raaja dvaara ek kaary saumpa hai')
     set_dialog('Peter: oh kool .. kya kaam hai? ')
     set_dialog('Kate: mujhe raaja ko chaabee surakshit roop se saumpane kee jaroorat hai taaki raajy ka khajaana surakshit haathon mein rahe...')
     set_dialog('Peter: jee aapake lie shubhakaamanaen')
     set_dialog('Kate: alavida.. dhanyavaad main aapase baad mein miloonga')
     show_dialog()
     while 1:
         if 'continue' in input():
            select ='continue'
            break
     if select == 'Kill':
        hide_dialog()
        draw('Kate', 'Sword')
        character_attack('Kate', 'Tom')
        character_attack('Tom', 'Kate')
        character_attack_success('Kate', 'Tom')
        die_character('Tom')
        pocket('Kate', 'Sword')
        exit_place('Kate', 'ForestPath.Exit')
        enter_place('Kate', 'Bridge.SouthEnd')


#def talktolily(self, character1, character2):
     character_walk(character1, character2)
     setLeft(character1)
     setRight(character2)
     set_dialog('Lily: ket, tumhen chaabee mil gaee...mujhe yah chaahie..bas mujhe de do nahin to yah tumhaare lie achchha nahin hoga.')
     set_dialog('Kate: nahin, main ise aapako nahin de sakata.')
     set_dialog('Lily: theek! aaie dekhate hain...\\n[ Attack | aakraman karana]')
     show_dialog()
     while 1:
         if 'continue' in input():
            select ='continue'
            break
     if select == 'Attack':
        hide_dialog()
        draw('Kate', 'Sword')
        character_attack('Lily', 'Kate')
        character_attack('Kate', 'Lily')
        character_attack('Kate', 'Lily')
        character_attack_success('Kate', 'Lily')
        die_character('Lily')
        pocket('Kate', 'Sword')
        exit_place('Kate', 'AlchemyShop.BackDoor')
        enter_place('Kate', 'CastleBedroom.Door')


def talktokim(self, character1, character2):
    character_walk(character1, character2)
    set_right(character1)
    set_left(character2)
    set_dialog('Kim: tum kaun ho?')
    set_dialog('Kate: main ket hoon')
    set_dialog('Kim: sunane kyon aae')
    set_dialog('Kate: mujhe aapakee madad chaahie..')
    set_dialog('Kim:  aapako kya madad chaahie?')
    set_dialog('Kate: mujhe thietar ke lie jagah kee disha chaahie mujhe kaimpas chaahie kya aap mujhe kaimpas de sakate hain')
    set_dialog('Kim:  theek hai..main aapakee madad karoonga..suno kampaas hai\\n[continue | jaaree rakhen]')
    show_dialog()
    while 1:
        if 'continue' in input():
           select ='continue'
           break
    if select == 'continue':
        hide_dialog()
        pocket('Kate', 'Compass')
        exit_place('Kate', 'Tavern.BackDoor')
        enter_place('Kate', 'Courtyard.Gate')

def talktoJerry(self, character1, character2):
    character_walk(character1, character2)
    set_right(character1)
    set_left(character2)
    set_dialog('Jerry: aapako kya chaahie?')
    set_dialog('Kate: mujhe bhookh lagee hai kya aap mujhe khaana de sakate hain...')
    set_dialog('Jerry: theek hai main tumhen khaana de sakata hoon.')
    set_dialog('Kate: shukriya ')
    set_dialog('Jerry:  apana khaana lo\\n[continue | jaaree rakhen]') 
    show_dialog()
    while 1:
        if 'RedPotion,Bottle,Bread' in input():
           select ='RedPotion,Bottle,Bread'
           break
   
    if select == 'RedPotion':
        hide_dialog()
        take_item('Jerry', 'RedPotion', 'Courtyard.BigStall.Left')
        give_item('RedPotion', 'Jerry', 'Kate')
        character_drink('Kate')
        die_character('Kate')
        set_position('BlueKey', 'Courtyard.Barrel')
    elif select == 'Bottle':
        take_item('Jerry', 'Bottle', 'Courtyard.BigStall.Right')
        give_item('Bottle', 'Jerry', 'Kate')
        setRight(character1)
        setLeft(character2)
        set_dialog('Jerry: Give me that key')
        set_dialog('Kate: nahin, main ise aapako nahin de sakata.\\n[Attack | aakraman karana]')
        show_dialog()
        while 1:
            if 'Attack' in input():
               select ='Attack'
               break
        character_attack('Kate', 'Jerry')
        character_attack('Jerry', 'Kate')
        character_attack_success('Kate', 'Jerry')
        exit_place('Kate', 'Courtyard.Gate' )
        enter_place('Kate', 'CastleCrossroads.Gate')
        
    elif select == 'Bread':
        take_item == ('Jerry', 'Bottle', 'Courtyard.SmallStall')
        give_item('Bread', 'Jerry', 'Kate')
    
    
def talktoMike(self, character1, character2):
    character_walk(character1, character2)
    set_right(character1)
    set_left(character2)
    set_dialog('Mike: hailo ket raajy mein aapakee peeth')
    set_dialog('Kate: aan...jems mujhe khoee huee chaabee mil gaee')
    set_dialog('Mike: jao ... raaja se milo vah tumhaaree saraahana karega')
    set_dialog('Kate:  haan main raaja ko chaabee saump doonga \\n[ continue | jaaree rakhen]')
    show_dialog()
    while 1:
        if 'continue' in input():
           select ='continue'
           break
    if select == 'continue':
        hide_dialog()
        exit_place('Kate', 'CastleCrossroads.Gate')
        enter_place('Kate', 'CastleBedroom.Door')
       
         

def talktojames(self, character1, character2):
     character_walk(character1, character2)
     setLeft(character1)
     setRight(character2)
     set_dialog('Kate: hailo king jems...mujhe khoee huee chaabee mil gaee')
     action(f'Wait(2.5)')
     set_dialog('James: oh...bahut badhiya! kahaan hai?')
     set_dialog('Kate: yah raha')
     set_dialog('James: bahut bahut dhanyavaad ket.\\n[continue | jaaree rakhen]')
     show_dialog()
     while 1:
         if 'continue' in input():
            select ='continue'
            break
     if select == 'continue':
         hide_dialog()
         give_item('BlueKey', 'Kate', 'James')

#def talktorobert(self, character1, character2):
     character_walk(character1, character2)
     setLeft(character1)
     setRight(character2)
     set_dialog('James: robart, mujhe vah cheejen do jo seene mein hain?')
     set_dialog('Robert: zaroor raaja!\\n[continue | jaaree rakhen]')
     show_dialog()
     while 1:
         if 'continue' in input():
            select ='continue'
            break
     if select == 'continue':
         hide_dialog()
         give_item('GoldCup', 'James', 'Kate')
         

     
