from user_module import User
from utils import load_data, save_data
from TKmain import username_entry, password_entry, customer_page

def signin(users):
    while True:
        username = input("Enter your username: ").strip().lower()
        if username not in users:
            print("User not found. Please try again or sign up first.")
            return

        password = input("Enter your password: ").strip()
        stored_password = users[username]['password']
        if password == stored_password:  # Replace with hashing in a secure system
            print(f"Welcome back, {username}!")
            # Add further operations (e.g., deposit, withdrawal) here.
            break
        else:
            print("Incorrect password. Please try again.")

def signin_function():
    passwordentered = password_entry.get()
    usernameentered = username_entry.get()

    # Add logic to handle the entered username and password
    # For example, you can call the signin function with the entered credentials
    users = load_data()  # Assuming load_data loads the users' data
    if usernameentered in users and users[usernameentered]['password'] == passwordentered:
        customer_page()
        print(f"Welcome back, {usernameentered}!")
    else:
        print("Incorrect username or password. Please try again.")