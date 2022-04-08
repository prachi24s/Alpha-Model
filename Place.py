from Action import *

class Place:
    def __init__(self, place, name):
        self.place = place
        self.name = name
        self.createPlace()
        
    def createPlace(self):
        return action(f'CreatePlace({self.place}, {self.name})')

    def enableIcon(self, action_name, act, location, message, default):
        return action(f'EnableIcon("{action_name}", {act}, {location}, "{message}", {default})')
    
    def disableIcon(self, action_name, entity_name):
        return action(f'DisableIcon("{action_name}", {entity_name})')
