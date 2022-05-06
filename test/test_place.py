import unittest
import mocktestplace

class TestPlace(unittest.TestCase):
    
    def test_create_place(self):
        self.assertEqual(create_place('Storage','Storage'),"succeeded CreatePlace(Storage,Storage)")
    def test_exit_place(self):
        self.assertEqual(exit_place('Kate','Storage'),"succeeded Exit(Kate, Storage.Door, true)")
    def test_enter_place(self):
        self.assertEqual(enter_place('Kate','Camp'),"succeeded Enter(Kate, Camp.Exit, true)")







