import random

# Parent Class
class Pykemon():
    def __init__(self,name,element,health,speed):
        self.name = name
        self.element = element
        self.current_health = health
        self.max_health = health
        self.speed = speed
        self.is_alive = True
    
    def light_attack(self,enemy):
        damage = random.randint(15,25)
        print(f"{self.name} used {self.moves[0]}!")
        print(f"It dealt {damage} damage!")
        enemy.current_health -= damage
    
    def heavy_attack(self,enemy):
        damage = random.randint(0,50)
        print(f"{self.name} used {self.moves[1]}!")
        if damage < 10:
            print("It missed!")
        else:
            print(f"It dealt {damage} damage!")
            enemy.current_health -= damage

    def restore(self):
        heal = random.randint(15,25)
        print(f"{self.name} used {self.moves[2]}!")
        print(f"{self.name} healed {heal} HP!")
        self.current_health += heal
        if self.current_health > self.max_health: # Check to not exceed max HP
            self.current_health = self.max_health
    
    def faint(self):
        if self.current_health <= 0:
            self.is_alive = False
            print(f"{self.name} fainted!")
            input("Press 'Enter' to continue. ")
    
    def show_stats(self):
        print(f"\nName: {self.name}")
        print(f"Element Type: {self.element}")
        print(f"HP: {self.current_health} / {self.max_health}")
        print(f"Speed: {self.speed}\n")

# Child Classes
class Fire(Pykemon):
    def __init__(self,name,element,health,speed):
        super().__init__(name, element, health, speed) # Get initial attributes from parent class
        self.moves = ["Scratch","Ember","Light","Fire Blast"] # Attacks unique for FIRE Pykemons
    
    def special_attack(self,enemy):
        print(f"{self.name} used {self.moves[3]}!")
        if enemy.element == "Grass":
            damage = random.randint(35,50)
            print(f"It dealt {damage} damage!")
            print("It's super effective!")
            enemy.current_health -= damage
        elif enemy.element == "Water":
            damage = random.randint(5,10)
            print(f"It dealt {damage} damage!")
            print(f"It's not very effective...")
            enemy.current_health -= damage
        else:
            damage = random.randint(10,30)
            print(f"It dealt {damage} damage!")
            enemy.current_health -= damage

    def move_info(self):
        print(f"---- {self.moves[0]} ----")
        print("A basic attack. Deals light damage to enemy.",sep="\n")
        print(f"---- {self.moves[1]} ----")
        print("A risky attack. Deals heavy damage to enemy or nothing at all.",sep="\n")
        print(f"---- {self.moves[2]} ----")
        print("A restorative move. Heals your Pykemon",sep="\n")
        print(f"---- {self.moves[3]} ----")
        print("A powerful FIRE attack. Deals massive damage to a GRASS enemy.",sep="\n")

class Water(Pykemon):
    def __init__(self,name,element,health,speed):
        super().__init__(name, element, health, speed)
        self.moves = ["Bite","Splash","Dive","Water Cannon"]
    
    def special_attack(self,enemy):
        print(f"{self.name} used {self.moves[3]}!")
        if enemy.element == "Fire":
            damage = random.randint(35,50)
            print(f"It dealt {damage} damage!")
            print("It's super effective!")
            enemy.current_health -= damage
        elif enemy.element == "Grass":
            damage = random.randint(5,10)
            print(f"It dealt {damage} damage!")
            print(f"It's not very effective...")
            enemy.current_health -= damage
        else:
            damage = random.randint(10,30)
            print(f"It dealt {damage} damage!")
            enemy.current_health -= damage

    def move_info(self):
        print(f"---- {self.moves[0]} ----")
        print("A basic attack. Deals light damage to enemy.",sep="\n")
        print(f"---- {self.moves[1]} ----")
        print("A risky attack. Deals heavy damage to enemy or nothing at all.",sep="\n")
        print(f"---- {self.moves[2]} ----")
        print("A restorative move. Heals your Pykemon",sep="\n")
        print(f"---- {self.moves[3]} ----")
        print("A powerful WATER attack. Deals massive damage to a FIRE enemy.",sep="\n")

class Grass(Pykemon):
    def __init__(self,name,element,health,speed):
        super().__init__(name, element, health, speed)
        self.moves = ["Vine Whip","Wrap","Grow","Leaf Blade"]
    
    def special_attack(self,enemy):
        print(f"{self.name} used {self.moves[3]}!")
        if enemy.element == "Water":
            damage = random.randint(35,50)
            print(f"It dealt {damage} damage!")
            print("It's super effective!")
            enemy.current_health -= damage
        elif enemy.element == "Fire":
            damage = random.randint(5,10)
            print(f"It dealt {damage} damage!")
            print(f"It's not very effective...")
            enemy.current_health -= damage
        else:
            damage = random.randint(10,30)
            print(f"It dealt {damage} damage!")
            enemy.current_health -= damage

    def move_info(self):
        print(f"---- {self.moves[0]} ----")
        print("A basic attack. Deals light damage to enemy.",sep="\n")
        print(f"---- {self.moves[1]} ----")
        print("A risky attack. Deals heavy damage to enemy or nothing at all.",sep="\n")
        print(f"---- {self.moves[2]} ----")
        print("A restorative move. Heals your Pykemon",sep="\n")
        print(f"---- {self.moves[3]} ----")
        print("A powerful GRASS attack. Deals massive damage to a WATER enemy.",sep="\n")

class Game():
    def __init__(self):
        self.pykemon_elements = ["Fire", "Water","Grass"]
        self.pykemon_names = ["Chewdie","Spatol","Acumon","Pykochu","Jampot","Zantbat","Rubblesaur","SolidoNaso","Burnmander","Sweetil","Muttle","Pionx","Carmurumon","Chomosuke","Abbacab"]
        self.battles_won = 0

    def create_pykemon(self):
        health = random.randint(70,100)
        speed = random.randint(1,10)
        # Random pick for element
        element = random.choice(self.pykemon_elements) 
        name = random.choice(self.pykemon_names)
        # Create the right Pykemon
        if element == "Fire":
            pykemon = Fire(name,element,health,speed)
        elif element == "Water":
            pykemon = Water(name,element,health,speed)
        else:
            pykemon = Grass(name,element,health,speed)
        # Return it
        return pykemon
    
    def choose_pykemon(self):
        starters = []

        while len(starters) < 3:
            pykemon = self.create_pykemon()
            # Check if it's unique
            valid_pykemon = True
            for starter in starters:                    ###### REVISAR ######
                if starter.name == pykemon.name or starter.element == pykemon.element:
                    valid_pykemon = False
            # The Pykemon it's unique so add it to starters        
            if valid_pykemon == True:
                starters.append(pykemon)
        # Show data of starters
        for starter in starters:
            starter.show_stats()
            starter.move_info()
        # Show info to user to get choice
        print("\nThe Proffesor Robel shows you 3 Pykemons.")
        print(f"Press (1) to choose {starters[0].name}.")
        print(f"Press (2) to choose {starters[1].name}.")
        print(f"Press (3) to choose {starters[2].name}.")
        choice = int(input("What's your choice? "))
        # Return the Pokymon
        return starters[choice - 1]

    def get_attack(self,pykemon):
        # User attack choice
        print(f"What move should {pykemon.name} use?")
        print(f"Press (1) to choose {pykemon.moves[0]}.")
        print(f"Press (2) to choose {pykemon.moves[1]}.")
        print(f"Press (3) to choose {pykemon.moves[2]}.")
        print(f"Press (4) to choose {pykemon.moves[3]}.")
        choice = int(input("What's your choice? "))
        # Formatting
        print()
        print("--------------------------------------")
        # Return choice
        return choice

    def player_attack(self,move,player,computer):
        # Attack computer
        if move == 1:
            player.light_attack(computer)
        elif move == 2:
            player.heavy_attack(computer)
        elif move == 3:
            player.restore()
        elif move == 4:
            player.special_attack(computer)

        computer.faint() # Check if the enemy fainted

    def computer_attack(self,player,computer):
        # Random move
        move = random.randint(1,4)
        if move == 1:
            computer.light_attack(player)
        elif move == 2:
            computer.heavy_attack(player)
        elif move == 3:
            computer.restore()
        elif move == 4:
            computer.special_attack(player)
        player.faint() # Check if user's Pykemon fainted

    def battle(self,player,computer):
        player_move = self.get_attack(player)
        # The fastest Pykemon attacks first
        if player.speed >= computer.speed:
            self.player_attack(player_move,player,computer)
            if computer.is_alive:
                self.computer_attack(player,computer)
        else:
            self.computer_attack(player,computer)
            if player.is_alive:
                self.player_attack(player_move,player,computer)

# Main code

print("Welcome to the Pykemon Simulator App!")
print("Can you become the greatest Pykemon Master ever?")

print("\nDon't worry, Prof. Robel is here to help you on your quest!")
print("He would like to gift you your first Pykemon!")
print("Here are three potential Pykemon partners.")
input("Press 'Enter' to choose your Pykemon. ")

playing_main = True
while playing_main:
    game = Game()
    # Player choose Pykemon
    player = game.choose_pykemon()
    print(f"\nCongratulations trainer, you've chosen {player.name}!")
    input("Press 'Enter' to start your adventure!")

    while player.is_alive:
        # Computer Pykemon appeared
        computer = game.create_pykemon()
        print(f"\nOh no! A wild {computer.name} appeared!")
        computer.show_stats()
        # Battle phase
        while player.is_alive and computer.is_alive:
            game.battle(player,computer)
            # Both survived first round
            if player.is_alive and computer.is_alive:
                player.show_stats()
                computer.show_stats()
                # Formatting
                print("------------------------------")
        # If the player survived update battles_won
        if player.is_alive:
            game.battles_won += 1

    print(f"\nOh no, your {player.name} fainted!")
    print(f"However it seems {player.name} defeated {game.battles_won} enemies. Good job!")
    choice = input("\nPlay again? (y/n) ").lower()
    if choice != "y":
        playing_main = False
        print("Thank you for playing Pykemon!")
