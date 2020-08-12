print("Welcome to the Fibonacci Calculator App!")

number = int(input("\nHow many digits would you like to compute? "))

# Start of the Fibonacci Sequence
sequence = [1, 1]

# Calculate the next digit in the sequence using a loop
for seq in range(2, number): # the sequence has already 2 items so we start in 2
    sequence.append(sequence[-1] + sequence[-2]) # sum the last 2 digits of the sequence and add to the list

# Display results
print(f"\nThe first {number} numbers of the Fibonacci sequence are:")

for i in sequence:
    print(i)   

# Empty list
golden = []

# Calculate golden ratio
for i in range(len(sequence) - 1):
    ratio = sequence[i + 1] / sequence[i]
    golden.append(ratio)

# Display results
print("\nThe corresponding Golden Ratio values are:")
for gold in golden:
    print(gold)

# Summary
print("\nThe ratio of consecutive Fibonacci terms approaches Phi: 1.618...")   
