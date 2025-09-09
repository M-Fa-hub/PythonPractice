
class Member():
    def __init__(self, name, email):
        # self.member_id = call a function to generate unique ID
        # self.member_id = name[:2] + email.split('@')[0][-2:]

        self.name = name
        self.email = email
        self.active_loans = False
        self.borrowed_items = []


    def cearte_account(self):
        return f"Account created for {self.name} with email {self.email} as {self.member_type} member."

    
    def deactivate_account(self):
        if not self.active_loans:
            return f"Account for {self.name} deactivated."
        else:
            return f"Cannot deactivate account for {self.name}. Active loans exist."




class StudentMember(Member):
    def __init__(self, name, email, student_id):
        super().__init__(self, name, email )
        self.student_id = student_id
        self.member_type = "Student"


class StaffMember(Member):
    def __init__(self, name, email, staff_id):
        super().__init__(self, name, email)
        self.staff_id = staff_id
        self.member_type = "Staff"


class ExternalMember(Member):
    def __init__(self, name, email, id_number):
        super().__init__(self, name, email)
        self.id_number = id_number
        self.member_type = "citizen"

