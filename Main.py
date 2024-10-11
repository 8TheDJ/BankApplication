import time
import os
import json
import GroupFunctions1
# user gegevens in een Json stoppen, account aanmaken en registratie voor de bank, uiteindelijke scenario in een GUI zetten

filepath=os.path.join(os.path.dirname(__file__),'data.json')
if not os.path.exists(filepath):
    with open(filepath, 'w') as f:
        f.write('{}')

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

while True:
    choice1 = input("Do you have a current account at Elias Bank? Please respond with 'yes' or 'no'. ").lower()
    if choice1 == "yes":
        print("Enter your username and password to enter your account.")
        break  
    elif choice1 == 'no':
        while True:
            choice2 = input("Do you want to make an account? Please respond with 'yes' or 'no'. ").lower()
            if choice2 == "yes":
                #enter function that makes an account
                break
            elif choice2 == "no":
                print("Thank you for your time. Goodbye!")
                break 
            else:
                print("Invalid input. Please respond with 'yes' or 'no'.")
        break
    else:
        print("Invalid input. Please respond with 'yes' or 'no'.") 

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

    # Add the new username to the data
    data[username] = {"username": username,
                      "password": password}  # Add more info here as needed

    # Write the updated data back to the file
    with open(file_path, 'w') as f:
        json.dump(data, f, indent=4)

    print(f"Username '{username}' and password have been successfully added.")

def signin():
    pass

