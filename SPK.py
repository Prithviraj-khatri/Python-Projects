#.
import random
computer = random.choice([0,1,2])
user = input("enter your choice: ")
yourDict = {"s":0,"p":1,"k":2}
revDict = {0:"stone",1:"paper",2:"knife"}

you = yourDict[user]

print(f"you choose {revDict[you]}\n commputer choose {revDict[computer]}")

if(computer == you):
    print("draw")
else:
    if (computer == 0 and you == 1):
        print("you won")
    elif (computer == 0 and you == 2):
        print("you lose")
    elif (computer == 1 and you == 2):
        print("you lose")
    elif (computer == 1 and you == 0):
        print("you won")
    elif (computer == 2 and you == 0):
        print("you lose")
    elif (computer == 2 and you == 1):
        print("you won")
    else:
        print("something went wrong")
    
