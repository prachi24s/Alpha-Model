       def talktosteve(self, character_left, character_right):
                self.setLeft(character_left)
                self.setRight(character_right)
                self.setDialog('Steve: Hi! How can I help you?')
                action(f'Wait(2.5)')
                self.setDialog('Kate: I need healing potion, do you have any?')
                self.setDialog('Steve: Yes, I am having one.')
                self.setDialog('Kate: Fine, how much does it cost?')
                self.setDialog('Steve: Its of one gold coin.')
                self.setDialog('Kate: I want to take that potion.')
                self.setDialog('Steve: Okay!\\n[ continue | continue]')
                self.showDialog()
                choice = waitForChoice(['continue'])
                if choice == 'continue':
                        self.hideDialog()
                        return True

        def talktojames(self, character_left, character_right):
                self.setLeft(character_left)
                self.setRight(character_right)
                self.setDialog('Kate: Hello king James, I found the lost key')
                action(f'Wait(2.5)')
                self.setDialog('James: Ohh...Thats great! Where is it?')
                self.setDialog('Kate: Here it is')
                self.setDialog('James: Thank you so much Kate.\\n[continue | continue]')
                self.showDialog()
                choice = waitForChoice(['continue'])
                if choice == 'continue':
                        self.hideDialog()
                        return True
