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
  input("OBJECTIVE 1: OBTAIN CITIZENSHIP")
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
  questions = True
  while questions == True :
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
    input("Press ENTER to see your results. You do not need to press ENTER while we're revealing it.")
    correct_answers = ["3", "4", "2", "1", "2", "1", "2", "1", "3", "4"]
    for i in range(len(answers)):
      time.sleep(1)
      if answers[i] == correct_answers[i]:
        print("Q"+str(i+1)+".", end = " ")
        time.sleep(2)
        print("✓")
      else:
        print("Q"+str(i+1)+".", end=" ")
        time.sleep(2)
        print("X")
    grade = score * 10
    print("Your grade is...",end=" ")
    time.sleep(2)
    print(str(grade)+"%!")
    if grade >= 60 :
      input("You passed! Congratulations! Press ENTER to continue.")
      questions = False
    else :
      input("You failed. You now have to start over. Press ENTER to continue.")
  input("After you passed the citizen, you took the Oath of Alleigance, and became a citizen.")
  input("OBJECTIVE 1 COMPLETED")
  input("OBJECTIVE 2: BE AN INFORMED AND RESPONSIBLE CITIZEN")
  input("Every year on April 4th, you have to pay part of your income to the federal government.")
  input("This is called income tax.")
  input("This helps the government pay for roads, public services, and goods for citizens.")
  input("You soon realize that there are other taxes besides the income tax.")
  input("Every time you buy something at a store or restaraunt, you notice you have a tax added to the total price.")
  input("This is called sales tax.")
  input("You also notice that you pay a tax for everything you own, such as your house and vehicles.")
  input("This is called property tax.")
  input("Finally, you pay another tax called the Social Security tax.")
  input("This goes towards the community so people could go into retirement.")
  input("All these taxes go towards the federal government to help fund public services.")
  input("November, 2024")
  input("There is a presidential election! There are two candidates, Joseph Biden and Donald Trump.")
  input("Joseph Biden: The current president. He has showed that he cares for climate change but handled political affairs poorly. Biden has a low approval rate.")
  input("Donald Trump: Has handled political affairs really well. He established relations with Vladamir Putin, president of Russia, and Kim Jong Un, president of North Korea. However, he has been impeached many times.")
  president = input("Who do you vote for?\n1. Joseph Biden\n2. Donald Trump\n")
  if president == 1 :
    input("Congratulations! You were the tiebreaker! Joesph Biden is the new president.")
  if president == 2 :
    input("Congratulations! You were the tiebreaker! Donald Trump is the new president.")
  else :
    input("It ended in a tie. There was a new vote and Donald Trump ended up winning.")
    president = 2  
  input("OBJECTIVE 2 COMPLETED")
  input("OBJECTIVE 3: KNOW YOUR RIGHTS")
  input("Your rights are listed in the United States Constitution. More specifically, the Bill of Rights.")
  input("The Bill of Rights are the first ten amendments in the Constitution.")
  input("These amendments list the rights of an individual.")
  input("First Amendment: Grants freedom of speech, religion, press, and assembly.")
  input("Second Amendment: Protects the right to bear arms for self defense.")
  input("The Second Amendment has become higlhy controversial recently because people are using weapons for actions other than self defense.")
  input("Third Amendment: prevents the government form forcing you out of your home. The British did this in the Revolutonary War.")