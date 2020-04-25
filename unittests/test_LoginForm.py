import unittest
from LoginForm import LoginForm

class TestLoginForm(unittest.TestCase):
    def test_update_login_status(self):
        loginForm = LoginForm()
        result = loginForm.update_login_status()
        self.assertEqual(result, 'login_status_clicked')

    def test_login_btn_click(self):
        loginForm = LoginForm()
        result = loginForm.login_btn_click()
        self.assertEqual(result, 'login_btn_clicked')

    def test_guest_login_btn_clickk(self):
        loginForm = LoginForm()
        result = loginForm.guest_login_btn_click()
        self.assertEqual(result, 'guest_login_clicked')


if __name__ == '__main__':
    unittest.main()
