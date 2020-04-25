import unittest
from ShippingScreen import ShippingScreen

class TestShippingScreen(unittest.TestCase):
    def test_button_1_click(self):
        shippingScreen = ShippingScreen()
        result = shippingScreen.button_1_click()
        self.assertEqual(result, 'place_order_clicked')


if __name__ == '__main__':
    unittest.main()
