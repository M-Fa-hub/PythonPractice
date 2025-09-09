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



class Member():
    def __init__(self, member_id, name, email, member_type, active_loans, fine_account):
        self.member_id = member_id
        self.name = name
        self.email = email
        self.member_type = member_type
        self.active_loans = active_loans
        self.fine_account = fine_account
        self.borrowed_items = []




    def check_out(self, item):
        pass


    def return_item(self, item):
        pass

    def renew(self, item):
        pass


    def reserve(self, item):
        pass


    def pay_fine(self, amount):
        pass

    def get_info(self):
        pass




class StudentMember(Member):
    def __init__(self, member_id, name, email, member_type, active_loans, fine_account, max_loans, student_id):
        super().__init__(member_id, name, email, member_type, active_loans, fine_account)
        self.student_id = student_id
        self.max_load = max_loans
        # self.borrowed_items = []



class StaffMember(Member):
    def __init__(self, member_id, name, email, member_type, active_loans, fine_account, max_loans, staff_id):
        super().__init__(member_id, name, email, member_type, active_loans, fine_account)
        self.staff_id = staff_id
        self.max_load = max_loans
        # self.borrowed_items = []


class ExternalMember(Member):
    def __init__(self, member_id, name, email, member_type, active_loans, fine_account, max_loans, organization, address):
        super().__init__(member_id, name, email, member_type, active_loans, fine_account)
        self.organization = organization
        self.address = address
        self.max_load = max_loans
        # self.borrowed_items = []



class Loan():
    def __init__(self, loan_id, item, member, borrow_date, due_date, return_date=None, renewed_count=0, status='active'):
        self.load_id = loan_id
        self.item = item
        self.member = member
        self.borrow_date = borrow_date
        self.due_date = due_date
        self.return_date = return_date
        self.renewed_count = renewed_count
        self.status = status


    def mark_returned():
        pass

    def renew_loan():
        pass

    def is_overdue():
        pass



class Reservation():
    def __init__(self, reservation_id, item, reservation_date, status='active'):
        self.reservation_id = reservation_id
        self.item = item
        self.reservation_date = reservation_date
        self.status = status

    def add_to_waitlist(self, member):
        pass

    def remove_from_waitlist(self, member):
        pass

    def next_in_waitlist(self):
        pass



class Fine():
    def __init__(self, fine_id, member, amount, reason, status='unpaid'):
        self.fine_id = fine_id
        self.member = member
        self.amount = amount
        self.reason = reason
        self.status = status

    def pay_fine(self, amount):
        pass

    def waive_fine(self):
        pass

    def get_fine_details(self):
        pass

    def is_sttteled():
        pass



class Catalog():
    def __init__(self):
        self.items = []

    def add_item(self, item):
        self.items.append(item)

    def remove_item(self, item):
        self.items.remove(item)

    def search_by_title(self, title):
        pass

    def search_by_author(self, author):
        pass

    def search_by_year(self, year):
        pass

    def search_by_type(self, item_type):
        pass


class NotificationService():

    def __init__(self):
        subscribers = []

    def add_subscriber(self, member):
        pass

    def remove_subscriber(self, member):
        pass

    def send_email(self, member, subject, message):
        pass

    def send_sms(self, member, message):
        pass


