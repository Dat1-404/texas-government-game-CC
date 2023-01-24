import time

print("Texas Government Game")
time.sleep(1)
print("The terminal game that was made because Pygame is too hard")
time.sleep(1)
var1 = int(input("Select an option:\n1. Play\n2. Credits\n"))
if var1 == 1 :
  input("DON'T EXIT OUT! This game doesn't have a saving mechanism.")
  input("Part 1: Citizen")
  input("Scenario: You are a 20-year-old immigrant from Mexico.\nYou plan to gain citizenship through naturalization.")
  input("Objectives:\n1. Gain citizenship\n2. Be a responsible and informed citizen\n3. Know your rights")
  input("You arrive from Mexico City to Houston for a chance to have better oppurtunities.")
  input("After getting a visa, you head to migration so you can go out of the airport.")
  input("You decide to permanently reside in the U.S, so you get a green card.")
  input("5 years later...")
  input("After becoming eligible for naturalization, you apply and pay the requisite fees.")
  input("After you applied, you must take the American Civics Test.")
  input("After demonstrating a good moral character and a lack of criminal history, you are to be tested on United States history and civics.")
  input("Luckily for you, you learned English before coming here, which you must know.")
  input("\nTHE AMERICAN CIVICS TEST\n")
  input("Instructions: Answer the questions with the number assigned to the answer. For example, if the correct answer is '1. 10', you will answer with '1' and press enter. You must get a 60% or higher to pass.\n")
  answers = []
  score = 0
  answer = input("Question 1: How many branches are there?\n1. 1\n2. 2\n3. 3\n4. 4\n")
  if answer == "3" :
    score = score + 1
  answers.append(answer)
  answer = input("Question 2: How many amendments are in the Bill of Rights?\n1. 5\n2. 13\n3. 12\n4. 10\n")
  if answer == "4" :
    score = score + 1
  answers.append(answer)
  answer = input("Question 3: In what year did the United States gain independence?\n1. 1778\n2. 1776\n3. 1789\n4. 1700\n")
  if answer == "2" :
    score = score + 1
  answers.append(answer)
  answer = input("Question 4: What country did the United States gain it's independence from?\n1. Great Britain\n2. France\n3. Portugal\n4. Spain\n")
  if answer == "1" :
    score = score + 1
  answers.append(answer)
  answer = input("Question 5: When is Independence Day?\n1. August 2nd\n2. July 4th\n3. December 25th\n4. November 24th\n")
  if answer == "2" :
    score = score + 1
  answers.append(answer)
  answer = input("Question 6: What is the national animal of the United States?\n1. Bald Eagle\n2. Armadillo\n3. Unicorn\n4. Bison\n")
  if answer == "1" :
    score = score + 1
  answers.append(answer)
  answer = input("Question 7: On what side did the United States fight on during WWII?\n1. Axis\n2. Allies\n3. Central\n4. Neutral\n")
  if answer == "2" :
    score = score + 1
  answers.append(answer)
  answer = input("Question 8: How many states are in the U.S?\n1. 50\n2. 13\n3. 55\n4. 45\n")
  if answer == "1" :
    score = score + 1
  answers.append(answer)
  answer = input("Question 9: How many colonies were there?\n1. 50\n2. 55\n3. 13\n4. 45\n")
  if answer == "3" :
    score = score + 1
  answers.append(answer)
  answer = input("Question 10: What branch contains the president?\n1. Judicial\n2. Tree Branch\n3. Legislative\n4. Executive\n")
  if answer == "4" :
    score = score + 1
  answers.append(answer)
  correct_answers = ["3", "4", "2", "1", "2", "1", "2", "1", "3", "4"]
  for i in range(len(answers)):
    time.sleep(1)
    if answers[i] == correct_answers[i]:
      print("Q"+str(i+1)+".", end = " ")
      time.sleep(3)
      print("✓")
    else:
      print("Q"+str(i+1)+".", end=" ")
      time.sleep(3)
      print("X")

