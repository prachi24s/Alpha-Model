from Action import *

class Dialog:

        def __init__(self):
                pass

        def setLeft(self, character):
                action(f'SetLeft({character.name})')

        def setRight(self, character):
                action(f'SetRight({character.name})')

        def showDialog(self):
                action('ShowDialog()')

        def setDialog(self, message):
                action(f'SetDialog("{message}")')
        
        def clearDialog(self):
                action('ClearDialog()')
    
        def hideDialog(self):
                action('HideDialog()')

        def showNarration(self):
                action('ShowNarration()')

        def setNarration(self, message):
                action(f'SetNarration("{message}")')

        def talktobob(self, character_left, character_right):
                self.setLeft(character_left)
                self.setRight(character_right)
                self.setDialog('Bob: Who are you?')
                action(f'Wait(2.5)')
                self.setDialog('Kate: I am Kate')
                self.setDialog('Bob: What are you doing here?')
                self.setDialog('Kate: I am here to take that key and handover it to the king.')
                self.setDialog('Bob:  I want the key...just handover it to me.')
                self.setDialog('Kate: No...just go away from my way\\n[Fight | Fight]')
                self.showDialog()
                choice = waitForChoice(['Fight'])
                if choice == 'Fight':
                        self.hideDialog()
                        return True
                        
        def talktosunny(self, character_left, character_right):
                self.setLeft(character_left)
                self.setRight(character_right)
                self.setDialog('Kate: Hi! How are you?')
                self.setDialog('Sunny: Hey! I am good. You are looking injured what happened with you?')
                self.setDialog('Kate: I had a fight recently thats why I got injured. Can you tell me is there any place where I can get the healing potion?')
                self.setDialog('Sunny: Yeah sure! Its just in front of you. Are you able to see the brown house door? .')
                self.setDialog('Kate: Yes, I can see that.')
                self.setDialog('Sunny: Just enter into that door,you can get the healing potion there.')
                self.setDialog('Kate: Thank you so much!')
                self.setDialog('Sunny: No problem. Take care! \\n[Fight | Fight]')
                self.showDialog()
                choice = waitForChoice(['Fight'])
                if choice == 'Fight':
                        self.hideDialog()
                        return True

        def talktosteve(self, character_left, character_right):
                self.setLeft(character_left)
                self.setRight(character_right)
                self.setDialog('Bob: Who are you?')
                action(f'Wait(2.5)')
                self.setDialog('Kate: I am Kate')
                self.setDialog('Bob: What are you doing here?')
                self.setDialog('Kate: I am here to take that key and handover it to the king.')
                self.setDialog('Bob:  I want the key...just handover it to me.')
                self.setDialog('Kate: No...just go away from my way\\n[Fight | Fight]')
                self.showDialog()
                choice = waitForChoice(['Fight'])
                if choice == 'Fight':
                        self.hideDialog()
                        return True

        def talktojames(self, character_left, character_right):
                self.setLeft(character_left)
                self.setRight(character_right)
                self.setDialog('Bob: Who are you?')
                action(f'Wait(2.5)')
                self.setDialog('Kate: I am Kate')
                self.setDialog('Bob: What are you doing here?')
                self.setDialog('Kate: I am here to take that key and handover it to the king.')
                self.setDialog('Bob:  I want the key...just handover it to me.')
                self.setDialog('Kate: No...just go away from my way\\n[Fight | Fight]')
                self.showDialog()
                choice = waitForChoice(['Fight'])
                if choice == 'Fight':
                        self.hideDialog()
                        return True
