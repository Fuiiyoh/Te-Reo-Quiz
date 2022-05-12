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

    # select between two difficulties 
    if difficulty == "easy" or difficulty == "[easy]" or difficulty == "ez":
      difficulty = "ez"
      return difficulty
    elif difficulty == "hard" or difficulty == "[hard]":
      difficulty = "hard"
      return difficulty

    # error output
    else:
      print("please type either [EASY] or [HARD] difficulty... \n")

# asks player to select the difficulty
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
  # question 1
  q1 = options("Question 1/10: What's Te Reo Maori for ocean? \n1) awa\n2) kātao \n3) moana \n4) roto \n", 0, 4)
  if q1 == 3:
    print("(3) moana is the correct answer!")
    correct += 1
  else:
    print("Good try, (3) moana was the correct answer.") 
  print()  
  
  # question 2
  q2 = options("Question 2/10: What's Te Reo Maori for mountain? \n1) maunga \n2) pikitanga \n3) pōhatu \n4) tuaropari \n", 0, 4)
  if q2 == 1:
    print("(1) maunga is the correct answer!")
    correct += 1
  else:
    print("Good try, (1) maunga was the correct answer.")
  print()

  # question 3
  q3 = options("Question 3/10: What's Te Reo Maori for land? \n1) moutere \n2) hangatanga \n3) whenua \n4) rangi \n", 0, 4)
  if q3 == 3:
    print("(3) whenua is the correct answer!")
    correct += 1
  else:
    print("Good try, (3) whenua was the correct answer.")
  print()
  
  # question 4
  q4 = options("Question 4/10: What's Te Reo Maori for sun? \n1) rama \n2) huru \n3) whetū \n4) rā \n", 0, 4)
  if q4 == 4:
    print("(4) rā is the correct answer!")
    correct += 1
  else:
    print("Good try, (4) rā was the correct answer.")
  print()

  # question 5
  q5 = options("Question 5/10: What's Te Reo Maori for family? \n1) hoa \n2) iwi \n3) mātāwaka \n4) whānau \n", 0, 4)
  if q5 == 4:
    print("(4) whānau is the correct answer!")
    correct += 1
  else:
    print("Good try, (4) whānau was the correct answer.")
  print()

  # question 6
  q6 = options("Question 6/10: What's Te Reo Maori for tribe? \n1) mātāwaka \n2) āti \n3) iwi \n4) hoa \n", 0, 4)
  if q6 == 3:
    print("(3) iwi is the correct answer!")
    correct += 1
  else:
    print("Good try, (3) iwi was the correct answer.")
  print()
  
  # question 7
  q7 = options("Question 7/10: What's Te Reo Moari for good morning? \n1) kia ora \n2) mōrena \n3) e noho rā \n4) rāhiritanga \n", 0, 4)
  if q7 == 2:
    print("(2) mōrena is the correct answer!")
    correct += 1
  else:
    print("Good try, (2) mōrena was the correct answer.")
  print()

  # question 8
  q8 = options("Question 8/10: What's Te Reo Moari for good evening? \n1) tēnā koe i tēnei ahiahi \n2) tēnā koe \n3) tēnā rawa atu koe \n4) ata hāpara \n", 0, 4)
  if q8 == 1:
    print("(1) tēnā koe i tēnei ahiahi is the correct answer!")
    correct += 1
  else:
    print("Good try, (1) tēnā koe i tēnei ahiahi was the correct answer.")
  print()

  # question 9
  q9 = options("Question 9/10: What's Te Reo Moari for hello? \n1) waimaria \n2) ka kite \n3) rāhiritanga \n4) kia ora \n", 0, 4)
  if q9 == 4:
    print("(4) kia ora is the correct answer!")
    correct += 1
  else:
    print("Good try, (4) kia ora was the correct answer.")
  print()

  # question 10
  q10 = options("Question 10/10: What's Te Reo Moari for farewell? \n1) rāhiritanga \n2) haere rā \n3) auina iho \n4) taritari \n", 0, 4)
  if q10 == 2:
    print("(2) haere rā is the correct answer!")
    correct += 1
  else:
    print("Good try, (2) haere rā was the correct answer.")
  print()

  # results
  if correct == 10:
    print("")