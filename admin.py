from datetime import datetime, timedelta
from policy import load_policy

import datetime

polici = load_policy("policies.json")   # Load policy from JSON file

class loan_return:
    def __init__(self, polici, item, member, #loan_id
                 ):
        self.polici = polici
        # self.loan_id = loan_id    call a function to generate unique ID
        self.item = item
        self.member = member

    def create_loan(self):
        self.loan_date = datetime.date.today()
        self.due_date = self.loan_date + datetime.timedelta(days=self.polici.max_loans(self.member.member_type))
        self.status = "active"
        self.renewed_count = 0
    


    def mark_returned(self):
        self.return_date = datetime.date.today()
        self.status = "returned"

    def renew_loan(self):
        if self.status == "active" and self.renewed_count < self.polici.max_renewals(self.item.item_type):
            self.due_date += datetime.timedelta(days=self.polici.max_loans(self.member.member_type))
            self.renewed_count += 1

        return True

    def is_overdue(self):
        if self.status == "active" and self.due_date < datetime.date.today():
            return True
        return False
            
class Reservation():
    def __init__(self, item):
        self.item = item
        self.date = datetime.date.today()
        self.waitlist = []

    def add_to_waitlist(self, member):
        if member.member_id not in self.waitlist:
            self.waitlist.append(member.member_id)
        

    def remove_from_waitlist(self, member):
        if member.member_id in self.waitlist:
            self.waitlist.remove(member.member_id)

    def next_in_waitlist(self):
        if self.waitlist:
            return self.waitlist[0]
        return None



class Fine():
    def __init__(self, polici, member, amount, reason):
        # self.fine_id = fine_id    generate unique ID
        self.polici = polici
        self.member = member
        self.amount = amount
        self.reason = reason
        self.date_issued = datetime.date.today()
        self.paid = False

    def pay_fine(self):
        self.paid = True
        return  f'fine of {self.amount} paid by member {self.member.member_id}'

    def waive_fine(self):
        self.paid = True
        

    def get_fine_details(self):
        return {
            "member": self.member.member_id,
            "amount": self.amount,
            "reason": self.reason,
            "date_issued": self.date_issued,
            "paid": self.paid
        }






