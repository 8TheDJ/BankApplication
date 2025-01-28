from user_module import User, BankAccount

def signup(users):
    while True:
        username = input("Enter your username: ").strip().lower()
        if username in users:
            print(f"Username '{username}' already exists. Please choose another one.")
            continue

        password = input("Enter your password: ").strip()
        confirm_password = input("Confirm your password: ").strip()
        if password != confirm_password:
            print("Passwords do not match. Try again.")
            continue

        try:
            initial_deposit = float(input("Enter your initial deposit: "))
            if initial_deposit < 0:
                raise ValueError
        except ValueError:
            print("Invalid deposit amount. Please enter a positive number.")
            continue

        account = BankAccount(initial_deposit)
        user = User(username, password, account)
        users[username] = user.to_dict()

        print(f"Account successfully created for {username}.")
        break
