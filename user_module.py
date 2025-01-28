class BankAccount:
    def __init__(self, balance=0.0):
        self.balance = round(float(balance), 2)

    def deposit(self, amount):
        self.balance = round(self.balance + amount, 2)
        print(f"Deposited {amount}. New balance: {self.balance}")

    def withdraw(self, amount):
        if amount > self.balance:
            print("Insufficient balance.")
        else:
            self.balance = round(self.balance - amount, 2)
            print(f"Withdrawn {amount}. New balance: {self.balance}")

    def to_dict(self):
        return {"balance": self.balance}

    @classmethod
    def from_dict(cls, data):
        return cls(data["balance"])


class User:
    def __init__(self, username, password, account):
        self.username = username
        self.password = password  # Use a hashed password in production.
        self.account = account

    def to_dict(self):
        return {
            "username": self.username,
            "password": self.password,
            "account": self.account.to_dict(),
        }

    @classmethod
    def from_dict(cls, data):
        account = BankAccount.from_dict(data["account"])
        return cls(data["username"], data["password"], account)
