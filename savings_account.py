# savings_account.py
from bank_account import BankAccount

class SavingsAccount(BankAccount):
    def __init__(self, customer_name, current_balance, minimum_balance, interest_rate):
        super().__init__(customer_name, current_balance, minimum_balance)
        self.interest_rate = interest_rate  # Annual interest %
#calculating interest
    def add_interest(self):
        interest = self._current_balance * (self.interest_rate / 100)
        self._current_balance += interest
        print(f"Interest of {interest} added. New balance: {self._current_balance}")