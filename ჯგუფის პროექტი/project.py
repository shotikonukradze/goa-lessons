print("Hello to our Quiz Game")
print("======================")
input("Press enter to continue.")
print("==================================")
print("We will challenge you to our IQ test")
print("==============================")

wanna_play = input("Do you want to play a game? (yes/no): ")
if wanna_play.lower() != "yes":
    print("Goodbye!")
    quit()
print("====================================")
print("Okay, let's start then")
input("Press enter to start. ")
print("====================================")
print("First of all, you must choose the difficulty of the quiz:")
print("1. Beginner  (Iq 4)")
print("2. Medium    (Iq 9)")
print("3. Expert    (Iq 15)")
difficulty = int(input(": "))

if difficulty == 1:
    print("====================================")

# Initialize total score
    total_score = 0

    # Define scores
    question1 = 4
    question2 = 4
    question3 = 4
    question4 = 4
    question5 = 4
    question6 = 4
    question7 = 4
    question8 = 4
    question9 = 4
    question10 = 4
    goa_question1 = 20


    # First Question
    print("number in the series: 2, 4, 6, 8, _?")
    answer1 = int(input("Your answer here: "))
    if answer1 == 10:
        print("Good guess!")
        total_score += question1
    else:
        print("Incorrect.")
    print("====================================")
    # Second Question
    print("What is the capital of Australia?")
    answer2 = input("Your answer here: ")
    if answer2.strip().lower() == "Canberra".lower():
        print("WOW!")
        total_score += question2
    else:
        print("Incorrect.")
    print("====================================")
    # Third Question
    print("If you have 12 apples and give away 5, how many apples do you have left?")
    answer3 = input("Your answer here: ")
    if answer3  == "7" or answer3.strip().lower() == "seven".lower():
        print("Impressive!")
        total_score += question3
    else:
        print("Incorrect.")
    print("====================================")
    #forth
    print("What is 9 + 10?")
    answer4 = int(input("Your answer here: "))
    if answer4  == 19:
        print("Good guess!")
        total_score += question4
    else:
        print("Incorrect.")
    print("====================================")
    #fifth
    print("Which number is missing in the sequence: 3, 6, 9, _?")
    answer5 = int(input("Your answer here: "))
    if answer5  == 12:
        print("good job!")
        total_score += question5    
    else:
        print("Incorrect.")
    print("====================================")
    #six
    print("How many weeks are there in a year?")
    answer6 = input("Your answer here: ")
    if answer6  == "52":
        print("Good guess!")
        total_score += question6
    else:
        print("Incorrect.")
    print("====================================")
    #seven
    print("What is the opposite of full?")
    answer7 = input("Your answer here: ")
    if answer7.strip().lower() == "empty":
        print("WOW!")
        total_score += question7
    else:
        print("Incorrect.")
    print("====================================")
    #eight
    print("If a book has 300 pages and you read 75, how many pages are left?")
    answer8 = int(input("Your answer here: "))
    if answer8  == 225:
        print("Good guess!")
        total_score += question8
    else:
        print("Incorrect.")
    print("====================================")
    #nine
    print("What day comes after Sunday?")
    answer9 = input("Your answer here: ")
    if answer9.strip().lower() == "monday": 
        print("Impressive!")
        total_score += question9
    else:
        print("Incorrect.")
    print("====================================")
    #ten
    print("What shape has 4 equal sides and 4 right angles?")
    answer10 = input("Your answer here: ")
    if answer10.strip().lower() == "Square".lower():
        print("Good guess!")
        total_score += question10
    else:
        print("Incorrect.")

        print("====================================")
    print("hardest question, best proggraming accademy in the world?")
    goa_answer = input("your answer here: ")
    if goa_answer.strip().lower() == "GOA".lower() or "GOA best".lower():
        total_score += goa_question1
    else:
        print("- unlimited aura")

    print("====================================")
    # Print the total Iq
    print("Your total Iq is:", total_score)



if difficulty == 2:
    print("====================================")

    total_score2 = 0

    # Define scores
    question1med = 9
    question2med = 9
    question3med = 9
    question4med = 9
    question5med = 9
    question6med = 9
    question7med = 9
    question8med = 9
    question9med = 9
    question10med = 9


    # First Question
    print("What is the next number in the series: 2, 5, 10, 17, 26, _? (Hint: The sequence is created by adding consecutive odd numbers.)")
    answer11 = int(input("Your answer here: "))
    if answer11 == 37:
        print("Good guess!")
        total_score2 += question1med
    else:
        print("Incorrect.")
    print("====================================")
    # Second Question
    print("Rearrange the letters of “PRESERVE” to form a word that means “to keep safe.” What is it?")
    answer12 = input("Your answer here: ")
    if answer12.strip().lower() == "Synonyms":
        print("Good guess!")
        total_score2 += question2med
    else:
        print("Incorrect.")
    print("====================================")
    # Third Question
    print("Question 3 (IQ 9): A car travels 180 miles in 3 hours. What is its average speed in miles per hour?")
    answer13 = input("Your answer here: ")
    if answer13.strip().lower() == "60 miles":
        print("Good guess!")
        total_score2 += question3med
    else:
        print("Incorrect.")
    print("====================================")
    #forth
    print("If 7x - 4 = 18, what is the value of x?")
    answer14 = float(input("Your answer here: "))
    if answer14  == 3.14:
        print("Good guess!")
        total_score2 += question4med
    else:
        print("Incorrect.")
    print("====================================")
    #fifth
    print("What is the area of a rectangle with a length of 12 units and a width of 9 units?")
    answer15 = int(input("Your answer here: "))
    if answer15  == 108:
        print("Good guess!")
        total_score2 += question5med
    else:
        print("Incorrect.")
    print("====================================")
    #six
    print("In a group of 80 people, 30 are interested in hiking, 25 are interested in swimming, and 10 are interested in both. How many people are interested in either hiking or swimming?")
    answer16 = int(input("Your answer here: "))
    if answer16  == 25:
        print("Good guess!")
        total_score2 += question6med
    else:
        print("Incorrect.")
    print("====================================")
    #seven
    print("What is the 8th letter of the English alphabet?")
    answer17 = input("Your answer here: ")
    if answer17.strip().lower() == 'H'.lower():
        print("Good guess!")
        total_score2 += question7med
    else:
        print("Incorrect.")
    print("====================================")    
    #eight
    print("Calculate the average (mean) of these numbers: 22, 27, 32, 37, 42.")
    answer18 = float(input("Your answer here: "))
    if answer18  == 29.5:
        print("Good guess!")
        total_score2 += question8med
    else:
        print("Incorrect.")
    print("====================================")
    #nine
    print("Solve for y: 4y + 15 = 39.")
    answer19 = input("Your answer here: ")
    if answer19.strip().lower() == "6": 
        print("Good guess!")
        total_score2 += question9med
    else:
        print("Incorrect.")
    print("====================================")
    #ten
    print("A number is increased by 50%, and then decreased by 50%. What is the final percentage change compared to the original number?")
    answer20 = input("Your answer here: ")
    if answer20.strip().lower() == "decreased by 50%":
        print("Good guess!")
        total_score2 += question10med
    else:
        print("Incorrect.")

    print("====================================")
    # Print the total Iq
    print("Your total Iq is:", total_score2)


if difficulty == 3:
    print("====================================")

    total_score3 = 0

    # Define scores
    question1hard = 15
    question2hard = 15
    question3hard = 15
    question4hard = 15
    question5hard = 15
    question6hard = 15
    question7hard = 15
    question8hard = 15
    question9hard = 15
    question10hard = 15
    goa_question = 25

    
    # First Question
    print("What is the next number in the series: 1, 8, 27, 64, 125, _? (Hint: These are cubes of integers.)")
    answer21 = input("Your answer here: ")
    if answer21 == "216":
        print("Good guess!")
        total_score3 += question1hard
    else:
        print("Incorrect.")
    print("====================================")
    # Second Question
    print("A puzzle involves finding a number that, when multiplied by 7 and then increased by 5, equals 50. What is the number?")
    answer22 = input("Your answer here: ")
    if answer22 == "6.5":
        print("Good guess!")
        total_score3 += question2hard
    else:
        print("Incorrect.")
    print("====================================")
    # Third Question
    print("If HORIZON is coded as IPSJAPO, how is ELEVATOR coded in the same manner?")
    answer23 = input("Your answer here: ")
    if answer23.strip().lower() == "FMFWBUPS".strip().lower():
        print("Good guess!")
        total_score3 += question3hard
    else:
        print("Incorrect.")
    print("====================================")
    #forth
    print("A container holds 1,200 liters of liquid. If 25%, of the liquid is removed, how many liters remain?")
    answer24 = input("Your answer here: ")
    if answer24.strip().lower() == "900 liters".strip().lower():
        print("Good guess!")
        total_score3 += question4hard
    else:
        print("Incorrect.")
    print("====================================")
    #fifth
    print("You have two ropes. Each rope takes exactly 70 minutes to burn completely when lit at one end. How can you measure exactly 85 minutes using these ropes?")
    answer25 = input("Your answer here: ")
    if answer25.strip().lower() == "measure 85 minutes with the two ropes.".strip().lower() or "85 minutes".lower():
        print("Good guess!")
        total_score3 += question5hard
    else:
        print("Incorrect.")
    print("====================================")
    #six
    print("What is the sum of the first 30 prime numbers?")
    answer26 = input("Your answer here: ")
    if answer26  == "1593":
        print("Good guess!")
        total_score3 += question6hard
    else:
        print("Incorrect.")
    print("====================================")
    #seven
    print("A sequence follows the rule where each term is twice the previous term plus 5. If the first term is 3, what is the 7th term?")
    answer27 = input("Your answer here: ")
    if answer27 == '507':
        print("Good guess!")
        total_score3 += question7hard
    else:
        print("Incorrect.")
    print("====================================")    
    #eight
    print("Calculate the area of a parallelogram with a base of 10 units and a height of 15 units.")
    answer28 = input("Your answer here: ")
    if answer28  == "150":
        print("Good guess!")
        total_score3 += question8hard
    else:
        print("Incorrect.")
    print("====================================")
    #nine
    print("If a number is increased by 40%, and then decreased by 40%, what is the final percentage change compared to the original number?")
    answer29 = input("Your answer here: ")
    if answer29 == "16%": 
        print("Good guess!")
        total_score3 += question9hard
    else:
        print("Incorrect.")
print("====================================")
    #ten
print("A clock shows 7:25. What is the angle between the hour and minute hands?")
answer30 = input("Your answer here: ")
if answer30.strip().lower() == "72.5 degrees.".strip().lower():
    print("Good guess!")
    total_score3 += question10hard
else:
    print("Incorrect.")
    
    print("====================================")
    print("hardest question, best proggraming accademy in the world?")
    goa_answer = input("your answer here: ")
    if goa_answer.strip().lower() == "GOA".lower() or "GOA best".lower():
        total_score3 += goa_question
    else:
        print("- unlimited aura")

print("====================================")
# Print the total Iq
print("Your total Iq is:", total_score3)

print("====================================")

task_ask_question = input("Do you want to play bonus fight: ")
if task_ask_question.strip().lower() == "yes":
    print("Alright Then")
print("====================================")
print("there will be 3 riddle, first one will be eazy, second one medium, and final hard.")
print("====================================")
press_enter = input("press enter to continue, if you dont want to continue enter(no/end)")
if press_enter != "":
    print("thank you for playing, goodbye")
    quit()

total_score4 = 0

riddleiq = 10
riddleiq2 = 15
riddleiq3 = 20

print("====================================")
print("alright then there is a first question")

print("====================================")
print("Im tall when Im young, and Im short when Im old. What am I?")
riddle_answer1 = input("your answer here: ")
if riddle_answer1.strip().lower() == "Candle".lower():
    print("bravo!")
    total_score4 += riddleiq
else:
    print("incorrect!")
print("====================================")
print("What can you catch but cant throw?")
riddle_answer2 = input("your answer here: ")
if riddle_answer2.strip().lower() == "Cold".lower():
    print("WoW!")
    total_score4 += riddleiq2
else:
    print("incorrect!")
print("====================================")

print("I speak without a mouth and hear without ears. I have no body, but I come alive with the wind. What am I?")
riddle_answer3 = input("your answer here: ")
if riddle_answer3.strip().lower() == "Echo".lower():
    print("bravo!")
    total_score4 += riddleiq
else:
    print("incorrect!")
print("====================================")
if difficulty == 1:
    print("congrats, your final iq is", total_score4 + total_score)

elif difficulty == 2:
    print("congrats, your final iq is", total_score4 + total_score2)

elif difficulty == 3:
    print("congrats, your final iq is", total_score4 + total_score3)

print("====================================")
print("thank you for playing! goodbye.")







    



