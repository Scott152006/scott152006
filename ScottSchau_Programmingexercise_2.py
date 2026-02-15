# ------------------------------------------------------------
# Spam Detector Program
# This program checks an email message for common spam words.
# For every spam word found, 1 point is added to the spam score.
# The program then tells the user how likely the message is spam.
# ------------------------------------------------------------


# ------------------------------------------------------------
# Function 1: Get Email From User
# This function allows the user to type in an email message.
# The user presses ENTER on a blank line to finish typing.
# The function returns the complete email as one string.
# ------------------------------------------------------------
def get_email():

    print("Type or paste your email message below.")
    print("Press ENTER on a blank line when finished.\n")

    lines = []  # This list will store each line the user types

    while True:
        line = input()  # Get one line of input

        if line == "":  # If the line is blank, stop collecting input
            break

        lines.append(line)  # Add the line to the list

    # Join all lines together into one string
    email_message = "\n".join(lines)

    return email_message


# ------------------------------------------------------------
# Function 2: Check for Spam Words
# This function searches the email for spam words.
# It returns:
#   1. The total spam score
#   2. A dictionary of spam words that were found
# ------------------------------------------------------------
def check_spam(email_message, spam_words):

    email_message = email_message.lower()  # Make everything lowercase
    spam_score = 0  # Start score at 0
    words_found = {}  # Dictionary to store words that were found

    # Loop through each spam word
    for word in spam_words:

        # Count how many times the spam word appears
        count = email_message.count(word)

        # If the word appears at least once
        if count > 0:
            spam_score += count        # Add to total score
            words_found[word] = count  # Save word and count

    return spam_score, words_found


# ------------------------------------------------------------
# Function 3: Rate the Spam Score
# This function returns a message based on the score.
# ------------------------------------------------------------
def spam_rating(score):

    if score == 0:
        return "Very unlikely to be spam."
    elif score <= 3:
        return "Unlikely to be spam."
    elif score <= 6:
        return "Possibly spam."
    elif score <= 10:
        return "Likely spam."
    else:
        return "Highly likely to be spam!"


# ------------------------------------------------------------
# Main Program
# This is where everything runs.
# ------------------------------------------------------------
def main():

    # List of 30 common spam words and phrases
    spam_words = [
        "act now", "limited time", "urgent", "final notice",
        "account suspended", "verify your account", "click here",
        "unsubscribe", "free", "100% free", "risk-free",
        "guaranteed", "no cost", "winner", "congratulations",
        "cash bonus", "free money", "make money",
        "earn extra cash", "work from home", "get paid",
        "instant cash", "low interest", "credit",
        "investment", "exclusive deal", "offer expires",
        "last chance", "lose weight", "viagra"
    ]

    # Step 1: Get the email message
    email = get_email()

    # Step 2: Check for spam words
    score, found_words = check_spam(email, spam_words)

    # Step 3: Get spam rating message
    rating = spam_rating(score)

    # Step 4: Display results
    print("\n----------------------------")
    print("Spam Analysis Results")
    print("----------------------------")
    print("Spam Score:", score)
    print("Spam Likelihood:", rating)

    # Show which words were found
    if found_words:
        print("\nSpam Words Found:")
        for word, count in found_words.items():
            print("-", word, ":", count, "time(s)")
    else:
        print("\nNo spam words were found.")


# This makes sure the program runs
if __name__ == "__main__":
    main()
