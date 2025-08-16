
import random

# Card class
class Card:
    def __init__(self, rank, suit):
        self.rank = rank
        self.suit = suit

    def __str__(self):
        return f"{self.rank} of {self.suit}"

# Deck class
class Deck:
    def __init__(self):
        self.cards = []
        suits = ["Hearts", "Diamonds", "Clubs", "Spades"]
        ranks = ["Ace", "2", "3", "4", "5", "6", "7", "8", "9", "10", "Jack", "Queen", "King"]

        for suit in suits:
            for rank in ranks:
                self.cards.append(Card(rank, suit))

    def shuffle(self):
        random.shuffle(self.cards)

    def deal(self):
        if len(self.cards) == 0:
            return None
        return self.cards.pop(0)

    def cards_remaining(self):
        return len(self.cards)


# Main program
def main():
    print("Card Dealer\n")

    deck = Deck()
    deck.shuffle()

    print("I have shuffled a deck of 52 cards.\n")

    number_to_deal = int(input("How many cards would you like?: "))
    print("\nHere are your cards:\n")

    for i in range(number_to_deal):
        card = deck.deal()
        if card:
            print(card)
        else:
            print("No more cards left in the deck!")
            break

    print(f"\nThere are {deck.cards_remaining()} cards left in the deck.\n")
    print("Good luck!")


if __name__ == "__main__":
    main()
