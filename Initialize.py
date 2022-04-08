from Action import *
from Character import *
from Place import *
from Item import *
from Dialog import *

class Initialize:

    def __init__(self):
        self.initialize()
        self.setCameraFocus('Kate') 
        self.showMenu()


    def initialize(self):

        self.storage = Place('Storage', 'Storage')
        self.kate = Character('Kate', 'C', 'Spiky', 'LightArmour', 'Storage')
        self.sword = Item('Sword', 'Sword', 'Storage.Shelf.Left')
        self.key = Item('BlueKey', 'BlueKey', 'Storage.Shelf.Right')
        self.coin = Item('Coin', 'Coin', 'Storage.Barrel')
        self.storage.enableIcon('Exit_Storage', 'Open', 'Storage.Door', 'Enter the Camp', True)
        self.storage.enableIcon('Select_Sword', 'Select', self.sword.item_name, "Sword", True)
        self.storage.enableIcon('Select_BlueKey', 'Select', self.key.item_name, "BlueKey", True)
        self.storage.enableIcon('Select_Coin', 'Select', self.coin.item_name, "Coin", True)
        self.camp = Place('Camp', 'Camp')
        self.bob = Character('Bob', 'F', 'Spiky', 'Bandit', 'Camp.RightLog')
        self.camp.enableIcon('Talk_Bob', 'Talk', self.bob.name, "Talk to the Bob", True)
        self.dialog = Dialog()
        
        self.city = Place('City', 'City')
        self.sunny = Character('Sunny', 'B', 'Long', 'Peasant', 'City.Bench')
        sit(self.sunny, 'City.Bench')
        self.city.enableIcon('Talk_Sunny', 'Talk', self.sunny.name, "Talk to the Sunny", True)
        
        self.blacksmith = Place('Blacksmith', 'Blacksmith')
        self.city.enableIcon('Exit_City', 'Open', 'City.BrownHouseDoor', 'Enter the Blacksmith', True)
        self.steve = Character('Steve', 'D', 'Spiky', 'Merchant', 'Blacksmith.Chest')
        self.city.enableIcon('Talk_Steve', 'Talk', self.steve.name, "Talk to the Steve", True)
        self.potion = Item('GreenPotion', 'GreenPotion', 'Blacksmith.Anvil')
        self.blacksmith.enableIcon('Exit_Blacksmith', 'Open', 'Blacksmith.BackDoor', 'Enter the Forest', True)
        self.forest = Place('ForestPath', 'ForestPath')
        self.bedroom = Place('CastleBedroom', 'CastleBedroom')
        self.james = Character('James', 'B', 'Mage_Beard', 'King', 'CastleBedroom.Bed')
        self.bedroom.enableIcon('Talk_James', 'Talk', self.james.name, "Talk to the James", True)
        
    def setCameraFocus(self, entity_name):
        action(f'SetCameraFocus({entity_name})')

    def showMenu(self):
        action('ShowMenu()')
    
    def hideMenu(self):
        action('HideMenu()')
    
    def enableInput(self):
        action('EnableInput()')

    def disableInput(self):
        action('DisableInput()')
    
    def showCredits(self):
        action('ShowCredits()')

    def hideCredits(self):
        action('HideCredits()')
    
    def quit(self):
        action('Quit()')

    def startGame(self):
        self.hideMenu()
        # Opening scene narration message
        message = "Welcome to THE LOST KEY! Your name is Kate and you found the lost key of King's treasure house. The bandit, Bob wants to get key from you. Your goal is to protect key from bandit and other people and bring that key safely to the King."
        self.showNarration(message)
        self.enableInput()

    def showNarration(self, message):
        action(f'SetNarration("{message}")')
        action('ShowNarration()')

    def hideNarration(self):
        action('HideNarration()')

    def take_sword(self):
        Take(self.kate, self.sword, 'Storage.Shelf')
        
    def take_key(self):
        Take(self.kate, self.key, 'Storage.Shelf')
        pocket(self.kate, self.key)
        
    def take_coin(self):
        Take(self.kate, self.coin, 'Storage.Barrel')
        pocket(self.kate, self.coin)
    
    def enter_camp(self):
        Leave(self.kate, 'Storage.Door', 'Camp.Exit')
        
    def enter_blacksmith(self):
        Leave(self.kate, 'City.BrownHouseDoor', 'Blacksmith.Door')

    def talkTobob(self):
        action(f'WalkTo({self.kate.name}, {self.bob.name})')
        flag = self.dialog.talktobob(self.kate, self.bob)
        if flag:
           action(f'Draw(Kate, Sword)')
           Fight(self.kate, self.bob)
           Die(self.bob)
           pocket(self.kate, self.sword)
           Leave(self.kate, 'Camp.Exit', 'City.NorthEnd')


    def talkTosunny(self):
        action(f'WalkTo({self.kate.name}, {self.sunny.name})')
        flag = self.dialog.talktosunny(self.kate, self.sunny)


    def talkTosteve(self):
        action(f'WalkTo({self.kate.name}, {self.steve.name})')
        flag = self.dialog.talktosteve(self.kate, self.steve)
        if flag:
           Take(self.steve, self.potion, 'Blacksmith.Anvil' )
           Give(self.kate, self.coin, self.steve)
           drink(self.kate)
           
           
    def talkTojames(self):
        action(f'WalkTo({self.kate.name}, {self.james.name})')
        flag = self.dialog.talktojames(self.kate, self.james)
        Give(self.kate, self.key, self.james)
           
    def exit_blacksmith(self):
         Leave(self.kate, 'Blacksmith.Backdoor', 'ForestPath.EastEnd')
         Leave(self.kate, 'ForestPath.WestEnd', 'CastleBedroom.Door')
         
    
    def forestToCastleBedroom(self):
        Leave(self.kate, 'ForestPath.WestEnd', 'CastleBedroom.Door')
