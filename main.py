# main.py
from savings_account import SavingsAccount
from checking_account import CheckingAccount
from bank_account import BankAccount

# Scenario 1: Savings Accounts
savings1 = SavingsAccount("Alice", 2000, 100, 5)  # 5% interest
savings2 = SavingsAccount("John", 1500, 100, 3)   # 3% interest

savings1.set_account_number("SAV1001")
savings2.set_account_number("SAV1002")

savings1.print_customer_information()
savings1.add_interest()
savings2.print_customer_information()
savings2.add_interest()

print("\n")

# Scenario 2: Checking Accounts
checking1 = CheckingAccount("Bob", 1000, 50, 500)
checking2 = CheckingAccount("Carol", 800, 50, 300)

checking1.set_account_number("CHK2001")
checking2.set_account_number("CHK2002")

checking1.print_customer_information()
checking1.withdraw(200)
checking1.transfer(400, checking2)  # Should succeed
checking1.transfer(600, checking2)  # Should fail (over limit)

checking2.print_customer_information()