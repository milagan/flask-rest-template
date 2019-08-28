import unittest

from main.app import app


class BasicTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        pass

    @classmethod
    def tearDownClass(cls):
        pass

    def setUp(self):
        self.app = app.test_client()
        self.app.testing = True
        pass

    def tearDown(self):
        pass

    def test_books_status_code(self):
        response = self.app.get('/books')
        self.assertEqual(response.status_code, 200)

    def test_books_by_isdn_status_code(self):
        response = self.app.get('/books/12345')
        self.assertEqual(response.status_code, 200)
