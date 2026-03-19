#.
import time
print("hello welcome to the game")
time.sleep(2)
user_input = input("Enter your name: ")
time.sleep(2)
print(f"hello!{user_input} welcome to the kbc")
time.sleep(2)
question=("What is capital of india")
print(f"{question}")
options=["Delhi","Mumbai","Bengluru"]
print(f"your option are {options}")
user_answer = input("Enter your answer: ")
if user_answer not in options:
    print("please choose from above options")
else:
    if user_answer == "Delhi":
        print("your answer is correct")
    else:
        print("your answer is wrong") 