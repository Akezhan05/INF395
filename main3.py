import ttkbootstrap as ttk
from ttkbootstrap.constants import *
from tkinter import messagebox

class BankAccount:
    def __init__(self, account_holder, balance=0):
        self.account_holder = account_holder
        self.balance = balance

    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
            return f"Deposited ₹{amount}. New balance: ₹{self.balance}"
        else:
            return "Invalid deposit amount."

    def withdraw(self, amount):
        if 0 < amount <= self.balance:
            self.balance -= amount
            return f"Withdrew ₹{amount}. New balance: ₹{self.balance}"
        else:
            return "Insufficient funds or invalid amount."

    def check_balance(self):
        return f"Account balance for {self.account_holder}: ₹{self.balance}"

    def __str__(self):
        return f"Account Holder: {self.account_holder}, Balance: ₹{self.balance}"


class BankSystem:
    def __init__(self):
        self.accounts = {}

    def create_account(self, name, initial_deposit=0):
        if name not in self.accounts:
            self.accounts[name] = BankAccount(name, initial_deposit)
            return f"Account created for {name} with an initial deposit of ₹{initial_deposit}."
        else:
            return "Account already exists."

    def delete_account(self, name):
        if name in self.accounts:
            del self.accounts[name]
            return f"Account for {name} deleted successfully."
        else:
            return "Account not found."

    def get_account(self, name):
        return self.accounts.get(name, None)

    def list_accounts(self):
        return "\n".join([str(account) for account in self.accounts.values()])


class BankApp:
    def __init__(self, root):
        self.bank = BankSystem()
        self.root = root
        self.root.title("Modern Bank Management System")
        self.root.geometry("500x500")
        self.style = ttk.Style(theme="cosmo")  # Choose a modern theme

        # Create Account Frame
        self.create_account_frame = ttk.LabelFrame(root, text="Create Account", padding=10)
        self.create_account_frame.pack(fill="x", padx=10, pady=10)

        ttk.Label(self.create_account_frame, text="Name:").grid(row=0, column=0, padx=5, pady=5)
        self.name_entry = ttk.Entry(self.create_account_frame)
        self.name_entry.grid(row=0, column=1, padx=5, pady=5)

        ttk.Label(self.create_account_frame, text="Initial Deposit:").grid(row=1, column=0, padx=5, pady=5)
        self.initial_deposit_entry = ttk.Entry(self.create_account_frame)
        self.initial_deposit_entry.grid(row=1, column=1, padx=5, pady=5)

        self.create_account_button = ttk.Button(
            self.create_account_frame, text="Create Account", bootstyle=SUCCESS, command=self.create_account
        )
        self.create_account_button.grid(row=2, column=0, columnspan=2, pady=10)

        # Deposit/Withdraw/Check Balance Frame
        self.transaction_frame = ttk.LabelFrame(root, text="Transactions", padding=10)
        self.transaction_frame.pack(fill="x", padx=10, pady=10)

        ttk.Label(self.transaction_frame, text="Name:").grid(row=0, column=0, padx=5, pady=5)
        self.transaction_name_entry = ttk.Entry(self.transaction_frame)
        self.transaction_name_entry.grid(row=0, column=1, padx=5, pady=5)

        ttk.Label(self.transaction_frame, text="Amount:").grid(row=1, column=0, padx=5, pady=5)
        self.amount_entry = ttk.Entry(self.transaction_frame)
        self.amount_entry.grid(row=1, column=1, padx=5, pady=5)

        self.deposit_button = ttk.Button(
            self.transaction_frame, text="Deposit", bootstyle=INFO, command=self.deposit
        )
        self.deposit_button.grid(row=2, column=0, padx=5, pady=5)

        self.withdraw_button = ttk.Button(
            self.transaction_frame, text="Withdraw", bootstyle=WARNING, command=self.withdraw
        )
        self.withdraw_button.grid(row=2, column=1, padx=5, pady=5)

        self.check_balance_button = ttk.Button(
            self.transaction_frame, text="Check Balance", bootstyle=PRIMARY, command=self.check_balance
        )
        self.check_balance_button.grid(row=3, column=0, columnspan=2, pady=10)

        # Admin Panel Frame
        self.admin_frame = ttk.LabelFrame(root, text="Admin Panel", padding=10)
        self.admin_frame.pack(fill="x", padx=10, pady=10)

        ttk.Label(self.admin_frame, text="Admin Name:").grid(row=0, column=0, padx=5, pady=5)
        self.admin_name_entry = ttk.Entry(self.admin_frame)
        self.admin_name_entry.grid(row=0, column=1, padx=5, pady=5)

        self.delete_account_button = ttk.Button(
            self.admin_frame, text="Delete Account", bootstyle=DANGER, command=self.delete_account
        )
        self.delete_account_button.grid(row=1, column=0, padx=5, pady=5)

        self.view_all_accounts_button = ttk.Button(
            self.admin_frame, text="View All Accounts", bootstyle=SECONDARY, command=self.view_all_accounts
        )
        self.view_all_accounts_button.grid(row=1, column=1, padx=5, pady=5)

    def create_account(self):
        name = self.name_entry.get()
        initial_deposit = self.initial_deposit_entry.get()
        if name and initial_deposit:
            try:
                initial_deposit = float(initial_deposit)
                message = self.bank.create_account(name, initial_deposit)
                messagebox.showinfo("Success", message)
            except ValueError:
                messagebox.showerror("Error", "Invalid initial deposit amount.")
        else:
            messagebox.showerror("Error", "Please fill in all fields.")

    def deposit(self):
        name = self.transaction_name_entry.get()
        amount = self.amount_entry.get()
        if name and amount:
            try:
                amount = float(amount)
                account = self.bank.get_account(name)
                if account:
                    message = account.deposit(amount)
                    messagebox.showinfo("Success", message)
                else:
                    messagebox.showerror("Error", "Account not found.")
            except ValueError:
                messagebox.showerror("Error", "Invalid amount.")
        else:
            messagebox.showerror("Error", "Please fill in all fields.")

    def withdraw(self):
        name = self.transaction_name_entry.get()
        amount = self.amount_entry.get()
        if name and amount:
            try:
                amount = float(amount)
                account = self.bank.get_account(name)
                if account:
                    message = account.withdraw(amount)
                    messagebox.showinfo("Success", message)
                else:
                    messagebox.showerror("Error", "Account not found.")
            except ValueError:
                messagebox.showerror("Error", "Invalid amount.")
        else:
            messagebox.showerror("Error", "Please fill in all fields.")

    def check_balance(self):
        name = self.transaction_name_entry.get()
        if name:
            account = self.bank.get_account(name)
            if account:
                message = account.check_balance()
                messagebox.showinfo("Balance", message)
            else:
                messagebox.showerror("Error", "Account not found.")
        else:
            messagebox.showerror("Error", "Please enter the account holder's name.")

    def delete_account(self):
        name = self.admin_name_entry.get()
        if name:
            message = self.bank.delete_account(name)
            messagebox.showinfo("Success", message)
        else:
            messagebox.showerror("Error", "Please enter the account holder's name.")

    def view_all_accounts(self):
        accounts = self.bank.list_accounts()
        if accounts:
            messagebox.showinfo("All Accounts", accounts)
        else:
            messagebox.showinfo("All Accounts", "No accounts found.")


if __name__ == "__main__":
    root = ttk.Window(themename="cosmo")  # Use a modern theme
    app = BankApp(root)
    root.mainloop()