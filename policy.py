# policy.py
import json

class PolicyError(Exception):
    pass

class Policy:
    def __init__(self, data):
        # store the rules
        self.data = data
        self.check_valid()

    def check_valid(self):
        # make sure required keys exist
        if "members" not in self.data:
            raise PolicyError("Missing 'members'")
        if "items" not in self.data:
            raise PolicyError("Missing 'items'")
        if "rules" not in self.data:
            raise PolicyError("Missing 'rules'")

    def max_loans(self, member_type):
        return self.data["members"][member_type]["max_loans"]

    def loan_days(self, item_type):
        return self.data["items"][item_type]["loan_days"]

    def daily_fine(self, item_type):
        return self.data["items"][item_type]["daily_fine"]

    def max_renewals(self, item_type):
        return self.data["items"][item_type]["max_renewals"]



def load_policy(path):
    try:
        with open(path, "r") as f:
            data = json.load(f)
    except FileNotFoundError:
        raise PolicyError("File not found: " + path)
    return Policy(data)
