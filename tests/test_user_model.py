import unittest

from model.UserModel import User


class ModelTests(unittest.TestCase):
    def test_repr(self):
        self.assertIsNotNone(repr(User()), "User should have repr")

    def test_get_all_books(self):
        users = User.get_all_users()
        self.assertIsNotNone(users, "Users should not be None")

    def test_username_password_match(self):
        match = User.username_password_match("maurice", "password")
        self.assertTrue(match, "Username and password should match")

    def test_create_user(self):
        User.delete_user('maurice1')
        match = User.create_user("maurice1", "password")
        self.assertTrue(match, "Username and password should be created")


if __name__ == '__main__':
    unittest.main()
