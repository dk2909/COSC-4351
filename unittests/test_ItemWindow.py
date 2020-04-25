import unittest
from ItemWindow import ItemWindow

class TestItemWindow(unittest.TestCase):
    def test_button_1_click(self):
        itemWindow = ItemWindow()
        result = itemWindow.button_1_click()
        self.assertEqual(result, 'add_item_clicked')


if __name__ == '__main__':
    unittest.main()
