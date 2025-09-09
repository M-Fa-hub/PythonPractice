
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

