# This program asks the user to enter their monthly expenses.
# The user enters:
#   - The type of expense (Rent, Food, Gas, etc.)
#   - The amount of the expense
#
# The program uses the reduce() function to:
#   - Calculate total expenses
#   - Find the highest expense
#   - Find the lowest expense
#
# The results are then displayed clearly.

from functools import reduce  # We import reduce so we can use it


def main():
    # This list will store all expenses
    # Each expense will be stored as a tuple:
    # (expense_type, amount)
    expenses = []

    print("Monthly Expense Tracker")
    print("-----------------------")

    # Keep asking the user for expenses
    while True:

        # Ask user for expense type
        expense_type = input("Enter expense type: ")

        # Ask user for expense amount
        # Convert the input into a float number
        amount = float(input("Enter amount: "))

        # Add the expense to the list
        # Example: ("Rent", 1200.00)
        expenses.append((expense_type, amount))

        # Ask if they want to continue
        again = input("Add another expense? (yes/no): ").lower()

        # If the user types anything other than "yes"
        # the loop will stop
        if again != "yes":
            break

    # ----------------------------
    # Using reduce() to calculate total
    # ----------------------------

    # Start with 0
    # Add each expense amount to the total
    total = reduce(lambda total, item: total + item[1], expenses, 0)

    # ----------------------------
    # Using reduce() to find highest expense
    # ----------------------------

    # Compare two expenses at a time
    # Keep the one with the larger amount
    highest = reduce(lambda x, y: x if x[1] > y[1] else y, expenses)

    # ----------------------------
    # Using reduce() to find lowest expense
    # ----------------------------

    # Compare two expenses at a time
    # Keep the one with the smaller amount
    lowest = reduce(lambda x, y: x if x[1] < y[1] else y, expenses)

    # ----------------------------
    # Display Results
    # ----------------------------

    print("\n----- Expense Summary -----")

    # Display total formatted to 2 decimal places
    print("Total Expenses: $" + format(total, ".2f"))

    # Display highest expense (label included)
    print("Highest Expense: " + highest[0] + " - $" + format(highest[1], ".2f"))

    # Display lowest expense (label included)
    print("Lowest Expense: " + lowest[0] + " - $" + format(lowest[1], ".2f"))


# This makes sure the program runs
if __name__ == "__main__":
    main()