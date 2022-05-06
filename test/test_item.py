import unittest
import mock_test_item

class TestItems(unittest.TestCase):

    def test_create_item(self):
        self.assertEqual(create_item('BlueKey', 'BlueKey'), "succeeded CreateItem(BlueKey,BlueKey)")

    def test_create_item(self):
        self.assertEqual(create_item('BlueKey', 'BlueKey'), "succeeded CreateItem(BlueKey,BlueKey)")
        

if __name__ == "__main__":
    unittest.main()
