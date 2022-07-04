# START OF THE CODE #

#imports random library
import random

# colors and stuff
bold = '\033[1m'
italic = '\033[3m'
underline = '\033[4m'
end = '\033[0m' # aka normalize
green = '\033[92m'
red = '\033[31m'
blue = '\033[34m'

# scoring system, this will add up per correct answer
correct = 0
# the current question number and max number of questions based off difficulty
question_current = 0
question_max = 0

# DIFFICULTY SELECT #
# player chooses a difficulty 'NORMAL' or 'HARD'

# difficulty function
def difficulty_select():
  # stops 'player' from proceeding until given a valid response
  valid = False
  while not valid:
    # the difficulty input the 'player' submits becomes the 'difficulty' variable 
    difficulty = input("type either [EASY] or [HARD] difficulty. ").lower()

    # only allows 'player' to choose between 'easy' or 'hard' difficulty 
    if difficulty == "easy" or difficulty == "[easy]" or difficulty == "ez":
      difficulty = "easy"
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

# OPTIONS FUNCTION #
# for each question given
# so the 'player' can only select options: 1, 2, 3, 4
def options(answer, first_option, last_option):
  # error message
  error = "please type either options: 1, 2, 3, 4..."

  # stops 'player' from proceeding until given a valid response
  valid = False
  while not valid:
    try:
      # asks the question
      response = int(input(answer))
     # checks if the number response is lower/higher than the options given
      if first_option < response <= last_option:
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
  

# prints the title
print(bold + ">>>>>>>>>>>>>>>>>>>>>>")
print(italic + "The Te Reo Maaori Quiz")
print(">>>>>>>>>>>>>>>>>>>>>>" + end)

# asks for name (uses name when answering questions), greets 'player'
name = input("\nWhat is your name? ")
print("\nKia ora {}!".format(name))

# asks player to select the difficulty
difficulty_mode = difficulty_select()

# if the difficulty is 'easy' or 'hard' the heading will be what is in quotations
# text color will be green on 'easy' and red on 'hard'
if difficulty_mode == "easy":
  difficulty_color = green
  heading = green + "[EASY] Difficulty has been selected" + end
  # The max number of the questions text
  question_max = 10
elif difficulty_mode == "hard":
  difficulty_color = red
  heading = red + "[HARD] Difficulty has been selected"+ end
  # The max number of the questions text
  question_max = 20

# prints heading of the selected difficulty
print()
print(difficulty_color + "***********************************" + end)
print(heading)
print(difficulty_color + "***********************************" + end)
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
if difficulty_mode == "easy":

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
  answer_correct = [
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
  answer_wrong1 = [
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

  answer_wrong2 = [
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
  
  answer_wrong3 = [
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
elif difficulty_mode == "hard":

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
    "Which iwi is based from the West Region of Aotearoa?",
    "What kind of fish did Maui pull up from the ocean and became the North Island?",
    "Matariki is a special occasion in Aotearoa, what sentence isn't true?",
    "What year was the first Māori Language Week?",
    "Māori TV launched on what year?",
    "Which one of these places don't exist in Aotearoa?",
    "When was the Treaty Of Waitangi signed?",
    "When was Te Reo Maori recoginzed as an official language?"
  ]

  # Hard Quiz Correct Answers 1-20
  answer_correct = [
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
  answer_wrong1 = [
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

  answer_wrong2 = [
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
  
  answer_wrong3 = [
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
def generate_questions(question, answer_correct, answer_wrong1, answer_wrong2, answer_wrong3):
  global correct # the score
  global question_current # current question number
  print(border1)
  question_current += 1

  print(underline + "Question {}/{}".format(question_current,question_max), question + end)
  # per question it uses the "OPTIONS FUNCTION"
  
  #generates a random number to determine the flow of questions 
  randomize_answers = random.randint(0,3)
  #seperate print statements for readability
  # if the answer is the correct answer, 'correct' variable gets a point (+1)
  # "else:" is a valid input but an incorrect answer
  # after a correct/incorrect answer it proceeds the next questions
 
  if (randomize_answers == 0):
    print("1)", answer_wrong1)
    print("2)", answer_wrong2)
    print("3)", answer_wrong3)
    print("4)", answer_correct)
    option_answer = options("", 0, 4)
    if option_answer == 4:
      print(green + "{} is the correct answer, nice {}!".format(answer_correct, name) + end)
      correct += 1
    else:
      print(red + "Good try {}, {} was the correct answer.".format(name,answer_correct) + end)
    print(border2)
    print()

  elif (randomize_answers == 1):
    print("1)", answer_correct)
    print("2)", answer_wrong1)
    print("3)", answer_wrong2)
    print("4)", answer_wrong3)
    option_answer = options("", 0, 4)
    if option_answer == 1:
      print(green + "{} is the correct answer, nice {}!".format(answer_correct, name) + end)
      correct += 1
    else:
      print(red + "Good try {}, {} was the correct answer.".format(name,answer_correct) + end)
    print(border2)
    print()

  elif (randomize_answers == 2):
    print("1)", answer_wrong3)
    print("2)", answer_correct)
    print("3)", answer_wrong1)
    print("4)", answer_wrong2)
    option_answer = options("", 0, 4)
    if option_answer == 2:
      print(green + "{} is the correct answer, nice {}!".format(answer_correct, name) + end)
      correct += 1
    else:
      print(red + "Good try {}, {} was the correct answer.".format(name,answer_correct) + end)
    print(border2)
    print()    

  elif (randomize_answers == 3):
    print("1)", answer_wrong2)
    print("2)", answer_wrong3)
    print("3)", answer_correct)
    print("4)", answer_wrong1)
    option_answer = options("", 0, 4)
    if option_answer == 3:
      print(green + "{} is the correct answer, nice {}!".format(answer_correct, name) + end)
      correct += 1
    else:
      print(red + "Good try {}, {} was the correct answer.".format(name,answer_correct) + end)
    print(border2)
    print()      

# generates quiz in easy mode
if difficulty_mode == "easy":
  for i in range (0,10):
    generate_questions(question[i],answer_correct[i],answer_wrong1[i],answer_wrong2[i],answer_wrong3[i])
  # results
  # if 'player' gets questions all correct it gives a special message
  if correct == 10:
    print(blue + "You aced it {}! You can go onto [HARD] difficulty next! 10/10 Correct".format(name) + end)
  # if 'player' gets nothing correct then it gives a goodluck message
  elif correct == 0:
    print("That's okay you can try again {}! 0/10 Correct".format(name))
    # generic message for answering higher than 0 and lower than 10
  else:
    print("Ka pai {}, you can always give it another shot! {}/10 Correct".format(name,correct))    

# generates quiz in hard mode
elif difficulty_mode == "hard":
  for i in range (0,20):
    generate_questions(question[i],answer_correct[i],answer_wrong1[i],answer_wrong2[i],answer_wrong3[i])
  # results
  # if 'player' gets questions all correct it gives a special message
  if correct == 20:
    print(blue + "You aced it {}! You have great Te Reo knowledge! 20/20 Correct".format(name) + end)
  # if 'player' gets nothing correct then it gives a goodluck message
  elif correct <= 0:
    print("That's alright {}, you can always give it another go! 0/20 Correct".format(name))
    # generic message for answering higher than 0 and lower than 20
  else:
    print("Ka pai {}, you can always give it another shot! {}/20 Correct".format(name,correct))    
