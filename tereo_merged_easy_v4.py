# START OF THE CODE #

print("The Te Reo Moari Quiz\n")
name = input("What is your name? ")
print("\nKia ora {}!".format(name))

# DIFFICULTY SELECT #
# player chooses a difficulty 'NORMAL' or 'HARD'

# difficulty function
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

# print selected difficulty
if diff_mode == "ez":
  heading = "[EASY] Difficulty has been selected"
elif diff_mode == "hard":
  heading = "[HARD] Difficulty has been selected"
print(heading)
print()

# OPTIONS FUNCTION #
# so the player can only select options: 1, 2, 3, 4

def options(question, first, last):
  
  error = "please type either options: 1, 2, 3, 4..."
  
  valid = False
  while not valid:
    try:
      # asks the question
      response = int(input(question))
     # checks if the number response is lower/higher than the options given
      if first < response <= last:
        return response
    
      # error output
      else:
        print(error)
        print()
        
    except ValueError:
      print(error)
      print()


# GAME START #
print("Quiz Starts!")

correct = 0

print("answer by typing either options: 1, 2, 3, 4")
print()

# DIFFICULTY EASY #
# player chose easy mode
if diff_mode == "ez":
  q1 = options("What's Te Reo Maori for ocean? \n1) awa\n2) kātao \n3) moana \n4) roto \n", 0, 4)
  if q1 == 3:
    print("(3) moana is the correct answer!")
    correct += 1
  else:
    print("Good try, (3) moana was the correct answer.") 
  
  q2 = options("What's Te Reo Maori for mountain? \n1) maunga \n2) pikitanga \n3) pōhatu \n4) tuaropari", 0, 4)
  if q2 == 1:
    print("(1) maunga is the correct answer!")
    correct += 1
  else:
    print("Good try, (1) maunga was the correct answer.")

