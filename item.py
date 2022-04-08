from Action import *
    
class Item:
    def __init__(self, item_name, item, position):
        self.item_name = item_name
        self.item = item
        self.position = position
        action('CreateItem('+self.item_name+','+self.item+')')
        action('SetPosition('+self.item_name+','+self.position+')')
        
