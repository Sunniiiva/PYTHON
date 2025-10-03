

#Correct login credentials 
login_credentials = {"username":"PGR107", "password":"Python"}

#login_info function that checks if the userinput for username and password corresponds to the correct login credentials 
def login_info(login_credentials, input_credentials):
    if input_credentials == login_credentials:
        return True
    else:
        return False


#A list with all the questions and anwers 
questions = [
    {
        "question":"\n\nQuestion 1 - What is the capital of Norway?\n",
        "options": "a. Bergen\nb. Oslo\nc. Stavanger\nd. Trondheim\n",
        "correct_answer": ["b. Oslo", "b", "Oslo", "oslo"]
    }, 
    
    {
       "question":"\n\nQuestion 2 - What is the currency in Norway?\n",
        "options": "a. Euro \nb. Pound\nc. Krone\nd. Deutsche Mark\n",
        "correct_answer": ["c. Krone", "c", "Krone", "c."]
    },

    {
        "question":"\n\nQuestion 3 - What is the largest city in Norway?\n",
        "options": "a. Oslo\nb. Stavanger\nc. Bergen\nd. Trondheim\n",
        "correct_answer": ["a. Oslo", "a", "a.", "Oslo", "oslo"]
    },
    
     {
        "question":"\n\nQuestion 4 - When is the constitution day of Norway?\n",
        "options": "a. 27. May\nb. 17. May\nc. 17. April\nd. 27. April\n",
        "correct_answer": ["b. 17. May", "b", "b.", "17. May", "17. may"]
    },

      {
        "question":"\n\nQuestion 5 - What color is the background of the Norwegian flag?\n",
        "options": "a. Red\nb. White\nc. Blue\nd. Yellow\n",
        "correct_answer": ["a. Red", "a", "a.", "Red"]
    },

      {
        "question":"\n\nQuestion 6 - Hoe many countries does Norway border?\n",
        "options": "a. 1\nb. 2\nc. 3\nd. 4\n",
        "correct_answer": ["c. 3", "c", "c.", "3"]
    },

      {
        "question":"\n\nQuestion 7 -  What is the name of the university in Trondheim?\n",
        "options": "a. UiS\nb. UiO\nc. NMBU\nd. NTNU\n",
        "correct_answer": ["d. NTNU", "d", "d.", "NTNU", "ntnu"]
    },

      {
        "question":"\n\nQuestion 8 -  How long  is the border between Norway and Russia?\n",
        "options": "a. 96 km\nb. 196 km\nc. 296\nd. 396\n",
        "correct_answer": ["b. 196", "b", "b.", "196"]
    },

      {
        "question":"\n\nQuestion 9 -  Where in Norway is Stavanger?\n",
        "options": "a. North\nb. South\nc. South-west\nd. South-east\n",
        "correct_answer": ["d. NTNU", "d", "d.", "NTNU", "ntnu"]
    },

      {
        "question":"\n\nQuestion 10 -  From wich Norwegian city did the world's famous composter Edvard Grieg come?\n",
        "options": "a. Oslo\nb. Bergen\nc. Stavanger\nd. Tromsø\n",
        "correct_answer": ["b. Bergen", "b", "b.", "bergen", "Bergen"]
    },
]

#Function for the quiz that prints out the questions and options from the list above
def quiz(questions):

#variables for saving the correct and incorrect answers 
   number_of_correct_answers = 0
   number_of_incorrect_answers = 0
   incorrect_answers = []


   #Loop that prints out each question with options and promts for an answer
   for i in range(len(questions)):
    print(questions[i]["question"])
    print(questions[i]["options"])
    input_answer = input("Enter your answer: ")
    
    #Checks if the answer is correct and saves the answer
    if input_answer in questions[i]["correct_answer"]:
        number_of_correct_answers += 1
    else:
        number_of_incorrect_answers += 1 
        incorrect_answers.append({
            "question": questions[i]["question"],
            "options": questions[i]["options"],
            "input_answer": input_answer,
            "correct_answer": questions[i]["correct_answer"][0]
            })  
            
  #Prints out the results at the end of the quiz
   print(f"\n\n\n---------------QUIZ RESULTS---------------\n\ncorrect answers: {number_of_correct_answers}")
   print(f"Incorrect answers:  {number_of_incorrect_answers}")
   print(f"Points: {number_of_correct_answers*2} \n\n\n\n -------------WRONG ANSWERS-------------" )
   for answer in incorrect_answers:
    print(f"{answer["question"]} \n{answer["options"]} \nYOUR ANSWER: {answer["input_answer"]} \nCORRECT ANSWER: {answer["correct_answer"][0]}")
   

   
#while loop that prints the login prompt when the function until the username and password is correct
while True:
  usernameInput = input("Enter username:")
  passwordInput = input("Enter password:")
  input_credentials = {"username": usernameInput, "password": passwordInput}

  if login_info(login_credentials, input_credentials):
     quiz(questions)
     break          
  else:
    print("Invalid username and/or password.")



