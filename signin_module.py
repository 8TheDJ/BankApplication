from user_module import User
from utils import load_data, save_data


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

def signin_function(login_username, login_password):
    users = load_data()
    if login_username not in users:
        print("User not found. Please try again or sign up first.")
        return

    stored_password = users[username]['password']
    if password == stored_password:  # Replace with hashing in a secure system
        print(f"Welcome back, {username}!")
        # Add further operations (e.g., deposit, withdrawal) here.
        break
    else:
        print("Incorrect password. Please try again.")
