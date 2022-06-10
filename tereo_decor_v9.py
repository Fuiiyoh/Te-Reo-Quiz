# START OF THE CODE #
# colors and stuff
bold = '\033[1m'
italic = '\033[3m'
uline = '\033[4m'
end = '\033[0m' # aka normalize
c_grn = '\033[92m'
c_red = '\033[31m'
c_blu = '\033[34m'

# prints the title
print(bold + ">>>>>>>>>>>>>>>>>>>>>>")
print(italic + "The Te Reo Moari Quiz")
print(">>>>>>>>>>>>>>>>>>>>>>" + end)

# asks for name (uses name when answering questions), greets 'player'
name = input("\nWhat is your name? ")
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
  heading = c_grn + "[EASY] Difficulty has been selected" + end
elif diff_mode == "hard":
  heading = c_red + "[HARD] Difficulty has been selected"+ end
# difficulty border color
if diff_mode == "ez":
  diff_c = c_grn
elif diff_mode == "hard":
  diff_c = c_red
# prints heading of the selected difficulty
print()
print(diff_c + "***********************************" + end)
print(heading)
print(diff_c + "***********************************" + end)
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
print(italic + "Quiz Starts!" + end)
# scoring system, this will add up per correct answer
correct = 0
# prints a message on how to answer
print("answer by typing either options: 1, 2, 3, 4")
print()

# quiz outerborder to make it look good
border1 = ">>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>"
border2 = "<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<"

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
  print(border1)
  q1 = options(uline + "Question 1/10: What's Te Reo Maori for ocean?"+ end + "\n1) awa\n2) kātao \n3) moana \n4) roto \n", 0, 4)
  if q1 == 3:
    print(c_grn + "(3) moana is the correct answer, nice {}!".format(name) + end)
    correct += 1
  else:
    print(c_red + "Good try {}, (3) moana was the correct answer.".format(name) + end) 
  print(border2)
  print()  
  
  # question 2
  print(border1)
  q2 = options(uline + "Question 2/10: What's Te Reo Maori for mountain?" + end + "\n1) maunga \n2) pikitanga \n3) pōhatu \n4) tuaropari \n", 0, 4)
  if q2 == 1:
    print(c_grn + "(1) maunga is the correct answer, nice {}!".format(name) + end)
    correct += 1
  else:
    print( c_red + "Good try {}, (1) maunga was the correct answer.".format(name) + end)
  print(border2)
  print()

  # question 3
  print(border1)
  q3 = options(uline + "Question 3/10: What's Te Reo Maori for land?" + end + "\n1) moutere \n2) hangatanga \n3) whenua \n4) rangi \n", 0, 4)
  if q3 == 3:
    print(c_grn + " (3) whenua is the correct answer, nice {}!".format(name) + end)
    correct += 1
  else:
    print(c_red + "Good try {}, (3) whenua was the correct answer.".format(name) + end)
  print(border2)
  print()
  
  # question 4
  print(border1)
  q4 = options(uline + "Question 4/10: What's Te Reo Maori for sun?" + end + "\n1) rama \n2) huru \n3) whetū \n4) rā \n", 0, 4)
  if q4 == 4:
    print(c_grn + "(4) rā is the correct answer, nice {}!".format(name) + end)
    correct += 1
  else:
    print(c_red + "Good try {}, (4) rā was the correct answer.".format(name) + end)
  print(border2)
  print()

  # question 5
  print(border1)
  q5 = options(uline + "Question 5/10: What's Te Reo Maori for family?" + end + "\n1) hoa \n2) iwi \n3) mātāwaka \n4) whānau \n", 0, 4)
  if q5 == 4:
    print(c_grn + "(4) whānau is the correct answer, nice {}!".format(name) + end)
    correct += 1
  else:
    print(c_red + "Good try {}, (4) whānau was the correct answer.".format(name) + end)
  print(border2)
  print()

  # question 6
  print(border1)
  q6 = options(uline + "Question 6/10: What's Te Reo Maori for tribe?" + end + "\n1) mātāwaka \n2) āti \n3) iwi \n4) hoa \n", 0, 4)
  if q6 == 3:
    print(c_grn + "(3) iwi is the correct answer, nice {}!".format(name) + end) 
    correct += 1
  else:
    print(c_red + "Good try {}, (3) iwi was the correct answer.".format(name) + end)
  print(border2)
  print()
  
  # question 7
  print(border1)
  q7 = options(uline + "Question 7/10: What's Te Reo Moari for good morning?" + end + "\n1) kia ora \n2) mōrena \n3) e noho rā \n4) rāhiritanga \n", 0, 4)
  if q7 == 2:
    print(c_grn + "(2) mōrena is the correct answer, nice {}!".format(name) + end)
    correct += 1
  else:
    print(c_red + "Good try {}, (2) mōrena was the correct answer.".format(name) + end)
  print(border2)
  print()

  # question 8
  print(border1)
  q8 = options(uline + "Question 8/10: What's Te Reo Moari for good evening?" + end + "\n1) tēnā koe i tēnei ahiahi \n2) tēnā koe \n3) tēnā rawa atu koe \n4) ata hāpara \n", 0, 4)
  if q8 == 1:
    print(c_grn + "(1) tēnā koe i tēnei ahiahi is the correct answer, nice {}!".format(name) + end)
    correct += 1
  else:
    print(c_red + "Good try {}, (1) tēnā koe i tēnei ahiahi was the correct answer.".format(name) + end)
  print(border2)
  print()

  # question 9
  print(border1)
  q9 = options(uline + "Question 9/10: What's Te Reo Moari for hello?" + end + "\n1) waimaria \n2) ka kite \n3) rāhiritanga \n4) kia ora \n", 0, 4)
  if q9 == 4:
    print(c_grn + "(4) kia ora is the correct answer, nice {}!".format(name) + end)
    correct += 1
  else:
    print(c_red + "Good try {}, (4) kia ora was the correct answer.".format(name) + end)
  print(border2)
  print()

  # question 10
  print(border1)
  q10 = options(uline + "Question 10/10: What's Te Reo Moari for farewell?" + end + "\n1) rāhiritanga \n2) haere rā \n3) auina iho \n4) taritari \n", 0, 4)
  if q10 == 2:
    print(c_grn + "(2) haere rā is the correct answer, nice {}!".format(name) + end)
    correct += 1
  else:
    print(c_red + "Good try {}, (2) haere rā was the correct answer.".format(name) + end)
  print(border2)
  print()

  # results
  # if 'player' gets questions all correct it gives a special message
  if correct == 10:
    print(c_blu + "You aced it {}! You can go onto [HARD] difficulty next! 10/10 Correct".format(name) + end)
  # if 'player' gets nothing correct then it gives a goodluck message
  elif correct == 0:
    print("That's okay you can try again {}! 0/10 Correct".format(name))
    # generic message for answering higher than 0 and lower than 10
  else:
    print("Ka pai {}, you can always give it another shot! {}/10 Correct".format(name,correct))

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
  q2 = options("Question 2/20: What's the translation for “hei tiki”? \n1) neck pendant of human form\n2) good luck charm \n3) ear pendant \n4) pendant of good fortune \n", 0, 4)
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
  q5 = options("Question 5/20: If someone says: “Kei te ngenge ahau”, what are they feeling? \n1) hungry  \n2) sad \n3) tired \n4) drunk \n", 0, 4)
  if q5 == 3:
    print(" (3) tired is the correct answer, nice {}!".format(name))
    correct += 1
  else:
    print("Good try {}, (3) tired was the correct answer.".format(name))
  print()  

  # question 6
  q6 = options("Question 6/20: “Aroha ahau ki a koe” means...  \n1) I love you  \n2) I love you both \n3) I love you all \n4) I love myself \n", 0, 4)
  if q6 == 1:
    print("(1) I love you is the correct answer, nice {}!".format(name))
    correct += 1
  else:
    print("Good try {}, (1) I love you was the correct answer.".format(name))
  print()  

  # question 7
  q7 = options("Question 7/20: “Rā whānau ki a koe” is what you'd say to someone... \n1) on their wedding anniversary \n2) before they go on holiday \n3) on their promotion \n4) on their birthday \n", 0, 4)
  if q7 == 4:
    print("(4) on their birthday is the correct answer, nice {}!".format(name))
    correct += 1
  else:
    print("Good try {}, (4) on their birthday was the correct answer.".format(name))
  print()  

  # question 8
  q8 = options("Question 8/20: you would wear a hat on your... \n1) waewae \n2) upoko \n3) ihu \n4) karu \n", 0, 4)
  if q8 == 2:
    print("(2) upoko is the correct answer, nice {}!".format(name))
    correct += 1
  else:
    print("Good try {}, (2) upoko was the correct answer.".format(name))
  print()    

  # question 9
  q9 = options("Question 9/20: On what day would you say: “Ngā mihi me te aroha nui mō te Rā o te Whaea”? \n1) Valentine's Day \n2) Chirstmas Day \n3) Father's Day \n4) Mother's Day \n", 0, 4)
  if q9 == 4:
    print("(4) Mother's Day is the correct answer, nice {}!".format(name))
    correct += 1
  else:
    print("Good try {}, (4) Mother's Day was the correct answer.".format(name))
  print()  

  # question 10
  q10 = options("Question 10/20: If someone told you “Kei te haere ahau ki te hokomaha” where would they be going? \n1) to the supermarket \n2) to school \n3) to the swimming pool \n4) to the park \n", 0, 4)
  if q10 == 1:
    print("(1) to the supermarket is the correct answer, nice {}!".format(name))
    correct += 1
  else:
    print("Good try {}, (1) to the supermarket was the correct answer.".format(name))
  print()  

  # question 11
  q11 = options("Question 11/20: If you wanted to ask your friend where he's/she's going what would you say? \n1) kei hea ko? \n2) kei te haere koe ki hea? \n3) kei te aha te wā? \n4) ko wai tō ingoa? \n", 0, 4)
  if q11 == 1:
    print("(1) kei hea ko? is the correct answer, nice {}!".format(name))
    correct += 1
  else:
    print("Good try {}, (1) kei hea ko? was the correct answer.".format(name))
  print()  

  # question 12
  q12 = options("Question 12/20: Pango is black, what else is black? \n1) mangu \n2) kākāriki \n3) māwhero \n4) parakaraka \n", 0, 4)
  if q12 == 1:
    print("(1) mangu is the correct answer, nice {}!".format(name))
    correct += 1
  else:
    print("Good try {}, (1) mangu was the correct answer.".format(name))
  print()  

  # question 13
  q13 = options("Question 13/20: Which iwi are from the East Coast of Aotearoa? \n1) Ngāti Tuwharetoa \n2) Ngāti Porou \n3) Te Rawara \n4) Tainui \n", 0, 4)
  if q13 == 2:
    print("(2) Ngāti Porou is the correct answer, nice {}!".format(name))
    correct += 1
  else:
    print("Good try {}, (2) Ngāti Porou was the correct answer.".format(name))
  print()  

  # question 14
  q14 = options("Question 14/20: What kind of fish did Maui pull up from the ocean and became the North Island? \n1) a shark \n2) a stingray \n3) a whale \n4) a snapper \n", 0, 4)
  if q14 == 2:
    print("(2) a stingray is the correct answer, nice {}!".format(name))
    correct += 1
  else:
    print("Good try {}, (2) a stingray was the correct answer.".format(name))
  print()  

  # question 15
  q15 = options("Question 15/20: Matariki is a special time of the year in Aotearoa. Which sentence isn't true? \n1) Matariki is always in winter \n2) Matariki's stars can be only seen in Aotearoa \n3) Matariki is known as the beginning of Maori New Year \n4) Matariki has more than one meaning \n", 0, 4)
  if q15 == 2:
    print("(2) Matariki's stars can be only seen in Aotearoa is the correct answer, nice {}!".format(name))
    correct += 1
  else:
    print("Good try {}, (2) Matariki's stars can be only seen in Aotearoa was the correct answer.".format(name))
  print()  

  # question 16
  q16 = options("Question 16/20: When was the first Māori Language Week? \n1) 1959 \n2) 1963 \n3) 1968 \n4) 1975 \n", 0, 4)
  if q16 == 4:
    print("(4) 1975 is the correct answer, nice {}!".format(name))
    correct += 1
  else:
    print("Good try {}, (4) 1975 was the correct answer.".format(name))
  print()  

  # question 17
  q17 = options("Question 17/20: When was Māori TV launched? \n1) 2000 \n2) 2002 \n3) 2004 \n4) 2006 \n", 0, 4)
  if q17 == 3:
    print("(3) 2004 is the correct answer, nice {}!".format(name))
    correct += 1
  else:
    print("Good try {}, (3) 2004 was the correct answer.".format(name))
  print()  

  # question 18
  q18 = options("Question 18/20: Which one of these places don't exist in Aotearoa? \n1) Kaiwaka \n2) Kaikowhaka \n3) Kaikoura \n4) Kaikohe \n", 0, 4)
  if q18 == 2:
    print("(2) Kaikowhaka is the correct answer, nice {}!".format(name))
    correct += 1
  else:
    print("Good try {}, (2) Kaikowhaka was the correct answer.".format(name))
  print()  

    # question 19
  q19 = options("Question 19/20: When was the Treaty Of Waitangi signed? \n1) 4 Semptember 1845 \n2) 9 May 1840 \n3) 13 October 1845 \n4) 6 February 1840 \n", 0, 4)
  if q19 == 4:
    print("(4) 6 February 1840 is the correct answer, nice {}!".format(name))
    correct += 1
  else:
    print("Good try {}, (4) 6 February 1840 was the correct answer.".format(name))
  print()  

  # question 20
  q20 = options("Question 20/20: When was Te Reo Maori recoginzed as an official language? \n1) 1 August 1987 \n2) 6 July 1985 \n3) 2 February 1986 \n4) 3 December 1989 \n", 0, 4)
  if q20 == 1:
    print("(1) 1 August 1987 is the correct answer, nice {}!".format(name))
    correct += 1
  else:
    print("Good try {}, (1) 1 August, 1987 was the correct answer.".format(name))
  print()  

  # results
  # if 'player' gets questions all correct it gives a special message
  if correct == 20:
    print("You aced it {}! You have great Te Reo knowledge! 20/20 Correct".format(name))
  # if 'player' gets nothing correct then it gives a goodluck message
  elif correct <= 0:
    print("That's alright {}, you can always give it another go! 0/20 Correct".format(name))
    # generic message for answering higher than 0 and lower than 20
  else:
    print("Ka pai {}, you can always give it another shot! {}/20 Correct".format(name,correct))