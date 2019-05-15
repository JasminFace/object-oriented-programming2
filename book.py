import random
from datetime import datetime

class Book:

    on_shelf = []
    on_loan = []
    overdue = []

    def __init__(self, title, author, isbn):
        self.title = title
        self.author = author
        self.isbn = isbn

    def borrow(self):
        borrowed = self.lent_out()

        if borrowed == True:
            return False
        else:
            self.on_shelf.remove(self)
            self.on_loan.append(self)
            due_date = self.current_due_date()
            return True
        

    def return_to_library(self):
        borrowed = self.lent_out()

        if borrowed == False:
            return False
        else:
            self.on_loan.remove(self)
            self.on_shelf.append(self)
            due_date = None
            return True

    def lent_out(self):
        for book in Book.on_loan:
            if book == self:
                return True
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
    
    @classmethod
    def overdue_books(cls):
        due_date = cls.current_due_date()

        if due_date < datetime.now:
            Book.overdue.append(cls)
            return True
        else:
            False

    @classmethod
    def browse(cls):
        return random.choice(Book.on_shelf)




bride_collector = Book.create("Bride Collector", "Ted Dekker", 123456789)
chosen = Book.create("Chosen", "Ted Dekker", 987654321)
infidel = Book.create("Infidel", "Ted Dekker", 192837465)

print(Book.browse().title) # Bride Collector
print(Book.browse().title) # Infidel
print(len(Book.on_shelf)) # 3
print(len(Book.on_loan)) # 0
print(bride_collector.lent_out()) # False
print(bride_collector.borrow()) # True
print(len(Book.on_shelf)) # 2
print(len(Book.on_loan)) # 1
print(bride_collector.lent_out()) # True
print(bride_collector.borrow()) # False
print(bride_collector.current_due_date()) # 2019-05-29 16:17:02.261833
print(len(Book.overdue)) # 0
print(bride_collector.return_to_library()) # True
print(bride_collector.lent_out()) # False
print(len(Book.on_shelf)) # 3
print(len(Book.on_loan)) # 0
