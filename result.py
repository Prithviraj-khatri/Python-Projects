# Function to take student details
def get_student_details():
    name = input("Enter student name: ")
    marks1 = int(input("Enter marks of Subject 1: "))
    marks2 = int(input("Enter marks of Subject 2: "))
    marks3 = int(input("Enter marks of Subject 3: "))
    return name, marks1, marks2, marks3


# Function to calculate result
def calculate_result(m1, m2, m3):
    total = m1 + m2 + m3
    percentage = total / 3

    if percentage >= 90:
        grade = "A"
    elif percentage >= 75:
        grade = "B"
    elif percentage >= 50:
        grade = "C"
    else:
        grade = "Fail"

    return total, percentage, grade


# Function to display result
def show_result(name, total, percentage, grade):
    print("\n----- RESULT -----")
    print(f"Name: {name}")
    print(f"Total Marks: {total}")
    print(f"Percentage: {percentage:.2f}%")
    print(f"Grade: {grade}")


# Main program
name, m1, m2, m3 = get_student_details()
total, percentage, grade = calculate_result(m1, m2, m3)
show_result(name, total, percentage, grade)