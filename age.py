import time
print("Age Checker")
time.sleep(2)
age = int(input("Enter your age: "))
if age <= 10:
    print("You are a Child.")
elif age > 10 and age <= 20:
    print("You are a Teenager.")
elif age > 20 and age <= 40:
    print("You are an Adult.")
else:
    print("You are a Senior Citizen.")