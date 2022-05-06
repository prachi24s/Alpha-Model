import unittest
import mock_test_item

class TestItems(unittest.TestCase):

    def test_create_item(self):
        self.assertEqual(create_item('BlueKey', 'BlueKey'), "succeeded CreateItem(BlueKey,BlueKey)")

    def test_set_position(self):
        self.assertEqual(set_position('BlueKey', 'Storage'), "succeeded SetPosition(BlueKey,Storage.Shelf.Right)")

    def test_take_item(self):
        self.assertEqual(take_item('Sword','Kate', 'BlueKey'), "succeeded TakeItem(Sword,Kate,Storage.Shelf.Left)")

    def test_give_item(self):
        self.assertEqual(give_item('Coin','Kate', 'Steve'), "succeeded GiveItem(Coin,Kate,Steve)")
        

        

        

if __name__ == "__main__":
    unittest.main()
