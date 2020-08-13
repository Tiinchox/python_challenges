from collections import Counter

# Welcome message
print("Welcome to the Code Breaker App!")

# List with symbols and numbers
non_letters = ["1","2","3","4","5","6","7","8","9","0"," ","?","!",".",",",":",";","-","_","\n","\t","<",">","=","#","'","$","#","/","+","-","*","&"]

# First phrase
key_phrase_1 = """Following an untimely and embarrassing death, Kazuma Sato, a Japanese teenager shut-in NEET, 
meets a goddess named Aqua, who offers to reincarnate him in a parallel world with MMORPG elements, where he 
can go on adventures and battle monsters. Despite being offered a superpowered item or ability to use in this 
new world, Kazuma, following some provocation, chooses Aqua herself to accompany him to the town of Axel, quickly 
finding her absent-mindedness to be less than beneficial. With Aqua unable to return to the afterlife until 
the Devil King is defeated, the two form a party and recruit two other members; an explosion-obsessed magician 
named Megumin and a masochistic crusader named Darkness. Due to the party's dysfunctional abilities, Kazuma quickly
gives up on the idea of defeating the Devil King and tries to live a luxurious lifestyle, only to find the 
circumstances of his daily life are forcing him and his party to encounter and battle the Devil King's generals.
"""
key_phrase_1 = key_phrase_1.lower()

# Replace non letters in phrase
for non_letter in non_letters:
    key_phrase_1 = key_phrase_1.replace(non_letter,"")

# Count length of phrase
total_ocurrences = len(key_phrase_1)

# Count letters
letter_count = Counter(key_phrase_1)

# Show result
print("\nHere is the frequency analysis from key phrase 1:")
print("\n\tLetter\tOcurrence\tPercentage")

for key, value in sorted(letter_count.items()):
    print(f"\t{key}\t{value}\t\t{round(value * 100 / total_ocurrences,2)}%")

# Show letters ordered
print("\nLetters ordered from highest ocurrence to lowest:")
print("---------------------------------------------------------------")

# Order by ocurrence
ordered_letter_count = Counter(key_phrase_1).most_common() # This will get us a tuple
key_phrase_1_ordered_letters = []

for pair in ordered_letter_count:
    key_phrase_1_ordered_letters.append(pair[0])

# Using a loop we print only the letters
for letter in key_phrase_1_ordered_letters:
    print(letter, end="")

# Second phrase
key_phrase_2 = """In a world of fantasy, adventurers come from far and wide to join the Guild. 
They complete contracts to earn gold and glory. An inexperienced priestess joins her first 
adventuring party, but comes into danger after her first contract involving goblinz goes wrong. 
As the rest of her party is wiped out, she is saved by a man known as Goblin Slayer, an adventurer
whose only purpose is the eradication of goblins with extreme prejudice. 
"""
key_phrase_2 = key_phrase_2.lower()

for non_letter in non_letters:
    key_phrase_2 = key_phrase_2.replace(non_letter,"")

total_ocurrences2 = len(key_phrase_2)

letter_count2 = Counter(key_phrase_2)

print("\nHere is the frequency analysis from key phrase 2:")
print("\n\tLetter\tOcurrence\tPercentage")

for key, value in sorted(letter_count2.items()):
    print(f"\t{key}\t{value}\t\t{round(value * 100 / total_ocurrences2,2)}%")

print("\nLetters ordered from highest ocurrence to lowest:")
print("---------------------------------------------------------------")


ordered_letter_count2 = Counter(key_phrase_2).most_common() 
key_phrase_2_ordered_letters = []

for pair in ordered_letter_count2:
    key_phrase_2_ordered_letters.append(pair[0])

for letter in key_phrase_2_ordered_letters:
    print(letter, end="")

# Get user's choice and a message to encode or decode
choice = input("\n\nWould you like to encode or decode? ").lower()
message = input("Enter your message: ").lower()

# Replace non letters in the message
for non_letter in non_letters:
    message = message.replace(non_letter,"")

# To encode
if choice == "encode":
    encoded_phrase = []
    for letter in message:
        index = key_phrase_1_ordered_letters.index(letter)
        letter = key_phrase_2_ordered_letters[index]
        encoded_phrase.append(letter)

    # Show message
    print("\nYour encoded message is:")
    for letter in encoded_phrase:
        print(letter,end="")

# To decode
elif choice == "decode":
    decoded_phrase = []
    for letter in message:
        index = key_phrase_2_ordered_letters.index(letter)
        letter = key_phrase_1_ordered_letters[index]
        decoded_phrase.append(letter)  

    # Show message
    print("\nYour decoded message is:")
    for letter in decoded_phrase:
        print(letter,end="")

# The user entered an invalid option
else:
    print("\nPlease enter 'encode' or 'decode'. Try again.")


        
