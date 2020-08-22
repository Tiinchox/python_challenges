import random

class Creature():

    def __init__(self, name):
        # Name
        self.name = name
        # Stats
        self.hunger = 0
        self.boredom = 0
        self.tiredness = 0
        self.dirtiness = 0
        # Food in inventory
        self.food = 2
        # Sleeping
        self.is_sleeping = False
        # Alive
        self.is_alive = True

    def eat(self):
        if self.food > 0: # If there's food in inventory
            self.food -= 1
            self.hunger -= random.randint(1,4)
            print(f"\n{self.name} ate a lot and its hunger levels went down!")
        else:
            print("\nYou don't have food in your inventory!")
        # We don't want a negative value in hunger
        if self.hunger < 0:
            self.hunger = 0
    
    def play(self):
        number = random.randint(0,2)
        print(f"It seems {self.name} wants to play a game...")
        guess = int(input(f"{self.name} is thinking of a number between 0 and 2. Can you guess what's that number? "))
        if guess == number:
            print(f"{self.name} is impressed, you got the number right!")
            self.boredom -= 3
            print(f"{self.name}'s levels of boredom went down a lot!")
        else:
            print("Sorry, that was not the number...")
            self.boredom -= 1
            print(f"{self.name}'s levels of boredom went down a little")
        if self.boredom < 0:
            self.boredom = 0

    def sleep(self):
        self.is_sleeping = True
        self.tiredness -= 3
        self.boredom -= 2
        print(f"{self.name} is sleeping...")
        if self.tiredness < 0:
            self.tiredness = 0
        if self.boredom < 0:
            self.boredom = 0
    
    def awake(self):
        wake_up = random.randint(0,2)
        if wake_up == 0:
            print(f"{self.name} woke up and is no longer bored!")
            self.boredom = 0
        else:
            print(f"{self.name} won't wake up!")
            self.sleep()
    
    def clean(self):
        self.dirtiness = 0
        print(f"{self.name} took a bath and is no longer dirty!")

    def forage(self):
        food_found = random.randint(0,4)
        self.food += food_found
        self.dirtiness += 2
        if food_found > 0:
            print(f"{self.name} found food!")
        else:
            print(f"Oh no! {self.name} didn't find anything!")
    
    def show_values(self): # Show creature's stats
        print(f"Creature Name: {self.name}")
        print(f"Hunger (0-10): {self.hunger}")
        print(f"Boredom (0-10): {self.boredom}")
        print(f"Tiredness (0-10): {self.tiredness}")
        print(f"Dirtiness (0-10): {self.dirtiness}")
        print(f"\nFood in inventory: {self.food}")
        if self.is_sleeping:
            print("Sleeping Status: Sleep")
        else:
            print("Sleeping Status: Awake")
    
    def increment_values(self, difficulty):
        self.hunger += random.randint(0, difficulty)
        if self.is_sleeping == False:
            self.boredom += random.randint(0, difficulty)
            self.tiredness += random.randint(0, difficulty)  
        self.dirtiness += random.randint(0, difficulty)
    
    def kill(self):
        if self.hunger >= 10:
            print(f"Oh no, {self.name} starved to death!")
            respects = input("Press F to pay respects: ").upper()
            if respects == "F":
                print("Don't worry, it's in a better place now :')")
            else:
                print("You monster, why couldn't do something so simple! D:<")
            self.is_alive = False
        elif self.dirtiness >= 10:
            print(f"{self.name} suffered an infection and died! D:")
            self.is_alive = False
        elif self.boredom >= 10:
            self.boredom = 10
            print(f"{self.name} is so bored it's falling asleep!")
            self.is_sleeping = True
        elif self.tiredness >= 10:
            self.tiredness = 10
            print(f"{self.name} is sleepy and fell asleep!")

def show_menu(creature):
    if creature.is_sleeping == True:
        choice = int(input(f"\nPress (6) to try to wake {creature.name} up! "))
        choice = 6
        return choice
    else:
        print("\nEnter (1) to eat.")
        print("Enter (2) to play.")
        print("Enter (3) to sleep.")
        print("Enter (4) to take a bath.")
        print("Enter (5) to forage for food.")
        choice = int(input("Enter your choice: "))
        return choice
    
def call_action(creature,choice):
    if choice == 1:
        creature.eat()
    elif choice == 2:
        creature.play()
    elif choice == 3:
        creature.sleep()
    elif choice == 4:
        creature.clean()
    elif choice == 5:
        creature.forage()
    elif choice == 6:
        creature.awake()
    else:
        print("That's not a valid command!")

# Main code

print("Welcome to the Pythonagachi Simulator App!")
difficulty = int(input("Choose your difficulty level (1-5): "))
if difficulty > 5:
    difficulty = 5
elif difficulty < 1:
    difficulty = 1

active = True
# Create a creature
name = input("Enter a name for your creature: ").title()
creature = Creature(name)
round = 1

while active:
    # Current round
    print("-------------------------------------")
    print(f"Round #{round}")
    creature.show_values()
    choice = show_menu(creature)
    call_action(creature,choice)

    # Summary
    print("-------------------------------------")
    print(f"\nRound #{round} Summary:")
    creature.show_values()
    input("Press 'Enter' to continue ")

    # Increment
    creature.increment_values(difficulty)
    creature.kill()
    round += 1

    # Check if creature is dead
    if creature.is_alive == False:
        print("R.I.P")
        print(f"{creature.name} survived a total of {round} rounds")
        # Play again
        restart = input("Play again? (y-n) ").lower()
        if restart != "y":
            active = False
            print("Thank you for playing Pythonagachi!")  
        else:
            round = 1