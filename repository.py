from typing import Dict
from models import Book

class BookRepository:
    def __init__(self):
        self.books: Dict[int, Book] = {}
    
    def create(self, book: Book):
        self.books[book.id] = book
        return book

    def get(self, book_id: int):
        return self.books.get(book_id)

    def get_all(self):
        return list(self.books.values())

    def update(self, book_id: int, book: Book):
        if book_id in self.books:
            self.books[book_id] = book
            return book
        return None

    def delete(self, book_id: int):
        return self.books.pop(book_id, None)