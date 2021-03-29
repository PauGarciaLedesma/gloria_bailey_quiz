# Quiz Script

import os
os.system('cls')
score = 0
print("Welcome To The Quiz About Gloria Bailey \n\
Please Input The Letter Of Your Answer In The Space Below The Question. \n\
\n\n")
print("QUESTION 1 - Where was Bailey born?\n",
      "a) England \n",
      "b) Japan \n",
      "c) Jamaica")
answer_1 = input("").lower()
print("Your answer was", answer_1)

if answer_1 == "c":
    print("Correct! Bailey was born in Manchester, Jamaica")
    score += 1
else:
    print("Nice Try! The correct answer was c.")
print("Your current score is:", score)

#-------------------------------------------------------------------------------

print("QUESTION 2 - In what year was Bailey born? \n",
      "a) 1924 \n",
      "b) 2021 \n",
      "c) 1945")
answer_2 = input("").lower()
print("Your answer was", answer_2)

if answer_2 == "a":
    print("Correct! Bailey was born in the year 1924")
    score += 1
else:
    print("Nice Try! The correct answer was a.")
print("Your current score is:", score)

#-------------------------------------------------------------------------------

print("QUESTION 3 - In what year did Bailey pass away? \n",
      "a) 1924 \n",
      "b) 2019 \n",
      "c) 1998")
answer_3 = input("").lower()
print("Your answer was", answer_3)

if answer_3 == "b":
    print("Correct! Bailey died in 2019")
    score += 1
else:
    print("Nice Try! The correct answer was b.")
print("Your current score is:", score)

#-------------------------------------------------------------------------------

print("QUESTION 4 - Which of these is Bailey famous for doing? \n",
      "a) Foster over 100 kids \n",
      "b) Being an emperor in the Roman Empire \n",
      "c) Being the first woman on the Moon")
answer_4 = input("").lower()
print("Your answer was", answer_4)

if answer_4 == "a":
    print("Correct! Bailey fostered over 100 kids!")
    score += 1
else:
    print("Nice Try! The correct answer was a.")
print("Your current score is:", score)

#-------------------------------------------------------------------------------


print("QUESTION 5 - Was Bailey a migrant from the Windrush? \n",
      "a) Yes \n",
      "b) No ")
answer_5 = input("").lower()
print("Your answer was", answer_5)

if answer_5 == "a":
    print("Correct! Bailey was a migrant from the Windrush!")
    score += 1
else:
    print("Nice Try! The correct answer was a.")
print("Your current score is:", score)

#-------------------------------------------------------------------------------

print("QUESTION 6 - A kid that Bailey fostered subsequently went to a country where a war was raging. Where was this? \n",
      "a) China \n",
      "b) USA \n",
      "c) Jamaica \n",
      "d) Sierra Leone")
answer_6 = input("").lower()
print("Your answer was", answer_6)

if answer_6 == "d":
    print("Correct! This kid was around six foot tall when they came to collect him back at the airport.")
    score += 1
else:
    print("Nice Try! The correct answer was d.")
print("Your FINAL score is:", score)
print("\n")
#-------------------------------------------------------------------------------

print("Thanks For Playing The Quiz! I hope you enjoyed it!")
