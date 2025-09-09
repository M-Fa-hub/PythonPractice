from members import Member
from MediaItem import Book
from admin import Loan
from database import DatabaseManager
import datetime

db = DatabaseManager()

# Create and insert a member
m1 = Member("M001", "Alice", "alice@mail.com", "Student", phone="123456")
db.add_member(m1)

# Create and insert a book
b1 = Book("B001", "1984", "George Orwell", 1949, "Available", 14, "Secker & Warburg", 328, "9780451524935")
db.add_item(b1)

# Create and insert a loan
loan = Loan(None, m1, b1, datetime.date.today().isoformat(), (datetime.date.today() + datetime.timedelta(days=14)).isoformat())
db.add_loan(loan)
