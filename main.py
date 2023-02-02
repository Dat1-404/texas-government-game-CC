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
    answer = input("Question 4: What country did the United States gain its independence from?\n1. Great Britain\n2. France\n3. Portugal\n4. Spain\n")
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
    choice = input("Press ENTER to see your results. You do not need to press ENTER while we're revealing it. (Also, enter 1 to skip the animation and get instant results)\n")
    correct_answers = ["3", "4", "2", "1", "2", "1", "2", "1", "3", "4"]
    grade = score * 10
    if choice == "1" :
      for i in range(len(answers)):
        if answers[i] == correct_answers[i]:
          print("Q"+str(i+1)+".", end = " ")
          print("✓")
        else:
          print("Q"+str(i+1)+".", end=" ")
          print("X")
      print("Your grade is...",end=" ")
      print(str(grade)+"%!")
    else :
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
  input("This goes towards the community. For example, this tax allow people to go into retirement.")
  input("All these taxes go towards the federal government to help fund public services.")
  input("November, 2024")
  input("There is a presidential election! There are two candidates, Joseph Biden and Donald Trump.")
  input("Joseph Biden: The current president. He has showed that he cares for climate change but handled political affairs poorly. Biden has a low approval rate.")
  input("Donald Trump: Has handled political affairs really well. He established relations with Vladamir Putin, president of Russia, and Kim Jong Un, president of North Korea. However, he has been impeached many times.")
  president = input("Who do you vote for?\n1. Joseph Biden\n2. Donald Trump\n")
  if president == "1" :
    input("Congratulations! You were the tiebreaker! Joesph Biden is the new president.")
    president == int(1)
  elif president == "2" :
    input("Congratulations! You were the tiebreaker! Donald Trump is the new president.")
    president == int(2)
  else :
    input("It ended in a tie. There was a new vote and Donald Trump ended up winning.")
    president = int(2)  
  input("OBJECTIVE 2 COMPLETED")
  input("OBJECTIVE 3: KNOW YOUR RIGHTS")
  input("Your rights are listed in the United States Constitution. More specifically, the Bill of Rights.")
  input("The Bill of Rights are the first ten amendments in the Constitution.")
  input("These amendments list the rights of an individual.")
  input("First Amendment: Grants freedom of speech, religion, press, and assembly.")
  input("Second Amendment: Protects the right to bear arms for self defense.")
  input("The Second Amendment has become higlhy controversial recently because people are using weapons for actions other than self defense.")
  input("Third Amendment: prevents the government form forcing you out of your home. The British did this in the Revolutonary War.")
  input("Fourth Amendment: prevents the government from unreasonable search and seizure of a person. The government would need a search warrant to do this.")
  input("Fifth Amendment: Provides protection for those charged with crimes. Specifically, people charged with a serious crime (felony) must be started by a grand jury. A person cannot be charged twice for the same offense or have property taken away without only compensation. A person cannot say anything self-incriminating and cannot be imprisoned without fair procedures and trials.")
  input("Sixth Amendment: Provides more protections for those who were charged with crimes. It grants the right to a speedy and public trial, trial by an impartial jury, and to be informed of criminal charges. The witness must face the accused, and the accused has the right of their own witnesses and the right to be represented by a lawyer.")
  input("Seventh Amendment: In Federal civil cases, this amendment extends the right to a jury trial.")
  input("Eighth Amendment: Bans excessive bail and fines and cruel and unusual punishment.")
  input("Ninth Amendment: says that listing certain rights in the Constitution does not mean that people don't have other rights that haven't been spelled out.")
  input("Tenth Amendment: says that the Federal Government only has those powers given in the Constitution. If it isn't listed, it belongs to the state or the people.")
  input("These are all the amendments in the Bill of Rights.")
  input("Time for a game.")
  input("This is how to play. I will give you a scenario and you will say if it is with or against the Constitution.")
  input("Respond with 1 if it goes with the Constitution and 2 if not.")
  answers = []
  score = 0
  answer = input("1: Protesting for civil rights.")
  if answer == "1" :
    score = score + 1
  answers.append(answer)
  answer = input("2: Burning down a building and breaking down windows as an act of protest.")
  if answer == "2" :
    score = score + 1
  answers.append(answer)
  answer = input("3: Getting prison for life for stealing.")
  if answer == "2" :
    score = score + 1
  answers.append(answer)
  answer = input("4: Bearing arms for self defense.")
  if answer == "1" :
    score = score + 1
  answers.append(answer)
  answer = input("5: The police searching your home for no reason.")
  if answer == "2" :
    score = score + 1
  answers.append(answer)
  correct_answers = ["1", "2", "2", "1", "2"]
  choice = input("Press ENTER to see your results. You do not need to press ENTER while we're revealing it. (Also, enter 1 to skip the animation and get instant results)\n")
  grade = score * 20
  if choice == "1" :
    for i in range(len(answers)):
      if answers[i] == correct_answers[i]:
        print("Q"+str(i+1)+".", end = " ")
        print("✓")
      else:
        print("Q"+str(i+1)+".", end=" ")
        print("X")
    print("Your grade is...",end=" ")
    print(str(grade)+"%!")
  else :
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
    print("Your grade is...",end=" ")
    time.sleep(2)
    print(str(grade)+"%!")
  input("OBJECTIVE 3 COMPLETED")
  input("PART 1 COMPLETE")
  part2 = True
  while part2 == True :
    input("Part 2: Government Official")
    input("Scenario: You are a government official hoping to become president. You must climb up the ranks, starting from local government.")
    input("Objectives:\n1. Become president")
    input("You successfully got elected mayor of Houston. You will need to provide public services to your municipality.")
    input("The Houston government is mayor-council.")
    input("The council is legislative and the mayor is executive.")
    input("This means that the council passes laws and the mayor enforces them.")
    input("One day, the United States declared war on Russia and China after the Russia-Ukraine conflict escalated.")
    input("Protests erupted across Houston against the war.")
    input("The anti-war movement quickly developed from a peaceful protest to a very violent protest.")
    input("Many people were damaging the Houston City Hall, which is against the law.")
    answer = input("What do you do?\n1. Send a police force to stop the protest.\n2. Nothing\n")
    if answer == "1" :
      input("You successfully stopped the protest. The police force arrested about 20 people that were damaging the city hall, and they were charged with crimes.")
      input("The United States and its allies won the war, turning the nationwide protests to a wave of celebration.")
      input("This led to the end of China's communist government and the end of the Russia-Ukraine conflict.")
      input("2 years later, the state elections take place.")
      pp = input("What political party will you go for?\n1. Democratic\n2. Republican\n")
      if pp == "1" :
        print("You chose to run as a Democrat.")
        pp = 1
        pps = "Democrat"
      if pp == "2" :
        print("You chose to run as a Republican.")
        pp = 2
        pps = "Republican"
      input("You ran in the election. People supported your decision to responsibly stop the protests in your city, and they voted for you. You now represent Texas as a "+pps+".")
      input("As part of the Senate, you vote on whether or not you want a law to be passed based on your political beliefs.")
      input("As you passed more laws, people started believing you would make a great president.")
      input("2036 PRESIDENTIAL ELECTION")
      if pp == 1 :
        input("You are the candidate for the Democrats, and the candidate for the Republicans is J.D Vance, the Republican senator from Ohio.")
        input("Both of you pointed their views on many things, and you competed with candidates from other political parties.")
        input("You witnessed many states shift towards your favor, and finally, the counting.")
        input("Votes are counted in the Capitol Building.")
        input("A few days later...")
        input("The results are posted. You go onto the news, and then, you see your face appear.")
        input("Congratulations! You have won the election!")
      if pp == 2 :
        input("You are the candidate for the Republicans, and the candidate for the Democrats is Jon Ossof, the Demcoratic senator from Georgia.")
        input("Both of you pointed their views on many things, and you competed with candidates from other political parties.")
        input("You witnessed many states shift towards your favor, and finally, the counting.")
        input("Votes are counted in the Capitol Building.")
        input("A few days later...")
        input("The results are posted. You go onto the news, and then, you see your face appear.")
        input("Congratulations! You have won the election!")
      input("In the Oval Office, you enforce laws just like how you did as a mayor. People seemed to enjoy you being president, and you make good decisions.")
      input("You also have an approval rating of 81%.")
      input("This is it. You have finally done it after the span of many years. You have become president of the United States.")
      input("OBJECTIVE 1 COMPLETE")
      input("Before we finish the game, I would like to review as this was a short part.")
      input("In most governements, including state and federal, there are three branches: Legislative, Executive, and Judicial.")
      input("Legislative passes laws, executive enforces them, and judicial makes sure that criminals get a proper punisment according to the Constitution.")
      input("There are also local government who handle a specific area, such as public services and taxes in a county.")
      input("There are municipal governments, who have a legislative and executive branch (mayor-council) and there is also a council-manager government.")
      input("There is also county governments, which provide public services, collect taxes, etc.")
      input("There are many courts which are part of the Judicial Branch of the state or the federal government.")
      input("Well, this is the unit recapped in a game. Hope you enjoyed.")
      input("PART 2 COMPLETE")
      input("GAME COMPLETE")
    if answer == "2" :
      input("You did nothing to stop the protests. As people cheered, the City Hall fell, just like your dreams of becoming president.")
      
    