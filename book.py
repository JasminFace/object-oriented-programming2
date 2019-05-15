import random
from datetime import datetime

class Book:

    on_shelf = []
    on_loan = []

    def __init__(self, title, author, isbn):
        self.title = title
        self.author = author
        self.isbn = isbn
    
    def borrow(self):
        borrowed = self.lent_out()
        due_date = self.current_due_date()

        if borrowed == True:
            return False
        else:
            self.on_shelf.remove(self)
            self.on_loan.append(self)
            return True
        

    # def return_to_library(self):
    
    def lent_out(self):
        for book in Book.on_shelf:
            if book == Book.on_shelf:
                return True
            else:
                return False

    @classmethod
    def create(cls, title, author, isbn):
        new_book = Book(title, author, isbn)
        cls.on_shelf.append(new_book)
        return new_book

    
    @classmethod
    def current_due_date(cls):
        now = datetime.now()
        two_weeks = 60 * 60 * 24 * 14 # two weeks expressed in seconds  
        future_timestamp = now.timestamp() + two_weeks
        return datetime.fromtimestamp(future_timestamp)
    
    # @classmethod
    # def overdue_books(cls):
    
    @classmethod
    def browse(cls):
        return random.choice(Book.on_shelf)

bride_collector = Book.create("Bride Collector", "Ted Dekker", 123456)
print(Book.on_shelf)
print(bride_collector.lent_out())
bride_collector.borrow()
print(Book.on_loan)
