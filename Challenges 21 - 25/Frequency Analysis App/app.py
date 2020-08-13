from collections import Counter

# Welcome message
print("Welcome to the Frequency Analysis App!")

# List with symbols and numbers
non_letters = ["1","2","3","4","5","6","7","8","9","0"," ","?","!",".",",",":",";","-","_","\n","\t","<",">","=","#","'","$","#","/","+","-","*","&"]

# Get first phrase
key_phrase_1 = input("\nEnter a word or a phrase to count the ocurrence of each letter: ").lower().strip()

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

# Using a loop we print only the letters
for letter, count in ordered_letter_count:
    print(letter, end="")

# Get second phrase and do the same as before
key_phrase_2 = input("\n\nEnter a word or a phrase to count the ocurrence of each letter: ").lower().strip()

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


for letter, count in ordered_letter_count2:
    print(letter, end="")

print("\n\nThank you for using the Frequency Analysis App!")    