#..
import time
def welcome():
    print("Welcome to KBC")
    time.sleep(1)
    name = input("Enter your name: ")
    print(f"Welcome {name} to KBC")
    time.sleep(1)

def question_1():
    question = "What is capital of India"
    options =["Delhi","Mumbai","Jaipur"]
    print(question)
    print("options: ", options)
    answer = input("Enter your answer: ")
    if answer not in options:
        print("Choose from given options")
    else:
        if answer == "Delhi":
            print("Your Answer is correct")
        else:
            print("Your answer is incorrect")
            time.sleep(1)

def question_2():
    question = "Who is PM India"
    options =["Modi","Rahul","Prithvi"]
    print(question)
    print("options: ", options)
    answer = input("Enter your answer: ")
    if answer not in options:
        print("Choose from given options")
    else:
        if answer == "Prithvi":
            print("Your Answer is correct")
        else:
            print("Your answer is incorrect")
            time.sleep(1)

def question_3():
    question = "What language is used in AI"
    options =["python","java","html"]
    print(question)
    print("options: ", options)
    answer = input("Enter your answer: ")
    if answer not in options:
        print("Choose from given options")
    else:
        if answer == "Python":
            print("Your Answer is correct")
        else:
            print("Your answer is incorrect")
            time.sleep(1)
welcome()
question_1()
question_2()
question_3()