import unittest
from unittest.mock import patch
from Store import Store



class TestStore(unittest.TestCase):  # inheriting from unittest.TestCase to access testing capabilities
    def test_button_3_click(self):
        store = Store()
        result = store.button_3_click()
        self.assertEqual(result, 'btn_3_clicked')

    def test_store_btn(self):
        store = Store()
        result = store.store_button_click()
        self.assertEqual(result, 'store_button_clicked')

    def test_button_1_click(self):
        store = Store()
        result = store.button_1_click()
        self.assertEqual(result, 'btn_1_clicked')

    def test_text_box_1_pressed_enter(self):
        store = Store()
        result = store.text_box_1_pressed_enter()
        self.assertEqual(result, 'text_1_pressed')

    def test_sign_in_btn_click(self):
        store = Store()
        result = store.sign_in_btn_click()
        self.assertEqual(result, 'sign_in_btn_click')