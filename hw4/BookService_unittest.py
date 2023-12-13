import unittest
from unittest.mock import Mock

from BookRepository import BookRepository
from BookService import BookService

class BookServiceTest(unittest.TestCase):
    
    def setUp(self):
        self.bookRepository = Mock(BookRepository)
        self.bookService = BookService(self.bookRepository)

    def test_book_service(self):
        books = [
            (1, "Title1", "Author1"),
            (2, "Title2", "Author2")
        ]
        self.bookRepository.allBooks = books
        result = self.bookService.getAllBooks()
        self.assertEqual(books, result)


# python -m unittest BookService_unittest.py -v