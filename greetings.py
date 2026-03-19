#.
import time
print("Greetings")
time.sleep(2)
timme = int(input("Enter current time: "))
if timme >=1 and timme<= 7:
    print("Good night")
elif timme >= 8 and timme <= 12:
    print("good morning.")
elif timme >= 13 and timme <= 18:
    print("Good Afternoon")
elif timme >= 19 and timme <= 24:
    print("good evening")
else:
    print("enter time between 1 to 24")