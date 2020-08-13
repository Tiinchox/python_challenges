import random

# Welcome message
print("Welcome to the Rock, Paper, Scissor App!")

rounds = int(input("\nHow many rounds would you like to play? "))

moves = ["Rock", "Paper", "Scissors"]

player_score = 0
ai_score = 0

for i in range(rounds):
    print(f"\nRound {i + 1}:")
    print(f"Player: {player_score}\t\tComputer: {ai_score}")

    ai_move = random.randint(0,2)
    if ai_move == 0:
        ai_move = moves[0]
    elif ai_move == 1:
        ai_move = moves[1]
    else: ai_move = moves[2]

    player_move = input("Time to pick... rock, paper, scissors! ").title()
    if player_move in moves:
        print(f"\tComputer: {ai_move}")
        print(f"\tPlayer: {player_move}")
        # Player chooses rock
        if player_move == moves[0] and ai_move == moves[1]:
            print("Paper covers rock!")
            print("Point for me!")
            ai_score += 1
        elif player_move == moves[0] and ai_move == moves[2]:
            print("Rock smashes scissors!")
            print("That's a point for you!")
            player_score += 1
        # Player chooses paper       
        elif player_move == moves[1] and ai_move == moves[0]:
            print("Paper covers rock!")
            print("That's a point for you!")
            player_score += 1
        elif player_move == moves[1] and ai_move == moves[2]:
            print("Scissors cut paper!")
            print("Point for me!")
            ai_score += 1
        # Player chooses scissors
        elif player_move == moves[2] and ai_move == moves[0]:
            print("Rock smashes scissors!")
            print("Point for me!")
            ai_score += 1
        elif player_move == moves[2] and ai_move == moves[1]:          
            print("Scissors cut paper!")
            print("That's a point for you!")
            player_score += 1
        # Tie
        elif player_move == ai_move:
            print("Oww, we got the same! It is a tie!")
        #Other 
        else:
            print("Round winner not calculated.")        
    else: 
        print("Whoops, that is not a valid move!")
        print("Computer gets the point!")
        ai_score += 1

# Winner

if player_score > ai_score:
    winner = "PLAYER! :D"
elif player_score < ai_score:
    winner = "I WIN >:D"
else:
    winner = "IT'S A TIE!"      

# Results
print("\nFinal Game Results:")
print(f"\tRounds Played: {rounds}")
print(f"\tPlayer Score: {player_score}")
print(f"\tComputer Score: {ai_score}")
print(f"\tWinner: {winner}")

