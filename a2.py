import random

def game():
    print("welcome to the game")
    score = random.randint(1, 62)
    # fetch highscore
    with open("hiscore.txt") as f:
        hiscore = f.read()
        if(hiscore != ""):
f            hiscore = int(hiscore)
        else:
            hiscore = 0

    print(f"your score :{score}")
    if(score>hiscore):
        with open("hiscore.txt", "w") as f:
            f.write(str(score))
    return(score)
game()   