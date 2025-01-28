from signup_module import signup_function
from signin_module import signin_function
from utils import load_data, save_data
import tkinter as tk
import customtkinter as ctk
# to do, make the login and signup functions work with the interface, improve interface, add more features, try database vs json.
#For later encryption, hashing, and salting. Develop app full and handle all logic client side. Then expant and deploy serverside logic with interface on client side.
#Make an admin panel on client side with a login. When serverside is established, make a server side admin panel.
#also write a report on what i learned and have done in this project.
def show_home_page():
    for widget in Mainwindow.winfo_children():
        widget.destroy()

    # Create a central frame to hold the widgets
    frame = ctk.CTkFrame(Mainwindow)
    frame.pack(expand=True)  # Center the frame both horizontally and vertically

    # Add a logo
    logo = ctk.CTkLabel(frame, text="Elias Bank", font=("Arial", 24))
    logo.pack(pady=20)

    label1 = ctk.CTkLabel(frame, text="Do you have an account at Elias Bank?")
    label1.pack(pady=10)

    # Buttons in a horizontal layout
    button_frame = ctk.CTkFrame(frame)
    button_frame.pack(pady=20)

    yesbutton = ctk.CTkButton(button_frame, text="Yes", command=show_login_page)
    yesbutton.pack(side="left", padx=20)

    nobutton = ctk.CTkButton(button_frame, text="No", command=show_signup_page)
    nobutton.pack(side="left", padx=20)
def loginfuncwrapper(login_username, login_password):
        if signin_function(login_username, login_password):
            customer_page()
        else:
            print("Login failed. Please try again.")



def show_login_page():
    for widget in Mainwindow.winfo_children():
        widget.destroy()

    frame = ctk.CTkFrame(Mainwindow)
    frame.pack(expand=True)

    label = ctk.CTkLabel(frame, text="Login Page")
    label.pack(pady=20)

    username_label = ctk.CTkLabel(frame, text="Username")
    username_label.pack(pady=5)
    login_username_entry = ctk.CTkEntry(frame)
    login_username_entry.pack(pady=5)

    password_label = ctk.CTkLabel(frame, text="Password")
    password_label.pack(pady=5)
    login_password_entry = ctk.CTkEntry(frame, show="*")
    login_password_entry.pack(pady=5)
    login_username=login_username_entry.get()
    login_password=login_password_entry.get()
    login_button = ctk.CTkButton(frame, text="Login", command=lambda: loginfuncwrapper(login_username, login_password))
    login_button.pack(pady=20)
    back_button = ctk.CTkButton(frame, text="Back", command=show_home_page)
    back_button.pack(pady=20)

def show_signup_page():
    for widget in Mainwindow.winfo_children():
        widget.destroy()

    frame = ctk.CTkFrame(Mainwindow)
    frame.pack(expand=True)

    label = ctk.CTkLabel(frame, text="Signup Page")
    label.pack(pady=20)

    username_label = ctk.CTkLabel(frame, text="Username")
    username_label.pack(pady=5)
    username_entry = ctk.CTkEntry(frame)
    username_entry.pack(pady=5)

    password_label = ctk.CTkLabel(frame, text="Password")
    password_label.pack(pady=5)
    password_entry = ctk.CTkEntry(frame, show="*")
    password_entry.pack(pady=5)

    confirm_password_label = ctk.CTkLabel(frame, text="Confirm Password")
    confirm_password_label.pack(pady=5)
    confirm_password_entry = ctk.CTkEntry(frame, show="*")
    confirm_password_entry.pack(pady=5)

    signup_button = ctk.CTkButton(frame, text="Signup", command=lambda: signup_fucntion(users))
    signup_button.pack(pady=20)

    back_button = ctk.CTkButton(frame, text="Back", command=show_home_page)
    back_button.pack(pady=20)
    passwordentered=password_entry.get()
    usernameentered=username_entry.get()
    confirm_passwordentered=confirm_password_entry.get()

def customer_page():
    for widget in Mainwindow.winfo_children():
        widget.destroy()

    frame = ctk.CTkFrame(Mainwindow)
    frame.pack(expand=True)

    label = ctk.CTkLabel(frame, text="Welcome to Elias Bank")
    label.pack(pady=20)

    deposit_button = ctk.CTkButton(frame, text="Deposit")
    deposit_button.pack(pady=20)

    withdrawal_button = ctk.CTkButton(frame, text="Withdrawal")
    withdrawal_button.pack(pady=20)

    balance_button = ctk.CTkButton(frame, text="Check Balance")
    balance_button.pack(pady=20)

    logout_button = ctk.CTkButton(frame, text="Logout")
    logout_button.pack(pady=20)

    # Add functionality to the buttons
def main():
    global Mainwindow, users
    Mainwindow = ctk.CTk()
    Mainwindow.state('zoomed')  # Fill the screen
    file_path = "data.json"
    users = load_data(file_path)
    show_home_page()
    Mainwindow.mainloop()

if __name__ == "__main__":
    main()
