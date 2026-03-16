import time
def welcome():
    print("Hello welcome to the game")
    time.sleep(2)
    name = input("Enter your name: ")
    print(f"Hello {name}! Welcome to KBC")
    time.sleep(2)
def ask_question():
    question = "What is capital of India?"
    options = ["Delhi", "Mumbai", "Bengaluru"]
    print(question)
    print("Your options are:", options)
    answer = input("Enter your answer: ")
    if answer not in options:
        print("Please choose from above options")
    else:
        if answer == "Delhi":
            print("Your answer is correct")
        else:
            print("Your answer is wrong")
welcome()
ask_question()