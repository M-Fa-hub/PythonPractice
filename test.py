import json
import os

print("Current working directory:", os.getcwd())
with open("policies.json", "r") as f:
    data = json.load(f)

print(data)