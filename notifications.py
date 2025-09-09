
class NotificationService:
    def __init__(self):
        self.subscribers = []

    def add_subscriber(self, member):
        if member not in self.subscribers:
            self.subscribers.append(member)

    def remove_subscriber(self, member):
        if member in self.subscribers:
            self.subscribers.remove(member)

    def send_email(self, member, subject, message):
        # For now, just simulate with a print statement
        print(f"[EMAIL to {member.email}] {subject}\n{message}\n")

    def send_sms(self, member, message):
        # For now, just simulate with a print statement
        print(f"[SMS to {member.name}] {message}\n")

    # New helpers for library events:
    def notify_due_soon(self, loan):
        subject = "Reminder: Item due soon"
        message = f"Dear {loan.member.name},\nYour loan for '{loan.item.title}' is due on {loan.due_date}."
        self.send_email(loan.member, subject, message)

    def notify_overdue(self, loan):
        subject = "Overdue Notice"
        message = f"Dear {loan.member.name},\nYour loan for '{loan.item.title}' is overdue since {loan.due_date}!"
        self.send_email(loan.member, subject, message)

    def notify_reservation_ready(self, member, item):
        subject = "Reservation Available"
        message = f"Dear {member.name},\nThe item '{item.title}' you reserved is now available."
        self.send_email(member, subject, message)
