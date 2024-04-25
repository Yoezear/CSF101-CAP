############################
# Thukten Yoezear
# 1ICE
# 02230229
############################
# REFERENCES
#W3school:https://www.w3schools.com/python/
#https://realpython.com/python-rock-paper-scissors/
############################
# SOLUTION
# Solution Score:50267
############################
def calculate_score(opponent_move, desired_outcome):
    # This function calculates the score for a single round of Rock-Paper-Scissors.
    
    # Define move scores
    move_values = {"A": 1, "B": 2, "C": 3}
    outcome_values = {"X": 0, "Y": 3, "Z": 6}

    # Calculate player's move based on the desired outcome
    player_move = opponent_move  # default to opponent's move
    if desired_outcome == "X":  # player has to lose
        if opponent_move == "A":
            player_move = "C"  # scissor loses to rock
        elif opponent_move == "B":
            player_move = "A"  # rock loses to paper
        elif opponent_move == "C":
            player_move = "B"  # paper loses to scissor
    elif desired_outcome == "Z":
        if opponent_move == "A":
            player_move = "B"  # paper wins against rock
        elif opponent_move == "B":
            player_move = "C"  # scissor wins against paper
        elif opponent_move == "C":
            player_move = "A"  # rock wins against scissor

    # Calculate round score
    round_score = move_values[player_move] + outcome_values[desired_outcome]  # calculate score for each round
    return round_score


# Define input file name
input_filename = f"input_9_cap1.txt"

# Initialize total score
total_game_score = 0

# Read input file
with open(input_filename, "r") as file:
    # Iterate through each line in the file
    for line in file:
        # Remove extra whitespace and split the line into move and outcome
        opponent_play, desired_result = line.strip().split()
        # Calculate round score and update total score
        total_game_score += calculate_score(opponent_play, desired_result)

# Print total score
print(f"Total Game Score: {total_game_score}")
