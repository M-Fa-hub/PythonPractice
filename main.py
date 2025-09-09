# main.py
from policy import load_policy

p = load_policy("policies.json")

print("Max loans for student:", p.members.student.max_loans())