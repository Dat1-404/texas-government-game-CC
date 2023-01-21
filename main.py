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
  input("Instructions: Answer the questions with the number assigned to them. For example, if the correct answer is '1. 10', you will answer with '1' and press enter. You must get a 60% or higher to pass.\n")
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
  answer = input("Question54. When is Independence Day?\n1. August 2nd\n2. July 4th\n3. December 25th\n4. November 24th\n")
  if answer == "2" :
    score = score + 1
    answers.append(answer)
  answer = input("What is the national animal of the United States?\n1. Bald Eagle\n2. Armadillo\n3. Unicorn\n4. Bison\n")
  if answer == "1" :
    score = score + 1
    answers.append(answer)
    