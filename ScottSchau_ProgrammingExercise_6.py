# Import the regular expression module
import re


# --------------------------------------------------
# Function to check if a phone number is valid
# Example valid format: 123-456-7890
# --------------------------------------------------
def validate_phone(phone):

    # Regular expression pattern for a phone number
    pattern = r"\d{3}-\d{3}-\d{4}"

    # re.fullmatch checks if the entire string matches the pattern
    if re.fullmatch(pattern, phone):
        return True
    else:
        return False


# --------------------------------------------------
# Function to check if a Social Security Number is valid
# Example valid format: 123-45-6789
# --------------------------------------------------
def validate_ssn(ssn):

    # Regular expression pattern for SSN
    pattern = r"\d{3}-\d{2}-\d{4}"

    if re.fullmatch(pattern, ssn):
        return True
    else:
        return False


# --------------------------------------------------
# Function to check if a ZIP code is valid
# Example valid formats:
# 12345
# 12345-6789
# --------------------------------------------------
def validate_zip(zip_code):

    # Regular expression pattern for ZIP code
    pattern = r"\d{5}(-\d{4})?"

    if re.fullmatch(pattern, zip_code):
        return True
    else:
        return False


# --------------------------------------------------
# Function to test the validators with sample data
# This helps confirm the regex works correctly
# --------------------------------------------------
def test_functions():

    print("Testing the validation functions\n")

    # Test phone numbers
    print("Phone Tests:")
    print("123-456-7890:", validate_phone("123-456-7890"))  # valid
    print("1234567890:", validate_phone("1234567890"))      # invalid
    print()

    # Test SSN
    print("SSN Tests:")
    print("123-45-6789:", validate_ssn("123-45-6789"))  # valid
    print("123456789:", validate_ssn("123456789"))      # invalid
    print()

    # Test ZIP codes
    print("ZIP Code Tests:")
    print("12345:", validate_zip("12345"))          # valid
    print("12345-6789:", validate_zip("12345-6789"))# valid
    print("1234:", validate_zip("1234"))            # invalid
    print()


# --------------------------------------------------
# Main function
# Gets user input and prints validation results
# --------------------------------------------------
def main():

    # Run tests first
    test_functions()

    print("Now enter your own information:\n")

    # Ask user for input
    phone = input("Enter a phone number (123-456-7890): ")
    ssn = input("Enter a SSN (123-45-6789): ")
    zip_code = input("Enter a ZIP code (12345 or 12345-6789): ")

    print("\nValidation Results:")

    # Check phone number
    if validate_phone(phone):
        print("Phone number is VALID")
    else:
        print("Phone number is INVALID")

    # Check SSN
    if validate_ssn(ssn):
        print("SSN is VALID")
    else:
        print("SSN is INVALID")

    # Check ZIP code
    if validate_zip(zip_code):
        print("ZIP code is VALID")
    else:
        print("ZIP code is INVALID")


# This line runs the program
if __name__ == "__main__":
    main()