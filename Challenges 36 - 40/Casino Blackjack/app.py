import random
import time

class Card():
    def __init__(self, rank, value, suit):
        self.rank = rank # 2-10, J, Q, K, A
        self.value = value # 1-11
        self.suit = suit
    
    def display_card(self):
        print(f"{self.rank} of {self.suit}")

class Deck():
    # 52 cards
    def __init__(self):
        self.cards = []
    
    def build_deck(self):
        suits = ["Diamonds","Spades","Hearts","Clovers"]
        ranks = {
            "2": 2,
            "3": 3,
            "4": 4,
            "5": 5,
            "6": 6,
            "7": 7,
            "8": 8,
            "9": 9,
            "10": 10,
            "J": 10,
            "Q": 10,
            "K": 10,
            "A": 11
        }
        # Create cards and add them to the deck
        for suit in suits:
            for rank, value in ranks.items():
                card = Card(rank,value,suit)
                self.cards.append(card)

    def shuffle_deck(self):
        random.shuffle(self.cards)

    def deal_card(self): # Once the deck is shuffled we deal a card
        card = self.cards.pop()
        return card

class Player():
    def __init__(self):
        self.hand = []
        self.hand_value = 0
        self.playing_hand = True

    def draw_hand(self,deck):
        for i in range(2):
            card = deck.deal_card()
            self.hand.append(card)

    def display_hand(self):
        print("\nYour hand:")
        for card in self.hand:
            card.display_card()
    
    def hit(self,deck):
        card = deck.deal_card()
        self.hand.append(card)
    
    def get_hand_value(self):
        self.hand_value = 0
        ace_in_hand = False
        for card in self.hand:
            self.hand_value += card.value 
            if card.rank == "A":
                ace_in_hand = True
        # Check if hand is greater than 21
        if self.hand_value > 21 and ace_in_hand:
            self.hand_value -= 10 # Treat A as 1 instead of 11
        print(f"\nTotal value of the hand: {self.hand_value}") 

    def update_hand(self,deck):
        if self.hand_value < 21:
            choice = input("\nWould you like to hit? (y/n) ").lower()
            if choice == "y":
                self.hit(deck)
            else:
                self.playing_hand = False
        else:
            self.playing_hand = False     

class Dealer():
    def __init__(self):
        self.hand = []
        self.hand_value = 0
        self.playing_hand = True
    
    def draw_hand(self,deck):
        for i in range(2):
            card = deck.deal_card()
            self.hand.append(card)
    
    def display_hand(self):
        input("Press 'Enter' to reveal dealer's cards ")
        for card in self.hand:
            card.display_card()
            time.sleep(1)

    def hit(self,deck):
        self.get_hand_value()
        while self.hand_value < 17:
            card = deck.deal_card()
            self.hand.append(card)
            self.get_hand_value()
        print(f"The dealer has {len(self.hand)} cards in his hand.")

    def get_hand_value(self):
        self.hand_value = 0
        ace_in_hand = False
        for card in self.hand:
            self.hand_value += card.value 
            if card.rank == "A":
                ace_in_hand = True
        # Check if hand is greater than 21
        if self.hand_value > 21 and ace_in_hand:
            self.hand_value -= 10 # Treat A as 1 instead of 11

class Game():
    def __init__(self,money):
        self.money = int(money)
        self.bet = 20
        self.winner = ""
    
    def set_bet(self):
        betting = True
        while betting:
            bet = int(input("Enter your bet: "))
            if bet < 20:
                bet = 20
            if bet > self.money:
                print("Sorry, you don't have enough money for that bet.")
            else:
                self.bet = bet
                betting = False
    
    def scoring(self,player_value, dealer_value):
        # Black Jack
        if player_value == 21:
            print("You got Black Jack!")
            self.winner = "p"
        elif dealer_value == 21:
            print("Dealer got Black Jack!")
            self.winner = "d"
        # More than 21 points
        elif player_value > 21:
            print("Whoops, your got more than 21!")
            self.winner = "d"
        elif dealer_value > 21:
            print("Dealer got more than 21!")
            self.winner = "p"
        # Other cases
        else:
            if player_value > dealer_value:
                print(f"You got {player_value} while the dealer got {dealer_value}.")
                print("You win!")
                self.winner = "p"
            elif player_value < dealer_value:
                print(f"You got {player_value} while the dealer got {dealer_value}.")
                print("Dealer wins!")
                self.winner = "d"
            else:
                print(f"You got {player_value} while the dealer got {dealer_value}.")
                print("It's a tie!")
                self.winner = "tie"
    
    def payout(self):
        # Player wins
        if self.winner == "p":
            self.money += self.bet
        # Player lose    
        elif self.winner == "d":
            self.money -= self.bet
    
    def display_money(self):
        print(f"\nYou have ${self.money}.")

    def display_money_and_bet(self):
        print(f"\nYou have ${self.money} and the current bet is ${self.bet}.")
        
# Main code

print("Welcome to the Casino Blackjack App!")
print("\nThe minimum bet is $20.")
money = int(input("How much money would you like to play today? "))
game = Game(money)

# Loop time
playing = True
while playing:
    # Create deck
    game_deck = Deck()
    game_deck.build_deck()
    game_deck.shuffle_deck()
    # Players
    player = Player()
    dealer = Dealer()
    # Money
    game.display_money()
    game.set_bet()
    # Hands
    player.draw_hand(game_deck)
    dealer.draw_hand(game_deck)
    # Money and bet
    game.display_money_and_bet()
    print("\nShowing dealer's first card...")
    print(f"{dealer.hand[0].rank} of {dealer.hand[0].suit}.")
    # Player hand
    while player.playing_hand:
        player.display_hand()
        player.get_hand_value()
        player.update_hand(game_deck)
    # Dealer hand
    dealer.hit(game_deck)
    dealer.display_hand()
    # Score
    game.scoring(player.hand_value,dealer.hand_value)
    game.payout()
    # End game
    if game.money < 20:
        playing = False
        print("\nThe game ended because you don't have enough money to bet!")
