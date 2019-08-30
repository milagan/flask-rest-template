import unittest

from model.BookModel import Book


class ModelTests(unittest.TestCase):
    def test_get_all_books(self):
        books = Book.get_all_books()
        self.assertIsNotNone(books, "Books should not be None")

    def test_add_book(self):
        status = Book.add_book("Sample Book", 1.99, 12345678)
        self.assertTrue(status, "Book should be added")

    def test_get_book(self):
        book = Book.get_book(123456789)
        self.assertIsNotNone(book, "Book should not be None")

    def test_delete_book(self):
        status = Book.delete_book(12345678)
        self.assertTrue(status, "Book should be deleted")

    def test_update_book(self):
        status = Book.update_book_price(123456789, 1.99)
        self.assertTrue(status, "Book price should be updated")
        status = Book.update_book_name(123456789, "Book 1")
        self.assertTrue(status, "Book name should be updated")

    def test_replace_book(self):
        status = Book.replace_book(123456789, "Book 2", 2.99)
        self.assertTrue(status, "Book name should be replaced")
