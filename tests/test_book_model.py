import unittest

from main.BookModel import Book


class ModelTests(unittest.TestCase):
    def test_get_all_books(self):
        books = Book.get_all_books()
        self.assertIsNotNone(books, "Books should not b None")

    def test_get_book(self):
        book = Book.get_book(123456789)
        self.assertIsNotNone(book, "Books should not b None")
