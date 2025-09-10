import sqlite3
from datetime import datetime, deltatime

class DatabaseManager:
    def __init__(self, db_name="library.db"):
        self.db_name = db_name
        self.init_database()

    def init_database(self):
        """Create all necessary tables if they don't exist"""
        with sqlite3.connect(self.db_name) as conn:
            cursor = conn.cursor()

            # Members table
            cursor.execute('''
                CREATE TABLE IF NOT EXISTS members (
                    member_id TEXT PRIMARY KEY,
                    name TEXT NOT NULL,
                    email TEXT UNIQUE NOT NULL,
                    phone TEXT,
                    join_date TEXT,
                    status TEXT DEFAULT 'Active'
                )
            ''')

            # Items table
            cursor.execute('''
                CREATE TABLE IF NOT EXISTS items (
                    item_id TEXT PRIMARY KEY,
                    title TEXT NOT NULL,
                    author TEXT,
                    year INTEGER,
                    item_type TEXT NOT NULL,
                    publisher TEXT,
                    status TEXT DEFAULT 'Available'
                )
            ''')

            # Loans table
            cursor.execute('''
                CREATE TABLE IF NOT EXISTS loans (
                    loan_id INTEGER PRIMARY KEY AUTOINCREMENT,
                    member_id TEXT NOT NULL,
                    item_id TEXT NOT NULL,
                    loan_date TEXT,
                    due_date TEXT,
                    return_date TEXT,
                    status TEXT DEFAULT 'active',
                    FOREIGN KEY (member_id) REFERENCES members(member_id),
                    FOREIGN KEY (item_id) REFERENCES items(item_id)
                )
            ''')

            conn.commit()

    # -----------------------------
    # Members
    # -----------------------------
    def add_member(self, member):
        """Insert a new member"""
        try:
            with sqlite3.connect(self.db_name) as conn:
                cursor = conn.cursor()
                cursor.execute('''
                    INSERT INTO members (member_id, name, email, phone, join_date, status)
                    VALUES (?, ?, ?, ?, ?, ?)
                ''', (
                    member.id,
                    member.name,
                    member.email,
                    member.phone,
                    datetime.now().strftime('%Y-%m-%d'),
                    member.status
                ))
                conn.commit()
                return True
        except sqlite3.IntegrityError:
            return False

    def get_member(self, member_id):
        with sqlite3.connect(self.db_name) as conn:
            cursor = conn.cursor()
            cursor.execute('SELECT * FROM members WHERE member_id = ?', (member_id,))
            return cursor.fetchone()

    # -----------------------------
    # Items
    # -----------------------------
    def add_item(self, item):
        with sqlite3.connect(self.db_name) as conn:
            cursor = conn.cursor()
            cursor.execute('''
                INSERT INTO items (item_id, title, author, year, item_type, publisher, status)
                VALUES (?, ?, ?, ?, ?, ?, ?)
            ''', (
                item.id,
                item.title,
                item.author,
                item.year,
                item.item_type,
                item.publisher,
                item.status
            ))
            conn.commit()
            return True

    def get_item(self, item_id):
        with sqlite3.connect(self.db_name) as conn:
            cursor = conn.cursor()
            cursor.execute('SELECT * FROM items WHERE item_id = ?', (item_id,))
            return cursor.fetchone()

    # -----------------------------
    # Loans
    # -----------------------------
    def add_loan(self, member_id, item_id, due_days=14):
        """Create a loan record"""
        loan_date = datetime.now().strftime('%Y-%m-%d')
        due_date = (datetime.now() + deltatime(days=due_days)).strftime('%Y-%m-%d')

        with sqlite3.connect(self.db_name) as conn:
            cursor = conn.cursor()
            cursor.execute('''
                INSERT INTO loans (member_id, item_id, loan_date, due_date, status)
                VALUES (?, ?, ?, ?, 'active')
            ''', (member_id, item_id, loan_date, due_date))
            conn.commit()
            return cursor.lastrowid

    def mark_returned(self, loan_id):
        with sqlite3.connect(self.db_name) as conn:
            cursor = conn.cursor()
            cursor.execute('''
                UPDATE loans
                SET return_date = ?, status = 'returned'
                WHERE loan_id = ?
            ''', (datetime.now().strftime('%Y-%m-%d'), loan_id))
            conn.commit()
            return cursor.rowcount > 0
