import unittest

from main.BookModel import Book


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
