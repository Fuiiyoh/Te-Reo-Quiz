# START OF THE CODE #

print("The Te Reo Moari Quiz\n")
name = input("What is your name? ")

# DIFFICULTY SELECT #
# player chooses a difficulty 'NORMAL' or 'HARD'
difficulty = input("\nKia Ora {}!\ntype either [EASY] or [HARD] difficulty. ".format(name)).lower()

if difficulty == "easy" or difficulty == "[easy]" or difficulty == "ez":
  difficulty = "ez"
  heading = "[EASY] Difficulty has been selected"
elif difficulty == "hard" or difficulty == "[hard]":
  difficulty = "hard"
  heading = "[HARD] Difficulty has been selected"
  
print(heading)

# QUESTIONS SELECT #
# player chooses if they'd want to do 10 or 20 questions