# START OF THE CODE #

#imports random lib
import random

# colors and stuff
bold = '\033[1m'
italic = '\033[3m'
uline = '\033[4m'
end = '\033[0m' # aka normalize
c_grn = '\033[92m'
c_red = '\033[31m'
c_blu = '\033[34m'

# scoring system, this will add up per correct answer
correct = 0
# the current question number and max number of questions based off difficulty
question_cur = 0
question_max = 0

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
# text color will be green on 'easy' and red on 'hard'
if diff_mode == "ez":
  diff_c = c_grn
  heading = c_grn + "[EASY] Difficulty has been selected" + end
  # The max number of the questions text
  question_max = 10
elif diff_mode == "hard":
  diff_c = c_red
  heading = c_red + "[HARD] Difficulty has been selected"+ end
  # The max number of the questions text
  question_max = 20

# prints heading of the selected difficulty
print()
print(diff_c + "***********************************" + end)
print(heading)
print(diff_c + "***********************************" + end)
print()

# OPTIONS FUNCTION #
# for each question given
# so the 'player' can only select options: 1, 2, 3, 4
def options(answer, first, last):
  # error message
  error = "please type either options: 1, 2, 3, 4..."

  # stops 'player' from proceeding until given a valid response
  valid = False
  while not valid:
    try:
      # asks the question
      response = int(input(answer))
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

# prints a message on how to answer
print("answer by typing either options: 1, 2, 3, 4")
print()

# quiz outerborder to make it look good
border1 = ">>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>"
border2 = "<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<"

# DIFFICULTY EASY #
# player chose easy mode
if diff_mode == "ez":

  # Easy Quiz Questions 1-10
  question = [
    "What's Te Reo Maori for ocean?",
    "What's Te Reo Maori for mountain?",
    "What's Te Reo Maori for land?",
    "What's Te Reo Maori for sun?",
    "What's Te Reo Maori for family?",
    "What's Te Reo Maori for tribe?",
    "What's Te Reo Maori for good morning?",
    "What's Te Reo Maori for good evening?",
    "What's Te Reo Maori for hello?",
    "What's Te Reo Maori for farewell?"
  ]

  # Easy Quiz Correct Answers 1-10
  ans_correct = [
    "moana",
    "maunga",
    "whenua",
    "rā",
    "whānau",
    "iwi",
    "mōrena",
    "tēnā koe i tēnei ahiahi",
    "kia ora",
    "haere rā",
  ]

  # Easy Quiz Incorrect Answers 1-10
  ans_wrong1 = [
    "awa",
    "pikitanga",
    "moutere",
    "rama",
    "hoa",
    "mātāwaka",
    "kia ora",
    "tēnā koe",
    "waimaria",
    "rāhiritanga"
  ]

  ans_wrong2 = [
    "kātao",
    "pōhatu",
    "hangatanga",
    "huru",
    "iwi",
    "āti",
    "e noho rā",
    "tēnā rawa atu koe",
    "ka kite",
    "auina iho"
  ]  
  
  ans_wrong3 = [
    "roto",
    "tuaropari",
    "rangi",
    "whetū",
    "mātāwaka",
    "hoa",
    "rāhiritanga",
    "ata hāpara",
    "rāhiritanga",
    "taritari"
  ]    

# DIFFICULTY HARD #
# player chose hard mode
elif diff_mode == "hard":

  # Hard Quiz Questions 1-20
  question = [
    "What does the the macron do (ā, ē, ī, ō, ū)?",
    "What does “hei tiki” mean in English?",
    "What would be stored in a pātaka?",
    "What would you catch with a trolling lure?",
    "If someone said “Kei te ngenge ahau”, they are feeling..?",
    "“Aroha ahau ki a koe” means what in English?",
    "You would say “Rā whānau ki a koe” to someone on what?",
    "you would wear a hat on your...",
    "On what day would you say “Ngā aroha nui mō te Rā o te Whaea”?",
    "If you wanted to ask your friend where they're going what would you say?",
    "If your friend said “Kei te haere ahau ki te hokomaha” where would they be going?",
    "If pango is black, what else is black?",
    "Which iwi is based from the West Coast of Aotearoa?",
    "What kind of fish did Maui pull up from the ocean and became the North Island?",
    "Matariki is a special occasion in Aotearoa, what sentence isn't true?",
    "What year was the first Māori Language Week?",
    "Māori TV launched on what year?",
    "Which one of these places don't exist in Aotearoa?",
    "When was the Treaty Of Waitangi signed?",
    "When was Te Reo Maori recoginzed as an official language?"
  ]

  # Hard Quiz Correct Answers 1-20
  ans_correct = [
    "lengthens the vowel",
    "neck pendant in the shape of a human figure",
    "kai",
    "ika",
    "tired",
    "I love you",
    "on their birthday",
    "upoko",
    "Mother's Day",
    "kei hea ko?",
    "to the supermarket",
    "mangu",
    "Tainui",
    "a stingray",
    "Matariki can be only seen in Aotearoa",
    "1975",
    "2004",
    "Kaikowhaka",
    "6 February 1840",
    "1 August 1987"
  ]

  # Hard Quiz Incorrect Answers 1-20
  ans_wrong1 = [
    "changes the vowel",
    "good luck charm in the shape of an ancient figure",
    "waka",
    "manu",
    "sad",
    "I love you both",
    "on their summer break",
    "waewae",
    "Easter Day",
    "kei te haere koe ki hea?",
    "to school",
    "kākāriki",
    "Ngāti Tuwharetoa",
    "a shark",
    "Matariki is always in the winter",
    "1959",
    "2000",
    "Kaiwaka",
    "4 Semptember 1845",
    "6 July 1985"
  ]

  ans_wrong2 = [
    "shortens the vowel",
    "ear pendant in the shape of an elden figure",
    "waiwaihā",
    "pekeketua",
    "excited",
    "I love you all",
    "on their anniversary",
    "ihu",
    "Valentine's Day",
    "kei te aha te wā?",
    "to the park",
    "māwhero",
    "Ngāti Porou",
    "a whale",
    "Matariki is known as the beginning of Maori New Year",
    "1963",
    "2002",
    "Kaikoura",
    "9 May 1840",
    "2 February 1986"
  ]  
  
  ans_wrong3 = [
    "ignores the vowel",
    "neck pendant of good fortune",
    "ranea",
    "kāunga",
    "hungry",
    "I love you too",
    "before their vacation",
    "karu",
    "Chirstmas Eve",
    "ko wai tō ingoa?",
    "to the club",
    "parakaraka",
    "Te Rawara",
    "a snapper",
    "Matariki has many different meanings",
    "1968",
    "2006",
    "Kaikohe",
    "13 October 1845",
    "3 December 1989"
  ]

# Question Generation Function
def gen_questions(question, ans_correct, ans_wrong1, ans_wrong2, ans_wrong3):
  global correct # the score
  global question_cur # current question number
  print(border1)
  question_cur += 1

  print(uline + "Question {}/{}".format(question_cur,question_max), question + end)
  # per question it uses the "OPTIONS FUNCTION"
  
  #generates a random number to determine the flow of questions 
  randomize_answers = random.randint(0,3)
  #seperate print statements for readability
  # if the answer is the correct answer, 'correct' variable gets a point (+1)
  # "else:" is a valid input but an incorrect answer
  # after a correct/incorrect answer it proceeds the next questions
 
  if (randomize_answers == 0):
    print("1)", ans_wrong1)
    print("2)", ans_wrong2)
    print("3)", ans_wrong3)
    print("4)", ans_correct)
    ans = options("", 0, 4)
    if ans == 4:
      print(c_grn + "{} is the correct answer, nice {}!".format(ans_correct, name) + end)
      correct += 1
    else:
      print(c_red + "Good try {}, {} was the correct answer.".format(name,ans_correct) + end)
    print(border2)
    print()

  elif (randomize_answers == 1):
    print("1)", ans_correct)
    print("2)", ans_wrong1)
    print("3)", ans_wrong2)
    print("4)", ans_wrong3)
    ans = options("", 0, 4)
    if ans == 1:
      print(c_grn + "{} is the correct answer, nice {}!".format(ans_correct, name) + end)
      correct += 1
    else:
      print(c_red + "Good try {}, {} was the correct answer.".format(name,ans_correct) + end)
    print(border2)
    print()

  elif (randomize_answers == 2):
    print("1)", ans_wrong3)
    print("2)", ans_correct)
    print("3)", ans_wrong1)
    print("4)", ans_wrong2)
    ans = options("", 0, 4)
    if ans == 2:
      print(c_grn + "{} is the correct answer, nice {}!".format(ans_correct, name) + end)
      correct += 1
    else:
      print(c_red + "Good try {}, {} was the correct answer.".format(name,ans_correct) + end)
    print(border2)
    print()    

  elif (randomize_answers == 3):
    print("1)", ans_wrong2)
    print("2)", ans_wrong3)
    print("3)", ans_correct)
    print("4)", ans_wrong1)
    ans = options("", 0, 4)
    if ans == 3:
      print(c_grn + "{} is the correct answer, nice {}!".format(ans_correct, name) + end)
      correct += 1
    else:
      print(c_red + "Good try {}, {} was the correct answer.".format(name,ans_correct) + end)
    print(border2)
    print()      

# generates quiz in easy mode
if diff_mode == "ez":
  for i in range (0,10):
    gen_questions(question[i],ans_correct[i],ans_wrong1[i],ans_wrong2[i],ans_wrong3[i])
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

# generates quiz in hard mode
elif diff_mode == "hard":
  for i in range (0,20):
    gen_questions(question[i],ans_correct[i],ans_wrong1[i],ans_wrong2[i],ans_wrong3[i])
  # results
  # if 'player' gets questions all correct it gives a special message
  if correct == 20:
    print(c_blu + "You aced it {}! You have great Te Reo knowledge! 20/20 Correct".format(name) + end)
  # if 'player' gets nothing correct then it gives a goodluck message
  elif correct <= 0:
    print("That's alright {}, you can always give it another go! 0/20 Correct".format(name))
    # generic message for answering higher than 0 and lower than 20
  else:
    print("Ka pai {}, you can always give it another shot! {}/20 Correct".format(name,correct))    
