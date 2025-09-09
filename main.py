# main.py
from policy import load_policy

p = load_policy("policies.json")

print("Student max loans:", p.max_loans("Student"))
print("Book loan days:", p.loan_days("Book"))
print("Fine per day for Book:", p.daily_fine("Book"))
print("Grace days for Staff:", p.grace_days("Staff"))
