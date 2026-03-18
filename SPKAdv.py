import random

# Function to get user choice
def get_user_choice():
    user = input("Enter your choice (s for stone, p for paper, k for knife): ")
    return user

# Function to play game
def play_game():
    
    yourDict = {"s":0,"p":1,"k":2}
    revDict = {0:"stone",1:"paper",2:"knife"}

    computer = random.choice([0,1,2])
    user = get_user_choice()

    # convert user input to number
    you = yourDict[user]

    print(f"You chose {revDict[you]} \nComputer chose {revDict[computer]}")

    if computer == you:
        print("Draw")
    else:
        if computer == 0 and you == 1:
            print("You won")
        elif computer == 0 and you == 2:
            print("You lose")
        elif computer == 1 and you == 2:
            print("You lose")
        elif computer == 1 and you == 0:
            print("You won")
        elif computer == 2 and you == 0:
            print("You lose")
        elif computer == 2 and you == 1:
            print("You won")

# main program
play_game()