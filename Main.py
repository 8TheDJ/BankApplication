import time
import os
import json
from GroupFunctions1 import *
# user gegevens in een Json stoppen, account aanmaken en registratie voor de bank, uiteindelijke scenario in een GUI zetten

filepath=os.path.join(os.path.dirname(__file__),'data.json')
if not os.path.exists(filepath):
    with open(filepath, 'w') as f:
        f.write('{}')

while True:
    choice1 = input("Do you have a current account at Elias Bank? Please respond with 'yes' or 'no'. ").lower()
    if choice1 == "yes":
        print("Enter your username and password to enter your account.")
        signin()
        break  
    elif choice1 == 'no':
        while True:
            choice2 = input("Do you want to make an account? Please respond with 'yes' or 'no'. ").lower()
            if choice2 == "yes":
                signup()
                break
            elif choice2 == "no":
                print("Thank you for your time. Goodbye!")
                break 
            else:
                print("Invalid input. Please respond with 'yes' or 'no'.")
        break
    else:
        print("Invalid input. Please respond with 'yes' or 'no'.") 



