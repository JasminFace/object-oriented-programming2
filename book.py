import random
from datetime import datetime

class Book:

    on_shelf = []
    on_loan = []

    def __init__(self, title, author, isbn):
        self.title = title
        self.author = author
        self.isbn = isbn
    
    # def borrow(self):
    
    # def return_to_library(self):
    
    # def lent_out(self):

    @classmethod
    def create(cls, title, author, isbn):
        new_book = Book(title, author, isbn)
        cls.on_shelf.append(new_book)
        return new_book

    
    # @classmethod
    # def current_due_date(cls):
    
    # @classmethod
    # def overdue_books(cls):
    
    @classmethod
    def browse(cls):
        return random.choice(Book.on_shelf)

harry = Book.create("Harry", "John", 1234)
print(Book.on_shelf)