# START OF THE CODE #
# prints the title
print("The Te Reo Moari Quiz\n")

# asks for name (uses name when answering questions), greets 'player'
name = input("What is your name? ")
print("\nKia ora {}!".format(name))

# DIFFICULTY SELECT #
# player chooses a difficulty 'NORMAL' or 'HARD'

# difficulty function
def ez_hard(question):
  # stops 'player' from proceeding until given a valid response
  valid = False
  while not valid:
    # the difficulty input the 'player' submits becomes the 'difficulty' variable 
    difficulty = input(question).lower()

    # only allows 'player' to choose between 'easy' or 'hard' difficulty 
    if difficulty == "easy" or difficulty == "[easy]" or difficulty == "ez":
      difficulty = "ez"
      # difficulty set to easy, 'player' now proceeds
      return difficulty
    elif difficulty == "hard" or difficulty == "[hard]":
      difficulty = "hard"
      # difficulty set to hard, 'player' now proceeds
      return difficulty

    # error output
    else:
      # prints error message, asks the question again
      print("please type either [EASY] or [HARD] difficulty... \n")

# asks player to select the difficulty
diff_mode = ez_hard("type either [EASY] or [HARD] difficulty. ".format(name))

# if the difficulty is 'easy' or 'hard' the heading will be what is in quotations
if diff_mode == "ez":
  heading = "[EASY] Difficulty has been selected"
elif diff_mode == "hard":
  heading = "[HARD] Difficulty has been selected"
# prints heading of the selected difficulty
print(heading)
print()

# OPTIONS FUNCTION #
# for each question given
# so the 'player' can only select options: 1, 2, 3, 4
def options(question, first, last):
  # error message
  error = "please type either options: 1, 2, 3, 4..."

  # stops 'player' from proceeding until given a valid response
  valid = False
  while not valid:
    try:
      # asks the question
      response = int(input(question))
     # checks if the number response is lower/higher than the options given
      if first < response <= last:
        # allows 'player' to proceed to the next question
        return response
    
      # error output
      # prints error if number is less than 1 or more than 4
      # prints error if 'player' uses decimals (eg. 1.35)
      else:
        print(error)
        print()
    # prints error if 'player' types anything besides numbers
    except ValueError:
      print(error)
      print()
  

# GAME START #
print("Quiz Starts!")
# scoring system, this will add up per correct answer
correct = 0
# prints a message on how to answer
print("answer by typing either options: 1, 2, 3, 4")
print()

# DIFFICULTY EASY #
# player chose easy mode
if diff_mode == "ez":
# EXAMPLE:
# per question it uses the "OPTIONS FUNCTION"
# q1 = options("Question 1/10: ...? \n1) ... \n2) ... \n3)... \n4) ... \n", 0 , 4) 
# Question 1/10: ... is question, 0 is first, 4 is last from "OPTIONS FUNCTION"
# "if q1 == 3:" is the correct answer, 'correct' variable gets a point (+1)
# "else:" is a valid input but an incorrect answer
# once 'player' gets a correct/incorrect answer it proceeds the next question
  
  # question 1
  q1 = options("Question 1/10: What's Te Reo Maori for ocean? \n1) awa\n2) kātao \n3) moana \n4) roto \n", 0, 4)
  if q1 == 3:
    print("(3) moana is the correct answer, nice {}!".format(name))
    correct += 1
  else:
    print("Good try {}, (3) moana was the correct answer.".format(name)) 
  print()  
  
  # question 2
  q2 = options("Question 2/10: What's Te Reo Maori for mountain? \n1) maunga \n2) pikitanga \n3) pōhatu \n4) tuaropari \n", 0, 4)
  if q2 == 1:
    print("(1) maunga is the correct answer, nice {}!".format(name))
    correct += 1
  else:
    print("Good try {}, (1) maunga was the correct answer.".format(name))
  print()

  # question 3
  q3 = options("Question 3/10: What's Te Reo Maori for land? \n1) moutere \n2) hangatanga \n3) whenua \n4) rangi \n", 0, 4)
  if q3 == 3:
    print("(3) whenua is the correct answer, nice {}!".format(name))
    correct += 1
  else:
    print("Good try {}, (3) whenua was the correct answer.".format(name))
  print()
  
  # question 4
  q4 = options("Question 4/10: What's Te Reo Maori for sun? \n1) rama \n2) huru \n3) whetū \n4) rā \n", 0, 4)
  if q4 == 4:
    print("(4) rā is the correct answer, nice {}!".format(name))
    correct += 1
  else:
    print("Good try {}, (4) rā was the correct answer.".format(name))
  print()

  # question 5
  q5 = options("Question 5/10: What's Te Reo Maori for family? \n1) hoa \n2) iwi \n3) mātāwaka \n4) whānau \n", 0, 4)
  if q5 == 4:
    print("(4) whānau is the correct answer, nice {}!".format(name))
    correct += 1
  else:
    print("Good try {}, (4) whānau was the correct answer.".format(name))
  print()

  # question 6
  q6 = options("Question 6/10: What's Te Reo Maori for tribe? \n1) mātāwaka \n2) āti \n3) iwi \n4) hoa \n", 0, 4)
  if q6 == 3:
    print("(3) iwi is the correct answer, nice {}!".format(name))
    correct += 1
  else:
    print("Good try {}, (3) iwi was the correct answer.".format(name))
  print()
  
  # question 7
  q7 = options("Question 7/10: What's Te Reo Moari for good morning? \n1) kia ora \n2) mōrena \n3) e noho rā \n4) rāhiritanga \n", 0, 4)
  if q7 == 2:
    print("(2) mōrena is the correct answer, nice {}!".format(name))
    correct += 1
  else:
    print("Good try {}, (2) mōrena was the correct answer.".format(name))
  print()

  # question 8
  q8 = options("Question 8/10: What's Te Reo Moari for good evening? \n1) tēnā koe i tēnei ahiahi \n2) tēnā koe \n3) tēnā rawa atu koe \n4) ata hāpara \n", 0, 4)
  if q8 == 1:
    print("(1) tēnā koe i tēnei ahiahi is the correct answer, nice {}!".format(name))
    correct += 1
  else:
    print("Good try {}, (1) tēnā koe i tēnei ahiahi was the correct answer.".format(name))
  print()

  # question 9
  q9 = options("Question 9/10: What's Te Reo Moari for hello? \n1) waimaria \n2) ka kite \n3) rāhiritanga \n4) kia ora \n", 0, 4)
  if q9 == 4:
    print("(4) kia ora is the correct answer, nice {}!".format(name))
    correct += 1
  else:
    print("Good try {}, (4) kia ora was the correct answer.".format(name))
  print()

  # question 10
  q10 = options("Question 10/10: What's Te Reo Moari for farewell? \n1) rāhiritanga \n2) haere rā \n3) auina iho \n4) taritari \n", 0, 4)
  if q10 == 2:
    print("(2) haere rā is the correct answer, nice {}!".format(name))
    correct += 1
  else:
    print("Good try {}, (2) haere rā was the correct answer.".format(name))
  print()

  # results
  # if 'player' gets questions all correct it gives a special message
  if correct == 10:
    print("You aced it {}! You can go onto [HARD] difficulty next! 10/10 Correct".format(name))
  # if 'player' gets nothing correct then it gives a goodluck message
  elif correct == 0:
    print("That's okay you can try again {}! 0/10 Correct".format(name))
    # generic message for answering higher than 0 and lower than 10
  else:
    print("Well done {}! {}/10 Correct".format(name,correct))

# DIFFICULTY HARD #
# player chose hard mode
elif diff_mode == "hard":
# EXAMPLE:
# per question it uses the "OPTIONS FUNCTION"
# q1 = options("Question 1/20: ...? \n1) ... \n2) ... \n3)... \n4) ... \n", 0 , 4) 
# Question 1/20: ... is question, 0 is first, 4 is last from "OPTIONS FUNCTION"
# "if q1 == 3:" is the correct answer, 'correct' variable gets a point (+1)
# "else:" is a valid input but an incorrect answer
# once 'player' gets a correct/incorrect answer it proceeds the next question  
  
  # question 1
  q1 = options("Question 1/20: What's the job of the macron (ā, ē, ī, ō, ū)? \n1) to change the vowel\n2) to shorten the vowel \n3) to ignore the vowel \n4) to lengthen the vowel \n", 0, 4)
  if q1 == 4:
    print("(4) to lengthen the vowel is the correct answer, nice {}!".format(name))
    correct += 1
  else:
    print("Good try {}, (4) to lengthen the vowel was the correct answer.".format(name)) 
  print()  

  # question 2
  q2 = options("Question 2/20: What's the translation for 'hei tiki'? \n1) neck pendant of human form\n2) good luck charm \n3) ear pendant \n4) pendant of good fortune \n", 0, 4)
  if q2 == 1:
    print("(1) neck pendant of human form is the correct answer, nice {}!".format(name))
    correct += 1
  else:
    print("Good try {}, (1) neck pendant of human form was the correct answer.".format(name)) 
  print()  

  # question 3
  q3 = options("Question 3/20: What would be stored in a pātaka? \n1) waka  \n2) raupanga \n3) kai \n4) pukapuka \n", 0, 4)
  if q3 == 3:
    print("(3) kai is the correct answer, nice {}!".format(name))
    correct += 1
  else:
    print("Good try {}, (3) kai was the correct answer.".format(name)) 
  print()  

  # question 4
  q4 = options("Question 4/20: What would you catch with a pā kahawai? \n1) manu  \n2) pekeketua \n3) ika \n4) kāunga \n", 0, 4)
  if q4 == 3:
    print("(3) ika is the correct answer, nice {}!".format(name))
    correct += 1
  else:
    print("Good try {}, (3) ika was the correct answer.".format(name)) 
  print()  

  # question 5
  q5 = options("Question 5/20: If someone says: ''Kei te ngenge ahau'', they are feeling... \n1) hungry  \n2) sad \n3) tired \n4) drunk \n", 0, 4)
  if q5 == 3:
    print("feeling... (3) tired is the correct answer, nice {}!".format(name))
    correct += 1
  else:
    print("Good try {}, feeling... (3) tired was the correct answer.".format(name))
  print()  

  # question 6
  q6 = options("Question 6/20: ''Aroha ahau ki a koe'' means...  \n1) I love you (singular)  \n2) I love you both (two people) \n3) I love you all (two or more people) \n4) I love myself (singular) \n", 0, 4)
  if q6 == 1:
    print("(1) I love you (singular) is the correct answer, nice {}!".format(name))
    correct += 1
  else:
    print("Good try {}, (1) I love you (singular) was the correct answer.".format(name))
  print()  