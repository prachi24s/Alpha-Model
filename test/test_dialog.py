import unittest
import mocktestdialog

class TestDialog(unittest.TestCase):
    def set_dialog(self):
        self.assertEqual(set_dialog('Kate: I need healing potion, do you have any?'),"succeeded SetDialog(Kate: I need healing potion, do you have any?)")
    
    def set_right(self):
        self.assertEqual(set_right('Kate'),"succeeded SetRight(Kate)")
    
    def set_left(self):
        self.assertEqual(set_left('Bob'),"succeeded SetLeft(Bob)")
