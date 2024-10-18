import json
import os
import GroupFunctions1
with open('data.json', 'r') as f:
    users = json.load(f)

print(users)  # Print the full dictionary to confirm its structure
print(users.get(username))  # Check if the username exists
print(users.get(username, {}).get('password'))  # Check the password value