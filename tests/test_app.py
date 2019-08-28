import unittest

from main.app import app, valid_book_object


class EndpointTests(unittest.TestCase):
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


class HelperMethodsTests(unittest.TestCase):
    def test_valid_book_object_valid(self):
        valid_object = {
            'name': 'A',
            'price': 2.75,
            'isbn': 12345
        }
        valid = valid_book_object(valid_object)
        self.assertTrue(valid, 'Book object should be valid')

    def test_valid_book_object_empty(self):
        invalid_object = {
        }
        valid = valid_book_object(invalid_object)
        self.assertTrue(not valid, 'Book object should be invalid')

    def test_valid_book_object_missing_isbn(self):
        invalid_object = {
            'name': 'A',
            'price': 2.75
        }
        valid = valid_book_object(invalid_object)
        self.assertTrue(not valid, 'Book object should be invalid')

    def test_valid_book_object_missing_name(self):
        invalid_object = {
            'price': 2.75,
            'isbn': 12345
        }
        valid = valid_book_object(invalid_object)
        self.assertTrue(not valid, 'Book object should be invalid')

    def test_valid_book_object_missing_price(self):
        invalid_object = {
            'name': 'A',
            'isbn': 12345
        }
        valid = valid_book_object(invalid_object)
        self.assertTrue(not valid, 'Book object should be invalid')
