import unittest
from Checkout import Checkout

class TestCheckout(unittest.TestCase):

    def test_home_click(self):
        checkout = Checkout()
        result = checkout.home_click()
        self.assertEqual(result, 'store_home_clicked')

    def test_account_click(self):
        checkout = Checkout()
        result = checkout.account_click()
        self.assertEqual(result, 'account_clicked')

    def test_button_1_click(self):
        checkout = Checkout()
        result = checkout.button_1_click()
        self.assertEqual(result, 'next_clicked')



if __name__ == '__main__':
    unittest.main()
