
def calculate_score(given_move, given_outcome):
#Define function to calculate score with two parameter given_move, and desired_outcome
  """
  Calculates the score for a single round of Rock-Paper-Scissors.

  define:
    given_move: A character representing the opponent's move (A for Rock, B for Paper, C for Scissors).
    desired_outcome: A character representing the desired outcome (X for lose, Y for draw, Z for win).

  Returns:
    The total score for the round.
  """
  # Define move scores
  moves_scores = {"A": 1, "B": 2, "C": 3}
  outcome_scores = {"X": 0, "Y": 3, "Z": 6}

  # TO Calculate Player move based on desired outcome
  player_move = given_move#for the draw
  if given_outcome == "X":#player have to lose
    if given_move == "A":
      player_move = "C"  # scissor loses to rock
    elif given_move == "B":
      player_move = "A"  # rock loses to paper
    elif given_move == "C":
      player_move = "B"  # paper loses to scissor
  elif given_outcome == "Z":
    if given_move == "A":
      player_move = "B"  # paper wins against rock
    elif given_move == "B":
      player_move = "C"  # scissor wins against paper
    elif given_move == "C":
      player_move = "A"  # rock wins against scissor

  # Calculate round score
  round_score = moves_scores[player_move] + outcome_scores[given_outcome]#calculate score for each rounds

  return round_score

def main():

  # Define input file name
  input_file = f"input_9_cap1.txt"

  # To read input file
  total_score = 0#Empty variable to calculate total score for every round
  with open(input_file, "r") as file:
    for line in file:# each line in the file
      given_move, given_outcome = line.strip().split()#used for removing extra whitespaces and specific characters and split function split the str into list
      round_score = calculate_score(given_move, given_outcome)
      total_score += round_score

  # Print total score
  print(f"Total Score: {total_score}")

if __name__ == "__main__":
  main()# this conditional statement tells when the main module is interpreted