# START OF THE CODE #

print("The Te Reo Moari Quiz\n")
name = input("What is your name? ")
print("\nKia Ora {}!".format(name))

# DIFFICULTY SELECT #
# player chooses a difficulty 'NORMAL' or 'HARD'

# Section
def ez_hard(question):
  valid = False
  while not valid:
    difficulty = input(question).lower()

    if difficulty == "easy" or difficulty == "[easy]" or difficulty == "ez":
      difficulty = "ez"
      return difficulty
    elif difficulty == "hard" or difficulty == "[hard]":
      difficulty = "hard"
      return difficulty
      
    else:
      print("please type either [EASY] or [HARD] difficulty... \n")

diff_mode = ez_hard("type either [EASY] or [HARD] difficulty. ".format(name))

if diff_mode == "easy":
  heading = "[EASY] Difficulty has been selected"
elif diff_mode == "hard":
  heading = "[HARD] Difficulty has been selected"
print(heading)

# QUESTIONS SELECT #
# player chooses if they'd want to do 10 or 20 questions