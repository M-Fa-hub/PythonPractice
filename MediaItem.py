from abc import ABC, abstractmethod
from datetime import datetime, timedelta

class MediaItem(ABC):

#it is the blue print for other media items
#all the methods and attributes are abstract and must be implemented in the child classes
#all media items must have a title, year, unique serial number, status, loan period, and publisher

    @abstractmethod
    def __init__(self, id, title, author, year, status, loan_period, publisher):
        self.id = id
        self.title = title
        self.author = author
        self.year = year
        self.status = status
        self.loan_period = loan_period
        self.publisher = publisher


    @abstractmethod
    def check_out(self, borrower):
        pass


    @abstractmethod
    def return_item(self):
        pass


    @abstractmethod
    def get_due_date(self):
        pass



    @abstractmethod
    def get_info(self):
        pass



    @abstractmethod
    def is_overdue(self):
        pass


    @abstractmethod
    def is_available(self):
        pass    



class Book(MediaItem):
    def __init__(self, id, title, author, year, status, loan_period, publisher, pages, isbn):
        super().__init__(id, title, author, year, status, loan_period, publisher) 
        self.pages = pages
        self.isbn = isbn


    
    def check_out(self, borrower):
        pass


    def return_item(self):
        pass


    def get_due_date(self):
        pass



    def get_info(self):
        pass



    def is_overdue(self):
        pass


    def is_available(self):
        pass  

class EBook(MediaItem):
        def __init__(self, id, title, author, year, status, loan_period, publisher, file_format, file_size):
            super().__init__(id, title, author, year, status, loan_period, publisher)
            self.file_format = file_format
            self.file_size = file_size


class AudioBook(MediaItem):
        def __init__(self, id, title, author, year, status, loan_period, publisher, narrator, duration):
            super().__init__(id, title, author, year, status, loan_period, publisher)
            self.narrator = narrator
            self.duration = duration
