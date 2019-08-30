import unittest

from main.BookModel import Book


class ModelTests(unittest.TestCase):
    @staticmethod
    def test_get_all_books():
        Book.get_all_books()
