def draw_board(char_list): # Draw Board
    print("\n\t\tTic-Tac-Toe")
    print("\t\t-------------")
    print(f"\t\t||{char_list[0]}||{char_list[1]}||{char_list[2]}||")
    print("\t\t-------------")
    print(f"\t\t||{char_list[3]}||{char_list[4]}||{char_list[5]}||")
    print("\t\t-------------")
    print(f"\t\t||{char_list[6]}||{char_list[7]}||{char_list[8]}||")

def get_player_input(player_char,char_list): # Get player move
    moving = True
    while moving:
        move = int(input(f"\n{player_char}: Where would you like to place your piece? (1 - 9) "))
        if move >= 1 and move <= 9:         # The move must be a number between 1 and 9
            if char_list[move - 1] == "_":  # If the spot is a "_" return the player move
                return move
                moving = False
            else:
                print("\nSorry that place is already taken. Try again.") # If that spot is not a "_" print a message
        else:                               # If the move is anything else, print a message
            print("\nSorry that place is not on the board. Try again.")

def place_char_on_board(player_char,move,char_list): # Change value in board
    char_list[move - 1] = player_char

def is_winner(char_list,player_char): # Check if the player won
    if char_list[0] == player_char and char_list[1] == player_char and char_list[2] == player_char:
        return True
    elif char_list[3] == player_char and char_list[4] == player_char and char_list[5] == player_char:
        return True
    elif char_list[6] == player_char and char_list[7] == player_char and char_list[8] == player_char:
        return True
    elif char_list[0] == player_char and char_list[3] == player_char and char_list[6] == player_char:
        return True
    elif char_list[1] == player_char and char_list[4] == player_char and char_list[7] == player_char:
        return True
    elif char_list[2] == player_char and char_list[5] == player_char and char_list[8] == player_char:
        return True
    elif char_list[0] == player_char and char_list[4] == player_char and char_list[8] == player_char:
        return True
    elif char_list[2] == player_char and char_list[4] == player_char and char_list[6] == player_char:
        return True
    else:
        return False

# Main code
# 2 players
player_1 = "X"
player_2 = "O"

char_list = ["_", "_", "_", "_", "_", "_", "_", "_", "_"] # Game board
num_list = ["1", "2", "3", "4", "5", "6", "7", "8", "9"]  # Move guide

# Print both boards
draw_board(num_list)
draw_board(char_list)

# Keep the app running until a winner is found
winner = "False"
while winner:
    # Player 1 turn
    move = get_player_input(player_1, char_list)
    place_char_on_board(player_1, move, char_list)
    draw_board(num_list)
    draw_board(char_list)
    if is_winner(char_list,player_1):
        print("\nGame ended! Winner player X!") # Game ended
        break
    elif "_" not in char_list:
        print("\nGame ended! It's a tie!") # Game ended
        break

    # Player 2 turn
    move = get_player_input(player_2, char_list)
    place_char_on_board(player_2, move, char_list)
    draw_board(num_list)
    draw_board(char_list)
    if is_winner(char_list,player_2):
        print("\nGame ended! Winner player O!")
        break

