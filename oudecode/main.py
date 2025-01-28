from signup_module import signup
from signin_module import signin
from utils import load_data, save_data

def main():
    file_path = "data.json"
    users = load_data(file_path)

    while True:
        choice = input("Do you have an account at Elias Bank? (yes/no): ").strip().lower()
        if choice == "yes":
            signin(users)
        elif choice == "no":
            signup(users)
        else:
            print("Invalid choice. Please respond with 'yes' or 'no'.")
            continue

        save_data(users, file_path)
        break


if __name__ == "__main__":
    main()
