from abc import ABC, abstractmethod
from datetime import datetime, timedelta

class MediaItem(ABC):

#it is the blue print for other media items
#all the methods and attributes are abstract and must be implemented in the child classes
#all media items must have a title, year, unique serial number, status, loan period, and publisher

    def __init__(self, id, title, author, year, publisher):
        self._id = id # unique identifier
        self._status = "Available"  # Available, Checked Out, Reserved
        self._title = title
        self._author = author
        self._year = year
        self._publisher = publisher
        self._current_borrower = None
        self._due_date = None

    @property
    def id(self):
        return self._id

    @property
    def title(self):
        return self._title

    @property
    def author(self):
        return self._author

    @property
    def status(self):
        return self._status


    def get_due_date(self):
        return self._due_date

    def get_info(self):
        return {
            "id": self._id,
            "title": self._title,
            "author": self._author,
            "year": self._year,
            "status": self._status,
            "publisher": self._publisher
        }

    def is_overdue(self):
        if self._status == "Checked Out" and self._due_date:
            return datetime.now() > self._due_date
        return False

    def is_available(self):
        return self._status == "Available"

class Book(MediaItem):
    def __init__(self, id, title, author, year, publisher, pages, isbn):
        super().__init__(id, title, author, year, publisher)
        self._pages = pages
        self._isbn = isbn
        self.item_type = "Book"

    def get_info(self):
        info = super().get_info()
        info.update({
            "pages": self._pages,
            "isbn": self._isbn,
            "type": "Book"
        })
        return info

class EBook(MediaItem):
    def __init__(self, id, title, author, year, publisher, file_format, file_size):
        super().__init__(id, title, author, year, publisher)
        self._file_format = file_format
        self._file_size = file_size
        self.item_type = "EBook"

    def get_info(self):
        info = super().get_info()
        info.update({
            "file_format": self._file_format,
            "file_size": self._file_size,
            "type": "EBook"
        })
        return info

class AudioBook(MediaItem):
    def __init__(self, id, title, author, year, publisher, narrator, duration):
        super().__init__(id, title, author, year, publisher)
        self._narrator = narrator
        self._duration = duration
        self.item_type = "AudioBook"
        

    def get_info(self):
        info = super().get_info()
        info.update({
            "narrator": self._narrator,
            "duration": self._duration,
            "type": "AudioBook"
        })
        return info