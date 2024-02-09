                                    # Name:Ashhal Ahmed
                                    # Gmail:Ashhalahmed8@gmail.com
                                    # PYTHON MATH QUIZ
# IMPORTING LIBARIES
import random
import math
# PRINTING
print("_________Welcome to the Math Quiz!____________")
print() #FOR MOVING TO ANOTHER LINE
print("______________________________Please create a username.______________________________")
# Taking input from the user for their username
username=input()
# SCORING CREATIRIA 
score=0
# GREETING USER
print(f"__________Welcome {username}__________")
print()
# Choosing levels
difficulty = input("Choose difficulty of Quiz (easy/intermediate/advanced): ").lower()
# CONDITIONS AS PER USER SELECTION LEVEL OF DIFFICULTY
print()
if difficulty=="easy":
    print("__________Like to know that you will be playing easy mode of quiz_______________")
    print()
    print("NOTE:You need to enter 2 numbers after decimal,Otherwise your answer will be considered as wrong")
elif difficulty == "intermediate":
    print("__________Like to know that you will be playing intermediate mode of quiz_______________")
    print()
    print("NOTE:You need to enter 2 numbers after decimal,Otherwise your answer will be considered as wrong")
elif difficulty == "advanced":
     print("__________Like to know that you will be playing advanced mode of quiz_______________")
     print()
     print("NOTE:You need to enter 2 numbers after decimal,Otherwise your answer will be considered as wrong")
# SHOW THE ERROR IF THE USER HAS NOT SELECTED BY THE CONDITIONS
if difficulty not in ["easy", "intermediate", "advanced"]:
  print("Invalid difficulty level. Please choose from easy, intermediate, or advanced.")
# PRINTNG ABOUT THE QUESTION HOW MUXH QUESTION WILL BE THERE
print()
print(f"There will be 10 questions in the Quiz")

print("_______________________________GOOD LUCK____________________________________")
# MAKING THE FUNCTION TO SUMMARIEZ THE CODE..BASIC2Y THIS FUNCTION IS RETURNING THE VALUES AS PER THE SELECTION OF THE USER FROM THE LEVEL OF DIFFICULTIES
def choosing_levels(difficulty):
    if difficulty == "easy":
        return 1, 10,
    elif difficulty == "intermediate":
        return 5, 50
    elif difficulty == "advanced":
        return 20,30      
# THIS FUNCTION IS RETURNING THE SUM OF THE OPERATOR LIKE: WHICH OPERATOR WILL DO THE TASK OF ADDITION,SUBTRACTION,MULTIPLICATION OR DIVISIONS
def calculate_answer(num1, num2, operator):
    if operator == '+':
        return num1 + num2
    elif operator == '-':
        return num1 - num2
    elif operator == '*':
        return num1 * num2
    elif operator == '/':
        # return f"{num1 / num2 :.2f}" 
        return round(num1 / num2,2)
    # jee jee   
# THIS LOOP IS GENENRATING THE QUESTION BY THE HELP OF RANDOM LIBARY,PRINTING THE QUESTION,AND IF THE USER ANSWER IS CORRECT SO IT WILL IMPLMENT 1 OTHER IT WILL CONSIDER AS 0
for i in range(10):  
   num1 = random.randint(*choosing_levels(difficulty))
   num2 = random.randint(*choosing_levels(difficulty))
   operator = random.choice(['+', '-', '*', '/'])
   print(f"Q{i+1}) {num1} {operator} {num2} = ?")
   answer = calculate_answer(num1, num2, operator)
   user=eval(input('Enter answer \n'))
   if answer==user:
       score+=1
       print(f"YOU ARE CORRECT {username.upper()}!!!")
   else:
    print(f"You are wrong: Correct answer was {answer}")
# HERE IS THE RESULTS OF THE QUIZ,THE PERCENTAGE OF THE USER AND THE SCORING CRETIRA 
print()
percentage_correct = (score / 10) * 100
print()
print(f"{username.upper()} Your score is: {score}/10")
print()
print(f"Percentage: {percentage_correct}%")
# GIVING THE REMARKS BY THE ANSWERS ANS THE SCORING OF THE USER
if score == 10:
    print(f"{username.upper()} ______________________YOU ARE THE BEST AT MATH!_________________________")
elif score <= 7:
    print(f"{username.upper()} ____________________YOU ARE NOT DOING WELL IN MATH YOU NEED TO DO MORE PRATICE!______________________")
print()
print(f"THANKS {username.upper()} FOR PLAYING THIS QUIZ")
