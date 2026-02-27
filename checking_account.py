# checking_account.py
from bank_account import BankAccount

class CheckingAccount(BankAccount):
    def __init__(self, customer_name, current_balance, minimum_balance, transfer_limit):
        super().__init__(customer_name, current_balance, minimum_balance)
        self.transfer_limit = transfer_limit  # Max transfer per transaction

    def transfer(self, amount, target_account):
        if amount <= 0:
            print("Transfer amount must be positive.")
            return
        if amount > self.transfer_limit:
            print(f"Transfer denied! Amount exceeds limit of {self.transfer_limit}.")
            return
        if (self._current_balance - amount) < self._minimum_balance:
            print("Transfer denied! Balance would drop below minimum required.")
            return
        self._current_balance -= amount
        target_account.deposit(amount)
        print(f"{amount} transferred to {target_account.customer_name}. New balance: {self._current_balance}")