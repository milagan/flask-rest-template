import unittest

from flask import json

from main.app import app, valid_book_object, valid_put_request_data


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

    def test_login_status_code(self):
        user_account = {
            'username': 'maurice',
            'password': 'password'
        }
        response = self.app.post('/login', data=json.dumps(user_account),
                                 content_type='application/json')
        self.assertEqual(response.status_code, 200)

    def test_login_status_code_401(self):
        user_account = {
            'username': 'invalid',
            'password': 'password'
        }
        response = self.app.post('/login', data=json.dumps(user_account),
                                 content_type='application/json')
        self.assertEqual(response.status_code, 401)

    def test_books_status_code(self):
        response = self.app.get('/books')
        self.assertEqual(response.status_code, 200)

    def test_books_by_isbn_status_code(self):
        response = self.app.get('/books/98765')
        self.assertEqual(response.status_code, 200)

    def test_add_books_status_code(self):
        valid_object = {
            'name': 'A',
            'price': 2.75,
            'isbn': 98765
        }
        response = self.app.post('/books', data=json.dumps(valid_object),
                                 content_type='application/json')
        self.assertEqual(response.status_code, 201)

    def test_add_books_status_code_400(self):
        invalid_object = dict(
        )
        response = self.app.post('/books', data=json.dumps(invalid_object),
                                 content_type='application/json')
        self.assertEqual(response.status_code, 400)

    def test_replace_books_status_code(self):
        valid_object = {
            'name': 'Updated name',
            'price': 10.75
        }
        response = self.app.put('/books/98765', data=json.dumps(valid_object),
                                content_type='application/json')
        self.assertEqual(response.status_code, 204)

    def test_replace_books_status_code_400(self):
        valid_object = {
            'name': 'Updated name'
        }
        response = self.app.put('/books/98765', data=json.dumps(valid_object),
                                content_type='application/json')
        self.assertEqual(response.status_code, 400)

    def test_update_books_status_code(self):
        valid_object = {
            'name': 'Updated name'
        }
        response = self.app.patch('/books/98765', data=json.dumps(valid_object),
                                  content_type='application/json')
        self.assertEqual(response.status_code, 204)

        valid_object = {
            'price': 1.00
        }
        response = self.app.patch('/books/98765', data=json.dumps(valid_object),
                                  content_type='application/json')
        self.assertEqual(response.status_code, 204)

    def test_delete_books_status_code(self):
        valid_object = {
            'name': 'A',
            'price': 2.75,
            'isbn': 12345
        }
        response = self.app.post('/books', data=json.dumps(valid_object),
                                 content_type='application/json')
        self.assertEqual(response.status_code, 201)
        response = self.app.delete('/books/12345')
        self.assertEqual(response.status_code, 204)

    def test_delete_books_status_code_404(self):
        response = self.app.delete('/books/12344')
        self.assertEqual(response.status_code, 404)


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

    def test_valid_put_request_data(self):
        valid_object = {
            'name': 'A',
            'price': 2.75,
            'isbn': 12345
        }
        valid = valid_put_request_data(valid_object)
        self.assertTrue(valid, 'Request data should be valid')
