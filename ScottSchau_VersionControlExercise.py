# This program sells a limited number of cinema tickets (10 total).
# Each person can buy up to 4 tickets. The program ends when all tickets are sold.

def get_tickets():
    """
    Ask the user how many tickets they want to buy (1 to 4).
    Keeps asking until they give a valid number.
    """
    while True:
        try:
            # Ask the user for how many tickets they want
            num = int(input("How many tickets do you want (1-4)? "))

            # Check if the number is between 1 and 4
            if 1 <= num <= 4:
                return num  # Valid number, return it
            else:
                print("You can only buy 1 to 4 tickets.")
        except ValueError:
            # If the user didn't enter a number
            print("Please enter a number.")


def sell_tickets():
    """
    This function keeps track of how many tickets are sold.
    It stops when all 20 tickets are sold and shows how many buyers there were.
    """
    tickets_left = 10  # Total number of tickets available
    buyers = 0         # Accumulator to count the number of buyers

    # Keep running while tickets are still available
    while tickets_left > 0:
        print(f"\nTickets left: {tickets_left}")  # Show how many tickets are left

        want = get_tickets()  # Ask the user how many they want

        # Check if there are enough tickets left for this request
        if want <= tickets_left:
            tickets_left -= want     # Subtract the bought tickets
            buyers += 1              # Count the buyer
            print(f"You bought {want} ticket(s).")  # Confirm purchase
        else:
            # Not enough tickets for their request
            print("Not enough tickets left. Try a smaller number.")

    # When all tickets are sold
    print("\nAll tickets are sold!")
    print(f"Total buyers: {buyers}")  # Show how many people bought tickets


# Start the ticket selling program
sell_tickets()