# bank_account.py
class BankAccount:
    bank_title = "Bank Of UNCC"

    def __init__(self, customer_name, current_balance, minimum_balance):
        self.customer_name = customer_name
        self._current_balance = current_balance      # Protected
        self._minimum_balance = minimum_balance    # Protected
        self.__account_number = None                # Private
        self.__routing_number = "00112233"          # Private

    # Setters and getters for private members
    def set_account_number(self, account_number):
        self.__account_number = account_number

    def get_account_number(self):
        return self.__account_number

    def get_routing_number(self):
        return self.__routing_number

    def deposit(self, amount):
        if amount > 0:
            self._current_balance += amount
            print(f"{amount} deposited. New balance is {self._current_balance}")
        else:
            print("Deposit must be greater than zero.")

    def withdraw(self, amount):
        if amount <= 0:
            print("Withdrawal amount must be positive.")
            return
        if (self._current_balance - amount) < self._minimum_balance:
            print("Withdrawal denied! Balance would drop below minimum required.")
        else:
            self._current_balance -= amount
            print(f"{amount} withdrawn. New balance: {self._current_balance}")

    def print_customer_information(self):
        print(f"Bank: {BankAccount.bank_title}")
        print(f"Customer Name: {self.customer_name}")
        print(f"Current Balance: {self._current_balance}")
        print(f"Minimum Balance: {self._minimum_balance}")
        print(f"Account Number: {self.__account_number}")
        print(f"Routing Number: {self.__routing_number}")