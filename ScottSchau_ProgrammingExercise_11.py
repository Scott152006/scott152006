import random   # used to shuffle the deck


# -------------------------------
# Deck class (holds all cards)
# -------------------------------
class Deck:
    def __init__(self):
        self.cards = []   # empty list to store cards

        # simple lists for ranks and suits
        ranks = ["2", "3", "4", "5", "6", "7", "8", "9", "10",
                 "J", "Q", "K", "A"]
        suits = ["Hearts", "Diamonds", "Clubs", "Spades"]

        # create all 52 cards
        for suit in suits:
            for rank in ranks:
                card = rank + " of " + suit
                self.cards.append(card)

        random.shuffle(self.cards)   # mix the cards


    # deal ONE card (remove from deck)
    def deal(self):
        return self.cards.pop()


# -------------------------------
# function to show the hand
# -------------------------------
def show_hand(hand):
    print("\nYour cards:")
    for i in range(5):
        print(i + 1, "-", hand[i])   # show number + card


# -------------------------------
# function to replace cards
# -------------------------------
def replace_cards(hand, deck, choices):
    for num in choices:
        index = num - 1          # convert 1-5 to 0-4
        hand[index] = deck.deal()   # replace card


# -------------------------------
# main program
# -------------------------------
def main():
    deck = Deck()   # create deck

    # deal 5 cards
    hand = []
    for i in range(5):
        hand.append(deck.deal())

    print("Starting Hand:")
    show_hand(hand)

    # ask user which cards to replace
    user_input = input("\nEnter card numbers to replace (ex: 1,3,5): ")

    # turn input into a list of numbers
    choices = []
    if user_input != "":
        parts = user_input.split(",")
        for p in parts:
            if p.strip().isdigit():
                choices.append(int(p.strip()))

    # replace selected cards
    replace_cards(hand, deck, choices)

    # show final hand
    print("\nFinal Hand:")
    show_hand(hand)


# run the program
main()