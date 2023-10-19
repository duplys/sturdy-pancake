"""
Code illustrating the data abstraction principle.
"""


class BankAccount:
    """A simple bank account."""
    def __init__(self, account_number, account_holder, balance=0):
        self._account_number = account_number  # Private attribute
        self._account_holder = account_holder  # Private attribute
        self._balance = balance  # Private attribute

    def get_account_number(self):
        return self._account_number

    def get_account_holder(self):
        return self._account_holder

    def get_balance(self):
        return self._balance

    def deposit(self, amount):
        if amount > 0:
            self._balance += amount

        if amount > 20000:
            self._report_authorities()

    def withdraw(self, amount):
        if 0 < amount <= self._balance:
            self._balance -= amount

    def _report_authorities(self):
        """Report to authorities if a large number of money was deposited."""
        print("Reporting to authorities ...")


# Example usage
account = BankAccount("12345", "John Doe")
print("Account Number:", account.get_account_number())
print("Account Holder:", account.get_account_holder())
print("Initial Balance:", account.get_balance())

account.deposit(1000)
print("Balance after deposit:", account.get_balance())

account.withdraw(500)
print("Balance after withdrawal:", account.get_balance())
