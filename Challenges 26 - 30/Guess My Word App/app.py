import random

# Welcome message
print("Welcome to the Guess My Word App (FGO Edition)!")

# Dictionary with classes and names
game_dict = {
    "saber": ["altria", "mordred", "lancelot", "altera", "okita", "gawain"],
    "archer": ["emiya","gilgamesh","robin","nobunaga","euryale","ishtar"],
    "lancer": ["cuchulainn","scathach","enkidu","parvati","ereshkigal","medusa"],
    "caster": ["medea", "illya","circe","nero","helena","hans"],
    "rider": ["ushiwaka","medusa","astolfo","iskandar","kintoki","achilles"],
    "assassin": ["stheno","jack","kotaro","shuten","cleopatra","hassan"],
    "berserker": ["heracles","spartacus","lancelot","kiyohime","beowulf","bunyan"]
}

# Empty list
game_keys = []

# Add dict keys to list
for key in game_dict.keys():
    game_keys.append(key)

playing = True

# Game
while playing:

    # Random category
    game_category = game_keys[random.randint(0,len(game_keys)-1)]

    # Random word
    game_word = game_dict[game_category][random.randint(0,len(game_dict[game_category])-1)]
    
    blank_word = []

    # Add "-" to list
    for i in game_word:
        blank_word.append("-")
    
    print(f"\nGuess the word from the following class: {game_category.title()}")

    # Start empty variables
    guess = ""
    guess_count = 0

    # Single round loop
    while guess != game_word:

        # Get single guess from user
        print("".join(blank_word))
        guess = input("\nEnter your guess: ").lower()
        guess_count += 1

        # Guess correct, end game
        if guess == game_word:
            print(f"Amazing, you guess it right! And only took you {guess_count} guesses!")
            break

        # Guess incorrect, keep guessing
        else:
            print("Nope, let me reveal a letter to help you!")

            # Loop to replace "-" in blank_word to reveal a letter
            swap = True
            while swap:
                letter_index = random.randint(0,len(game_word) - 1)
                if blank_word[letter_index] == "-":
                    blank_word[letter_index] = game_word[letter_index]
                    swap = False

    # Ask the user to play again        
    choice = input("\nPlay again? (y/n): ").lower()
    if choice != "y":
        playing = False
        print("\nThanks for playing!")  
