# BankAcct Class
class BankAcct:

    # Constructor (__init__) - runs when object is created
    def __init__(self, name, account_number, amount, interest_rate):
        self.name = name  # account holder name
        self.account_number = account_number  # account number
        self.amount = amount  # current balance
        self.interest_rate = interest_rate  # interest rate (example: 0.05 for 5%)

    # Method to deposit money
    def deposit(self, amount):
        self.amount += amount
        print(f"Deposited: ${amount}")

    # Method to withdraw money
    def withdraw(self, amount):
        if amount > self.amount:
            print("Not enough funds!")
        else:
            self.amount -= amount
            print(f"Withdrew: ${amount}")

    # Method to adjust interest rate
    def set_interest_rate(self, new_rate):
        self.interest_rate = new_rate
        print(f"New interest rate set to {new_rate}")

    # Method to return current balance
    def get_balance(self):
        return self.amount

    # Method to calculate interest based on number of days
    def calculate_interest(self, days):
        # Simple interest formula: Interest = balance * rate * (days / 365)
        interest = self.amount * self.interest_rate * (days / 365)
        return interest

    # __str__ method to display account info
    def __str__(self):
        return (f"Account Holder: {self.name}\n"
                f"Account Number: {self.account_number}\n"
                f"Balance: ${self.amount:.2f}\n"
                f"Interest Rate: {self.interest_rate}\n")


# Test function
def test_bank_account():
    # Create a BankAcct object
    acct = BankAcct("Scott", "123456", 1000, 0.05)

    # Display initial account info
    print("Initial Account Info:")
    print(acct)

    # Deposit money
    acct.deposit(500)
    print(f"Balance after deposit: ${acct.get_balance()}")

    # Withdraw money
    acct.withdraw(200)
    print(f"Balance after withdrawal: ${acct.get_balance()}")

    # Try withdrawing too much
    acct.withdraw(2000)

    # Change interest rate
    acct.set_interest_rate(0.07)

    # Calculate interest for 30 days
    interest = acct.calculate_interest(30)
    print(f"Interest for 30 days: ${interest:.2f}")

    # Final account info
    print("\nFinal Account Info:")
    print(acct)


# Run the test function
test_bank_account()