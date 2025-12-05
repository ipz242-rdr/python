from lab8_task9 import User, Privileges, Admin

import unittest


class TestUser(unittest.TestCase):

    def setUp(self):
        self.user = User("Іван", "Петренко", "ivan@email.com", "ivans", True)

    def test_init_correct(self):
        self.assertEqual(self.user.first_name, "Іван")
        self.assertEqual(self.user.login_attempts, 0)
        self.assertTrue(self.user.newsletter_subscription)

    def test_validation_errors(self):
        with self.assertRaises(ValueError):
            User("", "Петренко", "mail", "nick")  # Пусте ім'я
        with self.assertRaises(ValueError):
            User("Іван", "Петренко", "mail", "nick", "NotBoolean")  # Не булева розсилка

    def test_login_logic(self):
        self.assertEqual(self.user.login_attempts, 0)

        self.user.increment_login_attempts()
        self.assertEqual(self.user.login_attempts, 1)

        self.user.increment_login_attempts()
        self.assertEqual(self.user.login_attempts, 2)

        self.user.reset_login_attempts()
        self.assertEqual(self.user.login_attempts, 0)

    def test_greeting(self):
        expected = "привіт, Іван. Ласкаво просимо"
        self.assertEqual(self.user.greeting_user(), expected)


class TestPrivileges(unittest.TestCase):

    def test_init_default(self):
        priv = Privileges()
        self.assertEqual(priv.privileges, [])

    def test_init_validation(self):
        with self.assertRaises(ValueError):
            Privileges("Це рядок, а не список")

    def test_show_privileges_content(self):
        data = ["Видалення", "Бан"]
        priv = Privileges(data)
        output = priv.show_privileges()
        self.assertIn("Видалення", output)
        self.assertIn("Бан", output)


class TestAdmin(unittest.TestCase):

    def setUp(self):
        self.admin = Admin("Адмін", "Головний", "admin@site.com", "root")

    def test_inheritance(self):
        self.assertEqual(self.admin.first_name, "Адмін")
        self.admin.increment_login_attempts()
        self.assertEqual(self.admin.login_attempts, 1)

    def test_composition(self):
        self.assertIsInstance(self.admin.priv, Privileges)

        rights = self.admin.priv.privileges
        self.assertIn("Дозволено видаляти користувачів", rights)
        self.assertEqual(len(rights), 4)

    def test_show_privileges_via_admin(self):
        output = self.admin.priv.show_privileges()
        self.assertIn("Дозволено змінювати налаштування", output)


if __name__ == '__main__':
    unittest.main()