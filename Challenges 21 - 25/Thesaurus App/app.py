import random

# Dictionary
thesaurus = {
    "sword": ["cutlass","rapier","falchion","broadsword","katana"],
    "bow": ["crossbow","longbow","shortbow","handbow","flatbow"],
    "spear": ["lance","trident","javelin","glaive","halverd"],
    "rod": ["staff","pole","baton","wand","ramrod"]
}

# Welcome message
print("Welcome to the Thesaurus App!")

print("\nChoose a word from the thesaurus and I will give you a synonym!")

print("\nHere are the word in the thesaurus:")

# Show the available words
for key in thesaurus.keys():
    print(f"\t-{key}")

# Get word from user
word = input("\nWhat word would you like a synonym for? ").lower()

# If the word is in the dict
if word in thesaurus:
    num = random.randint(0,4)
    # Show a random synonym for that word
    print(f"A synonym for {word} is {thesaurus[word][num]}.")
    # Ask if the user want to see all words and synonys
    full = input("\nWould you like to see the full thesaurus? (y/n): ")
    if full.startswith("y"):
        for key, values in thesaurus.items():
            print(f"\n{key.title()} synonyms are:")
            for value in values:
                print(f"\t-{value}")
    # If the answer was no show a goodbye message            
    else:
        print("\nI hope you enjoyed the program. See you!")
# If the word is not in the dict show an apology message
else:
    print("\nSorry, that word is yet to be included in thesaurus. Please reload and try another word")        


