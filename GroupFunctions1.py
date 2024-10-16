import time
import os
import json

class Bankaccount:
    def __init__(self, balance= 0):  
        self.balance = float(balance)
        
    def withdrawal(self, amount):
            if amount> self.balance:
                print("Not enough balance to withdrawl.")
            else:
                self.balance = round(self.balance - amount,2)
                print(f"Succesfully withdrawed:{amount}.\n Your current balance is now:{self.balance}.")
    def deposit(self, amount):
            self.balance= round(self.balance + amount,2)
            print(f"You have succesfully deposited{amount}.\n Your balance is now:{self.balance}")
    def check_balance(self):
         print(f"Your balance is {self.balance}")

def signup():
    file_path = 'data.json'
    
    # Load existing data from the file or initialize empty data
    if os.path.exists(file_path):
        with open(file_path, 'r+') as f:
            try:
                data = json.load(f)
            except json.JSONDecodeError:
                data = {}  # Initialize to an empty dict if the file is empty or corrupted
    else:
        data = {}

    while True:
        username = input("Enter your username: ").lower().strip()

        # Check if the username already exists in the data
        if username in data:
            print(f"Username '{username}' already exists. Please choose another one.")
            continue  # Start over if username is taken

        choice3 = input("Are you sure this is the right username? (yes or no): ").lower().strip()

        if choice3 == "yes":
            break  # Exit the loop if the username is confirmed
        elif choice3 == "no":
            print("Please try again.")
        else:
            print("Invalid input. Please answer with 'yes' or 'no'.")
    
    while True:
        password=input("Please enter your password?").strip()
        choicepassword=input("Are you satisfied with this password?\n Please reply with a 'yes' or a 'no'.").lower().strip()
        if choicepassword== 'yes':
            break
        elif choicepassword== 'no':
            print("Please try again.")
        else:
            print("Invalid input. Please answer with 'yes' or 'no'.")
    while True:
        try:
            initial_deposit=float(input('Enter your initial deposit:'))
            break
        except ValueError:
            print("Invalid input, please enter only numbers.")
    account= Bankaccount(initial_deposit)
    
    # Add the new username to the data
    data[username] = {"username": username,
                      "password": password,
                      "account": account}  # Add more info here as needed

    # Write the updated data back to the file
    with open(file_path, 'w') as f:
        json.dump(data, f, indent=4)

    print(f"Username '{username}', password and bankaccount have been successfully added.")

def signin():
    pass
#proberen signin() en de functie waarin je ingelogd je bankaccount kan aanpassen apart maken.